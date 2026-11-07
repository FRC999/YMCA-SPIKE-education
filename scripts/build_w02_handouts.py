"""Typeset Week 2 Markdown handouts and assemble the exact class packet.

Run after regenerating the workbook's Week 2 team sheet. Requires reportlab/pypdf.
Inspect PDFs before recording their hashes with check_reading_copies.py.
"""
from pathlib import Path
import re
from xml.sax.saxutils import escape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from pypdf import PdfReader, PdfWriter

ROOT=Path(__file__).resolve().parents[1]
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Main',fontName='Helvetica-Bold',fontSize=20,leading=24,spaceAfter=12))
styles.add(ParagraphStyle(name='Head',fontName='Helvetica-Bold',fontSize=12,leading=15,spaceBefore=9,spaceAfter=6))
styles.add(ParagraphStyle(name='Body',fontName='Helvetica',fontSize=10.5,leading=14,spaceAfter=7))

def typeset(rel,pages):
    src=ROOT/rel;story=[]
    for block in src.read_text(encoding='utf-8-sig').strip().split('\n\n'):
        if block.startswith('## Rehearse'):
            story.append(PageBreak())
        style='Main' if block.startswith('# ') else 'Head' if block.startswith('## ') else 'Body'
        for line in block.splitlines():
            line=re.sub(r'^#{1,2} ','',line)
            line=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',line)
            line=escape(line)
            line=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',line)
            story.append(Paragraph(line,styles[style]))
    dest=src.with_suffix('.pdf')
    def footer(c,d):
        c.setFont('Helvetica',8);c.drawString(42,23,'MechaRAMS / Cheshire YMCA / Week 2');c.drawRightString(570,23,str(d.page))
    SimpleDocTemplate(str(dest),pagesize=(612,792),leftMargin=42,rightMargin=42,topMargin=34,bottomMargin=40).build(story,onFirstPage=footer,onLaterPages=footer)
    actual=len(PdfReader(dest).pages)
    if actual!=pages:raise ValueError(f'{dest.name}: expected {pages} pages, got {actual}')
    print(dest.name,actual)

def packet():
    writer=PdfWriter();folder=ROOT/'02_Student/Printouts'
    for name,count in [('W02_delivery_Team_Sheet.pdf',5),('W02_delivery_Build_Card.pdf',4),('W02_Wheel_Reference.pdf',4),('Attendance.pdf',1)]:
        reader=PdfReader(folder/name)
        assert len(reader.pages)==1,name
        for _ in range(count):writer.add_page(reader.pages[0])
    assert len(writer.pages)==14
    with (folder/'W02_Class_Print_Packet.pdf').open('wb') as f:writer.write(f)
    print('W02_Class_Print_Packet.pdf: 14 pages')

if __name__=='__main__':
    typeset('02_Student/Printouts/W02_Wheel_Reference.md',1)
    typeset('01_Instructor/Class_Preparation/W02_delivery_Checklist.md',2)
    packet()
