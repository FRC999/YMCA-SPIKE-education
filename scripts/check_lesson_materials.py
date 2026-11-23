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
LESSONS = ['W01_signal', 'W02_delivery', 'W03_dance', 'W04_cone_rematch',
           'W05_marker', 'W06_rescue', 'W07_speed_trial', 'W08_showcase']


def norm(text):
    return re.sub(r'\s+', ' ', text).strip()


def check():
    errors = []
    for name in LESSONS:
        files = [f'03_Presentations/{name}.{ext}' for ext in ('pptx', 'pdf')]
        files += [f'01_Instructor/Speaker_Notes/{name}_Speaker_Notes.{ext}'
                  for ext in ('docx', 'md')]
        if name != 'W08_showcase':
            files.append(f'04_Python/{name}.py')
        if name == 'W04_cone_rematch':
            files += ['02_Student/Printouts/W04_Cone_Rematch.pdf',
                      '02_Student/Printouts/W04_Cone_Rematch_Full_Size_Field.pdf',
                      '02_Student/Printouts/W04_Class_Print_Packet.pdf',
                      '01_Instructor/Class_Preparation/W04_cone_rematch_Guide.md']
        elif name == 'W05_marker':
            files += ['02_Student/Printouts/W05_Sensor_Mission.pdf',
                      '02_Student/Printouts/W05_Delivery_Strip_Full_Size_Field.pdf',
                      '02_Student/Printouts/W05_Class_Print_Packet.pdf',
                      '04_Python/W05_distance_demo.py',
                      '01_Instructor/Class_Preparation/W05_sensor_mission_Guide.md']
        else:
            files += [f'02_Student/Printouts/{name}_Build_Card.{ext}'
                      for ext in ('md', 'pdf')]
            files += [f'01_Instructor/Class_Preparation/{name}_Checklist.{ext}'
                      for ext in ('md', 'pdf')]
            if name == 'W08_showcase':
                files += ['02_Student/Printouts/W08_showcase_Timed_Team_Sheet.pdf',
                          '02_Student/Printouts/W08_Class_Print_Packet.pdf']
            else:
                files.append(f'02_Student/Printouts/{name}_Team_Sheet.pdf')
        missing = [f for f in files if not (ROOT/f).is_file()]
        if missing:
            errors.extend('Missing: '+f for f in missing)
            continue
        for file in files:
            if file.endswith('.py'):
                ast.parse((ROOT/file).read_text(encoding='utf-8-sig'))
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
        expected_count = {'W02_delivery': 15, 'W03_dance': 7}.get(name, 6)
        if len(sections) != expected_count + 1:
            errors.append(f'{name}: expected preparation plus {expected_count} slide sections')
            continue
        with ZipFile(ROOT/f'03_Presentations/{name}.pptx') as z:
            slide_files = [f for f in z.namelist()
                           if re.fullmatch(r'ppt/slides/slide\d+.xml', f)]
            if len(slide_files) != expected_count:
                errors.append(f'{name}: expected {expected_count} slides')
            for i in range(1, expected_count + 1):
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
        print(f'{name}: material set and {expected_count} note sections checked')
    if errors:
        raise SystemExit('\n'.join(errors))
    print('All eight lesson sets agree. Hardware rehearsal remains separate.')


if __name__ == '__main__':
    check()
