import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('reading_copies', Path(__file__).resolve().parents[1] / 'scripts/check_reading_copies.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ReadingCopiesTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'source.md').write_bytes(b'First\nSecond\n')
        (self.root / 'view.pdf').write_bytes(b'export')
        self.entries = [{'output': 'view.pdf', 'sha256': '', 'sources': {'source.md': ''}}]
        module.record(self.root, self.entries, ['view.pdf'])

    def test_source_and_export_drift_are_detected(self):
        self.assertEqual(module.check(self.root, self.entries), [])
        (self.root / 'source.md').write_bytes(b'New text')
        (self.root / 'view.pdf').write_bytes(b'New export')
        self.assertEqual(len(module.check(self.root, self.entries)), 2)

    def test_text_line_endings_do_not_create_cross_platform_drift(self):
        (self.root / 'source.md').write_bytes(b'First\r\nSecond\r\n')
        self.assertEqual(module.check(self.root, self.entries), [])

    def test_missing_source_is_reported(self):
        (self.root / 'source.md').unlink()
        self.assertIn('Missing source.md', module.check(self.root, self.entries)[0])

    def test_unknown_record_does_not_silently_accept_typo(self):
        with self.assertRaises(ValueError):
            module.record(self.root, self.entries, ['typo.pdf'])

    def test_repository_escape_is_rejected(self):
        with self.assertRaises(ValueError):
            module.local_path(self.root, '../outside.pdf')


if __name__ == '__main__':
    unittest.main()
