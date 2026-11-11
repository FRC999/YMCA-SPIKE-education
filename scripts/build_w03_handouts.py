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
 entries=[('Week 3 cone pusher preparation', 'Main'), ('Attach the team pusher and guide the cone during the robot dance', 'Body'), ('Print', 'Head'), ('[ ] 5 team sheets + 4 build cards + 1 attendance sheet = 10 required pages. Reuse role cards/hub guides; this checklist and lead notes are optional.', 'Body'), ('Pack and match the mounts', 'Head'), ('[ ] Reusable kit: 2 assembled robots, 4 laptops/chargers, tested cables, 14 pencils/erasers, 4 rulers, 4 team trays and 2 timers.', 'Body'), ('[ ] 6 matching lightweight cones with flat bases (suggested height 4-8 cm): 4 team props and 2 robot props. Check sliding on the actual surface.', 'Body'), ('[ ] 4 pusher packs with compatible pins/beams, two mounts, braces and short side guides; optional pre-cut card and craft tape. 4 mounting proxies and 2 mentor pushers. Keep bases assembled.', 'Body'), ('[ ] Mark two actual front mounting points; verify proxy spacing, height and wheel outline. Tape for starts and two clear floor areas covering the full swept dance path.', 'Body'), ('Rehearse on BOTH kits', 'Head'), ('[ ] Read W03_dance_Checklist.md. A left/B right, auxiliary unplugged; no sensors. Check Stop/save. Fit pusher while stopped; clear floor, wheels, cables and buttons.', 'Body'), ('[ ] Test WITH cone and pusher: repeat await drive(90), await turn(90) three times; await signal("D") outside. SPEED = 200. A wheel turn is not a heading angle. Rehearse a smaller positive turn if needed; retain turns.', 'Body'), ('[ ] Success: 3 complete drive-and-turn repeats, secure mount, cone upright inside guide. Record repeats before failure (0-3). Stop for tip/escape/loose mount; reset only when stopped.', 'Body'), ('Teach and close', 'Head'), ('[ ] Build with proxies; hand-check a gentle push and turn. Each team MUST attach and test its own pusher on the actual robot. Cone slides freely, not fastened or carried.', 'Body'), ('[ ] Use mentor pushers for early coding turns; swap to team builds for 38-50 minute retests. Change one build feature, hold dance code fixed, rerun. Preserve driver turns and minute-50 reflection.', 'Body'), ('[ ] Save four projects, label builds, count supplies and record real results in SESSION_PREP.md. Keep completed child records private.', 'Body')]
 write('01_Instructor/Class_Preparation/W03_dance_Checklist.pdf',[para(t,st) for t,st in entries])
if __name__=='__main__':main()
