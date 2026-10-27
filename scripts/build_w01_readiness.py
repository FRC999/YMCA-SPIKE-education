#!/usr/bin/env python3
"""Render the Week 1 readiness guide and assemble its exact print quantities.

Requires reportlab and pypdf. Review rendered PDFs before recording export hashes.
"""
from pathlib import Path
from io import BytesIO
import re
from xml.sax.saxutils import escape

from pypdf import PdfReader, PdfWriter
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / '01_Instructor/Class_Preparation/W01_Readiness_Guide.md'
PACKET = ROOT / '02_Student/Printouts/W01_Class_Print_Packet.pdf'
SECTIONS = [
    ('02_Student/Printouts/W01_signal_Team_Sheet.pdf', 5, 1),
    ('02_Student/Printouts/W01_signal_Build_Card.pdf', 4, 1),
    ('02_Student/Printouts/Attendance.pdf', 1, 1),
    ('02_Student/Printouts/Role_Cards.pdf', 2, 2),
    ('06_References/SPIKE_Hub_Color_Guide.pdf', 2, 1),
]


def inline(text):
    text = escape(text)
    def link(match):
        label, url = match.groups()
        if not url.startswith('https://'):
            relative = (GUIDE.parent / url).resolve().relative_to(ROOT).as_posix()
            url = 'https://github.com/FRC999/YMCA-SPIKE-education/blob/main/' + relative
        return f'<a href="{url}" color="#145078">{label}</a>'
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, text)
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)


def guide_pdf():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='BodyReady', fontName='Helvetica', fontSize=10,
                              leading=12.5, spaceAfter=5, alignment=TA_LEFT))
    styles.add(ParagraphStyle(name='CheckReady', parent=styles['BodyReady'],
                              leftIndent=12, firstLineIndent=-12, spaceAfter=4))
    styles.add(ParagraphStyle(name='CellReady', parent=styles['BodyReady'],
                              fontSize=8.6, leading=11, spaceAfter=0))
    styles['Title'].fontSize = 22
    styles['Title'].leading = 25
    styles['Title'].alignment = TA_LEFT
    styles['Heading2'].fontSize = 16
    styles['Heading2'].leading = 19
    styles['Heading2'].textColor = colors.HexColor('#143f53')
    styles['Heading3'].fontSize = 11.5
    styles['Heading3'].leading = 14
    story = []
    lines = GUIDE.read_text(encoding='utf-8').splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        i += 1
        if not line.strip():
            continue
        if line == '<!-- pagebreak -->':
            story.append(PageBreak())
        elif line.startswith('|'):
            rows = [line]
            while i < len(lines) and lines[i].startswith('|'):
                rows.append(lines[i])
                i += 1
            cells = [[Paragraph(inline(cell.strip()), styles['CellReady'])
                      for cell in row.strip('|').split('|')]
                     for row in rows if not re.fullmatch(r'[|:\- ]+', row)]
            table = Table(cells, colWidths=[120, 115, 60, 221], repeatRows=1)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e3edf1')),
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
                ('GRID', (0,0), (-1,-1), .4, colors.HexColor('#b5c4ca')),
                ('TOPPADDING', (0,0), (-1,-1), 7),
                ('BOTTOMPADDING', (0,0), (-1,-1), 7),
            ]))
            story.extend([table, Spacer(1, 10)])
        elif line.startswith('# '):
            story.append(Paragraph(inline(line[2:]), styles['Title']))
        elif line.startswith('## '):
            story.append(Paragraph(inline(line[3:]), styles['Heading2']))
        elif line.startswith('### '):
            story.append(Paragraph(inline(line[4:]), styles['Heading3']))
        elif line.startswith('- [ ] '):
            story.append(Paragraph('[ ] ' + inline(line[6:]), styles['CheckReady']))
        elif line.startswith('- '):
            story.append(Paragraph('- ' + inline(line[2:]), styles['CheckReady']))
        else:
            story.append(Paragraph(inline(line), styles['BodyReady']))

    def footer(canvas, doc):
        canvas.setStrokeColor(colors.HexColor('#b5c4ca'))
        canvas.line(48, 37, 564, 37)
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(colors.HexColor('#48606c'))
        canvas.drawString(48, 25, 'MechaRAMS / Cheshire YMCA | First session | October 27, 2026')
        canvas.drawRightString(564, 25, str(doc.page))

    output = GUIDE.with_suffix('.pdf')
    SimpleDocTemplate(str(output), pagesize=letter, leftMargin=48, rightMargin=48,
                      topMargin=36, bottomMargin=48, title='First session readiness',
                      author='MechaRAMS / Cheshire YMCA').build(
                          story, onFirstPage=footer, onLaterPages=footer)
    pages = len(PdfReader(output).pages)
    if pages != 4:
        raise ValueError(f'Guide should fit four pages, got {pages}; inspect layout.')
    print(f'Readiness guide: {pages} pages')


def packet_pdf():
    writer = PdfWriter()
    expected_text = []
    for filename, copies, expected_pages in SECTIONS:
        source = PdfReader(BytesIO((ROOT / filename).read_bytes()))
        if len(source.pages) != expected_pages:
            raise ValueError(f'Unexpected source page count: {filename}')
        for _ in range(copies):
            for page in source.pages:
                writer.add_page(page)
                expected_text.append(page.extract_text())
    writer.add_metadata({'/Title': 'Week 1 class packet - print one copy, single-sided',
                         '/Author': 'MechaRAMS / Cheshire YMCA'})
    stream = BytesIO()
    writer.write(stream)
    PACKET.write_bytes(stream.getvalue())
    output = PdfReader(BytesIO(stream.getvalue()))
    if len(output.pages) != 16 or [p.extract_text() for p in output.pages] != expected_text:
        raise ValueError('Print packet failed quantity/content verification')
    print('Class packet: 16 pages; every page matches its ordered source text')


if __name__ == '__main__':
    guide_pdf()
    packet_pdf()
