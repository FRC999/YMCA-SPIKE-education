"""Typeset the optional timed-delivery handouts (reportlab/pypdf required).

Markdown is the maintained source. The checklist PDF is a packing summary;
its full rehearsal procedure remains in the Markdown and speaker notes.
Render and inspect outputs before recording hashes in reading_copies.json.
"""
from pathlib import Path
from io import BytesIO
import re
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
STYLES=getSampleStyleSheet()
STYLES.add(ParagraphStyle(name='Body',fontName='Helvetica',fontSize=10.3,leading=13.5,spaceAfter=7))
STYLES.add(ParagraphStyle(name='Small',parent=STYLES['Body'],fontSize=9.3,leading=12,spaceAfter=5))
STYLES.add(ParagraphStyle(name='Head',fontName='Helvetica-Bold',fontSize=12,leading=15,spaceBefore=6,spaceAfter=6))
STYLES.add(ParagraphStyle(name='Main',fontName='Helvetica-Bold',fontSize=20,leading=23,spaceAfter=12))
STYLES.add(ParagraphStyle(name='Cell',fontName='Helvetica',fontSize=9,leading=11,spaceAfter=0))

def p(text,style='Body'):
    text=escape(text)
    text=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',text)
    return Paragraph(text,STYLES[style])

def pdf(relative,story):
    dest=ROOT/relative
    def footer(c,d):
        c.setFont('Helvetica',8);c.drawString(42,24,'MechaRAMS / Cheshire YMCA / Week 7 option');c.drawRightString(570,24,str(d.page))
    SimpleDocTemplate(str(dest),pagesize=(612,792),leftMargin=42,rightMargin=42,topMargin=32,bottomMargin=38).build(story,onFirstPage=footer,onLaterPages=footer)
    pages=len(PdfReader(BytesIO(dest.read_bytes())).pages)
    if pages != 1:raise ValueError(f'{relative}: expected one page, got {pages}')
    print(f'{relative}: one page')

def build_card():
    src=ROOT/'02_Student/Printouts/W07_speed_trial_Build_Card.md'
    story=[]
    for block in src.read_text(encoding='utf-8').strip().split('\n\n'):
        if block.startswith('# '):story.append(p(block[2:],'Main'))
        elif block.startswith('## '):story.append(p(block[3:],'Head'))
        else:
            for line in block.splitlines():story.append(p(line))
    pdf('02_Student/Printouts/W07_speed_trial_Build_Card.pdf',story)

def team_sheet():
    story=[p('Week 7 timed delivery','Main'),p('Team ____   Kit ____   Date ____   Timed distance: 60 cm'),
        p('Our user and delivery job: __________________________________________'),
        p('Fixed travel: ____ wheel degrees. Approved speeds: ____________________'),
        p('We predict a speed change will: _____________________________________'),
        p('Keep kit, floor, start, cube, tray and travel fixed when comparing speed. Then compare our cradle at the same speed as the mentor tray. The mentor starts timing at first movement and stops at the chassis mark crossing the finish. Record seconds to one decimal place.','Small'),
        p('Valid (Y): crosses, keeps cargo, stays in lane and stops in the runout. Record N for any failure. Write DNF if it never crosses. Keep every attempt.','Small')]
    rows=[[p(t,'Cell') for t in ['Trial','Tray','Speed\nwheel deg/s','Time (s)\nor DNF','Valid\nY/N','What happened?']]]
    for group,tray,speed in [('A','Mentor','200'),('B','Mentor','____'),('C','Our cradle','____')]:
        for i in range(1,4):rows.append([p(t,'Cell') for t in [group+str(i),tray,speed,'____','____','']])
    table=Table(rows,colWidths=[35,65,80,76,55,217],rowHeights=[32]+[24]*9)
    table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#E8EEF1')),('GRID',(0,0),(-1,-1),.5,colors.HexColor('#D9D9D9')),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6)]))
    story += [table,Spacer(1,8),
        p('B is optional: one approved higher speed for all three runs, or mark SKIP. Use one unchanged speed for C, matching A or B. Each child drives once per set used.','Small'),
        p('Successful trials: A ____ / 3; B ____ / 3 or skipped; C ____ / 3.'),
        p('For a complete 3/3 valid set only: mean = (time 1 + time 2 + time 3) / 3.','Small'),
        p('Mean A ____ s; B ____ s; C ____ s. Leave blank if failed or incomplete.','Small'),
        p('Showcase choice: tray ____ speed ____; tested 3/3? ____'),
        p('Our build change and result: ________________________________________'),
        p('Next test: ______________________________________________________'),
        p('Close stopwatch times can be a tie. Choose a fast, reliable delivery supported by trials.','Small')]
    pdf('02_Student/Printouts/W07_speed_trial_Team_Sheet.pdf',story)

def checklist():
    story=[p('Week 7 timed delivery preparation','Main'),p('Optional mission replacement / 12 children / four teams / two kits'),
        p('Print','Head'),p('[ ] 5 speed team sheets + 4 speed build cards + 1 attendance sheet = 10 required sheets, single-sided. Replace the original Week 7 handouts. Reuse role cards and hub guides. This checklist and a lead note copy are optional.'),
        p('Pack','Head'),p('[ ] Reusable kit: two charged assembled bases, four laptops/chargers, tested cables, pencils, four team trays, mounting proxies, rulers and floor-safe tape.'),
        p('[ ] Two stopwatch devices plus a rotation timer; two mentor trays; six similar lightweight cubes; four equal build packs with eight rail strips, eight brace strips, four spare card panels, craft tape and four storage bags.'),
        p('[ ] Two clear FLOOR lanes at least 150 cm long and 50 cm wide; 60 cm timed section and clear runout. Two measuring tapes and fixed chassis-reference markers. Confirm more room if rehearsal requires it.'),
        p('Rehearse before class','Head'),p('[ ] Read the full W07_speed_trial_Checklist.md calibration procedure. Verify A left/B right, auxiliary motor unplugged, controls accessible and stop behavior on BOTH kits.'),
        p('[ ] Calibrate TRAVEL_DEGREES (1–1440; supplied 0 refuses motion). Keep travel fixed after calibration. Approve 200 first, then 300 only after three successful loaded rehearsals. Optional 400 needs the same check. No higher classroom speeds.'),
        p('[ ] Practice consistent stopwatch timing from first movement to chassis mark crossing. Judge cargo, lane and stopping validity through the end. Inspect a sample cradle and quick swap.'),
        p('[ ] Download matching speed slides/notes/full program. Save separate team projects with the correct kit settings. Assign two robot and two build mentors. If lanes cannot be supervised independently, alternate runs and omit the speed stretch.'),
        p('Record and close','Head'),p('Kit A travel ____ approved speeds ____ passed/date __________________'),p('Kit B travel ____ approved speeds ____ passed/date __________________'),
        p('[ ] Save four programs, label four cradles, keep completed sheets private and record actual results in SESSION_PREP.md. Showcase only a setting tested 3/3; reload that speed project in Week 8.'),
        p('If the speed setup is not reliable, use the original rehearsed Week 7 mission. Full rules, calibration and role timing are in the Markdown checklist and speaker notes.','Small')]
    pdf('01_Instructor/Class_Preparation/W07_speed_trial_Checklist.pdf',story)

if __name__=='__main__':
    build_card();team_sheet();checklist()
