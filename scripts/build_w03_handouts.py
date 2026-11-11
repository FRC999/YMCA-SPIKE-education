"""Build Week 3 cone handouts from maintained Markdown; inspect PDFs before recording hashes."""
from pathlib import Path
import re
from xml.sax.saxutils import escape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
from pypdf import PdfReader
R=Path(__file__).resolve().parents[1]
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Main',fontName='Helvetica-Bold',fontSize=20,leading=23,spaceAfter=10))
styles.add(ParagraphStyle(name='Head',fontName='Helvetica-Bold',fontSize=12,leading=15,spaceAfter=6,spaceBefore=6))
styles.add(ParagraphStyle(name='Body',fontName='Helvetica',fontSize=10.3,leading=13.3,spaceAfter=7))
def para(text,style='Body'):
 text=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',text)
 text=text.replace('–','-').replace('—','-').replace('’',"'").replace('**','@@')
 text=escape(text);text=re.sub(r'@@(.+?)@@',r'<b>\1</b>',text)
 return Paragraph(text,styles[style])
def write(rel,story):
 p=R/rel
 def footer(c,d):
  c.setFont('Helvetica',8);c.drawString(42,24,'MechaRAMS / Cheshire YMCA / Week 3');c.drawRightString(570,24,str(d.page))
 SimpleDocTemplate(str(p),pagesize=(612,792),leftMargin=42,rightMargin=42,topMargin=32,bottomMargin=38).build(story,onFirstPage=footer,onLaterPages=footer)
 assert len(PdfReader(p).pages)==1,rel
 print(rel, 'one page')
def main():
 src=R/'02_Student/Printouts/W03_dance_Build_Card.md';story=[]
 for line in src.read_text(encoding='utf-8-sig').splitlines():
  if line.strip():story.append(para(line[3:] if line.startswith('## ') else line[2:] if line.startswith('# ') else line,'Head' if line.startswith('## ') else 'Main' if line.startswith('# ') else 'Body'))
 write('02_Student/Printouts/W03_dance_Build_Card.pdf',story)
 # Deliberately compact packing summary; detailed steps stay in the source checklist.
 entries=[('Week 3 cone pusher preparation','Main'),('Robot dance studio + removable cone pusher / 12 children / four teams','Body'),('Print','Head'),('[ ] 5 team sheets + 4 build cards + 1 attendance sheet = 10 required pages. Reuse role cards and hub guides. This checklist and a lead note copy are optional.','Body'),('Pack','Head'),('[ ] Reusable kit: 2 assembled robots, 4 laptops/chargers, tested cables, 14 pencils/erasers, 4 rulers, 4 team trays and 2 timers.','Body'),('[ ] 6 matching lightweight cones with flat bases (suggested height 4-8 cm): 4 team props and 2 robot-lane props. Check that they slide on the actual surface.','Body'),('[ ] 4 equal pusher build packs, 4 mounting proxies and 2 mentor pushers. Beams/pins or pre-cut card, two mounting supports and braces per team, craft tape. Keep both bases assembled.','Body'),('[ ] Floor-safe tape for two clear lanes, starts and reachable target zones; 10 cm hand-test paths and zones wider than the cone at build tables.','Body'),('Rehearse on BOTH kits','Head'),('[ ] Read the full W03_dance_Checklist.md. Test original dance with pusher removed. A left/B right; auxiliary motor unplugged; no sensors required. Check Stop and save workflow.','Body'),('[ ] Fit on stopped base; clear wheels, floor, cables and buttons. Test quick swaps. Cone loop: three repeats of await drive(60), await pause(300); await signal("D") outside. SPEED = 200; no turns.','Body'),('[ ] Mark target for actual 180-wheel-degree travel. Rehearse three runs. Success: upright, whole cone base inside zone. Stop for tipping/escape; reset only after motion stops. Record actual results.','Body'),('Teach and close','Head'),('[ ] Hand-test three times, change one feature, repeat three times. Keep cone, floor, start and travel fixed. Rotate builder, designer and tester.','Body'),('[ ] Use 38-50 minute retests for fit and cone loop. Preserve each driver turn and minute-50 reflection. Use mentor pusher if team fit fails; share hand-test evidence.','Body'),('[ ] Save team projects, label four builds, count parts and record shortages/results in SESSION_PREP.md. Keep completed child records private.','Body')]
 write('01_Instructor/Class_Preparation/W03_dance_Checklist.pdf',[para(t,st) for t,st in entries])
if __name__=='__main__':main()
