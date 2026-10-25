"""Content preservation and stale-mirror checks; no external packages required."""
from contextlib import redirect_stdout, redirect_stderr
import html
import io
from pathlib import Path
import re
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import sync_documents as sync


def package(path, extra='', body=None):
    title = '<w:p><w:pPr><w:pStyle w:val="Title"/></w:pPr><w:r><w:t>Robot guide</w:t></w:r></w:p>'
    if body is None:
        body = '''
<w:p><w:pPr><w:pStyle w:val="Heading1"/></w:pPr><w:r><w:t>Build and test</w:t></w:r></w:p>
<w:p><w:r><w:rPr><w:b/></w:rPr><w:t xml:space="preserve">Goal </w:t></w:r><w:r><w:t>Keep A and B separate.</w:t></w:r></w:p>
<w:p><w:pPr><w:pStyle w:val="ListBullet"/></w:pPr><w:r><w:t>Check both kits.</w:t></w:r></w:p>
<w:tbl><w:tr><w:tc><w:p><w:r><w:t>Kit</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>Result</w:t></w:r></w:p></w:tc></w:tr>
<w:tr><w:tc><w:p><w:r><w:t>A</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>left | right</w:t></w:r></w:p><w:p><w:r><w:t>not checked</w:t></w:r></w:p></w:tc></w:tr></w:tbl>
<w:p><w:hyperlink r:id="rId1"><w:r><w:t>Official instructions</w:t></w:r></w:hyperlink></w:p>
<w:p><w:r><w:rPr><w:rFonts w:ascii="Consolas"/></w:rPr><w:t>for step in range(2):</w:t><w:br/><w:t xml:space="preserve">    await drive(90)</w:t></w:r></w:p>
<w:p><w:r><w:t>gap &lt; 150; student_recipe; __________</w:t></w:r></w:p>
'''
    document = f'<w:document xmlns:w="{sync.W}" xmlns:r="{sync.R}"><w:body>{title}{body}{extra}<w:sectPr/></w:body></w:document>'
    rels = '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Target="https://example.org/build?kit=A&amp;step=1" Type="hyperlink" TargetMode="External"/></Relationships>'
    with zipfile.ZipFile(path, 'w') as z:
        z.writestr('word/document.xml', document)
        z.writestr('word/_rels/document.xml.rels', rels)


def quiet_sync(root, write):
    with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
        return sync.sync(root, write)


class MirrorTests(unittest.TestCase):
    def test_preserves_order_links_tables_and_code_indentation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); source = root / 'sample.docx'; package(source)
            out = sync.render_docx(source, root)
            self.assertIn('## Build and test', out)
            self.assertIn('**Goal** Keep A and B separate.', out)
            self.assertIn('- Check both kits.', out)
            self.assertIn('| A | left \\| right<br><br>not checked |', out)
            self.assertIn('[Official instructions](https://example.org/build?kit=A&step=1)', out)
            self.assertIn('```python\nfor step in range(2):\n    await drive(90)\n```', out)
            self.assertLess(out.index('Check both kits'), out.index('| Kit |'))
            self.assertLess(out.index('| Kit |'), out.index('[Official instructions]'))

    def test_check_detects_missing_manual_drift_and_docx_edits(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); source = root / 'sample.docx'; package(source)
            self.assertEqual(quiet_sync(root, False), 1)
            self.assertEqual(quiet_sync(root, True), 0)
            self.assertEqual(quiet_sync(root, False), 0)
            md = source.with_suffix('.md')
            md.write_text(md.read_text(encoding='utf-8') + '\nUnpaired edit\n', encoding='utf-8')
            self.assertEqual(quiet_sync(root, False), 1)
            quiet_sync(root, True)
            package(source, '<w:p><w:r><w:t>A new instruction.</w:t></w:r></w:p>')
            self.assertEqual(quiet_sync(root, False), 1)
            self.assertEqual(quiet_sync(root, True), 0)
            self.assertIn('A new instruction.', md.read_text(encoding='utf-8'))

    def test_unsupported_content_does_not_erase_existing_mirrors(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); a = root / 'a.docx'; b = root / 'b.docx'
            package(a); quiet_sync(root, True)
            before = a.with_suffix('.md').read_bytes()
            package(a, '<w:p><w:r><w:t>Changed source</w:t></w:r></w:p>')
            package(b, '<w:p><w:r><w:drawing/></w:r></w:p>')
            with self.assertRaises(sync.UnsupportedContent): quiet_sync(root, True)
            self.assertEqual(a.with_suffix('.md').read_bytes(), before)

    def test_independent_markdown_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); source = root / 'sample.docx'; package(source)
            source.with_suffix('.md').write_text('# Independent document\n', encoding='utf-8')
            with self.assertRaises(ValueError): quiet_sync(root, True)
            self.assertEqual(source.with_suffix('.md').read_text(encoding='utf-8'), '# Independent document\n')

    def test_source_deletion_is_reported_and_build_files_are_ignored(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); a = root / 'a.docx'; b = root / 'b.docx'
            package(a); package(b); quiet_sync(root, True)
            a.unlink()
            build = root / '.build'; build.mkdir(); package(build / 'ignored.docx')
            self.assertEqual(quiet_sync(root, False), 1)
            self.assertTrue(a.with_suffix('.md').exists())
            self.assertFalse((build / 'ignored.md').exists())

    def test_all_repository_body_paragraphs_survive_in_reading_order(self):
        # Independent text-coverage audit includes table cells, repeated blanks,
        # source links and code. It catches loss even when a generator is deterministic.
        for source in sync.visible_files(ROOT, '*.docx'):
            out = sync.render_docx(source, ROOT)
            out = re.sub(r'\[([^\]]+)\]\([^\n]+?\)', r'\1', out)
            out = out.replace('**', '').replace('<br>', '\n')
            out = re.sub(r'\\([\\`*_\[\]|])', r'\1', out)
            out = html.unescape(out)
            out = re.sub(r'\s+', ' ', out)
            cursor = 0
            with zipfile.ZipFile(source) as z:
                document = ET.fromstring(z.read('word/document.xml'))
                for p in document.findall('.//w:body//w:p', sync.NS):
                    text = re.sub(r'\s+', ' ', sync.plain(p)).strip()
                    if not text: continue
                    pos = out.find(text, cursor)
                    self.assertNotEqual(pos, -1, f'{source.name}: missing/out-of-order {text[:90]!r}')
                    cursor = pos + len(text)


if __name__ == '__main__':
    unittest.main()
