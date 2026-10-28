"""Check complete lesson sets and embedded notes using only standard Python.

This checks file/content agreement, not layout or real hardware behavior.
"""
from pathlib import Path
import ast
import re
from xml.etree import ElementTree as ET
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
LESSONS = ['W01_signal', 'W02_delivery', 'W03_dance', 'W04_parking',
           'W05_marker', 'W06_rescue', 'W07_mission', 'W08_showcase',
           'W07_speed_trial']


def norm(text):
    return re.sub(r'\s+', ' ', text).strip()


def check():
    errors = []
    for name in LESSONS:
        files = [f'03_Presentations/{name}.{ext}' for ext in ('pptx', 'pdf')]
        files += [f'01_Instructor/Speaker_Notes/{name}_Speaker_Notes.{ext}'
                  for ext in ('docx', 'md')]
        files += [f'02_Student/Printouts/{name}_Build_Card.{ext}'
                  for ext in ('md', 'pdf')]
        files += [f'01_Instructor/Class_Preparation/{name}_Checklist.{ext}'
                  for ext in ('md', 'pdf')]
        files += [f'02_Student/Printouts/{name}_Team_Sheet.pdf',
                  f'04_Python/{name}.py']
        missing = [f for f in files if not (ROOT/f).is_file()]
        if missing:
            errors.extend('Missing: '+f for f in missing)
            continue
        ast.parse((ROOT/f'04_Python/{name}.py').read_text(encoding='utf-8-sig'))
        with ZipFile(ROOT/f'01_Instructor/Speaker_Notes/{name}_Speaker_Notes.docx') as z:
            body = ET.fromstring(z.read('word/document.xml'))
            paragraphs = [''.join((t.text or '') if t.tag == W+'t' else
                                  '\n' if t.tag == W+'br' else
                                  '\t' if t.tag == W+'tab' else '' for t in p.iter())
                          for p in body.iter(W+'p')]
        sections = []; current = []
        for p in paragraphs:
            if re.match(r'^Slide \d+ ', p):
                sections.append(current); current = [p]
            elif p.strip():
                current.append(p)
        sections.append(current)
        if len(sections) != 7:
            errors.append(f'{name}: expected preparation plus six slide sections')
            continue
        with ZipFile(ROOT/f'03_Presentations/{name}.pptx') as z:
            slide_files = [f for f in z.namelist()
                           if re.fullmatch(r'ppt/slides/slide\d+.xml', f)]
            if len(slide_files) != 6:
                errors.append(f'{name}: expected six slides')
            for i in range(1, 7):
                if not sections[i][0].startswith(f'Slide {i} '):
                    errors.append(f'{name}: note section order {i}')
                try:
                    tree = ET.fromstring(z.read(f'ppt/notesSlides/notesSlide{i}.xml'))
                except KeyError:
                    errors.append(f'{name}: missing embedded notes on slide {i}')
                    continue
                embedded = norm(' '.join(t.text or '' for t in tree.iter(A+'t')))
                expected = sections[0]+sections[1] if i == 1 else sections[i]
                if norm(' '.join(expected)) not in embedded:
                    errors.append(f'{name}: slide {i} notes differ from DOCX')
        print(f'{name}: material set and six note sections checked')
    if errors:
        raise SystemExit('\n'.join(errors))
    print('All eight core lessons and optional timed delivery agree. Hardware rehearsal remains separate.')


if __name__ == '__main__':
    check()
