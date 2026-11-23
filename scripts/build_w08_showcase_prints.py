"""Build the Week 8 timed showcase checklist, team sheet and class packet."""

from pypdf import PdfWriter
from pypdf.generic import NameObject
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen.canvas import Canvas

from build_w04_w05_mission_prints import LINE, MUTED, PALE, TEAL, para, stroke, text
from build_w04_w05_print_packets import PREP, PRINTS, Section, indexed_sections
from build_w04_w05_setup_checklists import checks, finish, item, section, title
from build_w07_speed_prints import COURSE, COURSE_H, COURSE_W, ROWS, RUNOUT, TIMED_LENGTH

CHECKLIST = PREP / 'W08_showcase_Checklist.pdf'
TEAM_SHEET = PRINTS / 'W08_showcase_Timed_Team_Sheet.pdf'
PACKET = PRINTS / 'W08_Class_Print_Packet.pdf'
LAST_TILE = 1 + 2 * len(ROWS)
PLAN = (
    Section('Mentor checklist', CHECKLIST),
    Section('Course assembly guide', COURSE),
    Section('Kit A course tiles', COURSE, 2, LAST_TILE),
    Section('Kit B course tiles', COURSE, 2, LAST_TILE),
    Section('Team sheets (4 teams + spare)', TEAM_SHEET, copies=5),
    Section('Build cards (1 per team)', PRINTS / 'W08_showcase_Build_Card.pdf', copies=4),
    Section('Final checks (12 + 2 spares)', PRINTS / 'Final_Check.pdf', copies=14),
    Section('Attendance', PRINTS / 'Attendance.pdf'),
)


def checklist(canvas):
    title(canvas, 8, 'Timed delivery showcase')
    index = list(indexed_sections(PLAN))
    text(canvas, 36, 660, f'Print this {index[-1][2]}-page packet once', 13, TEAL, True)
    text(canvas, 36, 642, 'US Letter / Actual Size (100%) / Single-sided / Auto page orientation', 10)
    canvas.setFillColor(HexColor(PALE))
    canvas.roundRect(36, 551, 540, 79, 6, stroke=0, fill=1)
    for i, (part, first, last) in enumerate(index):
        page_range = str(first) if first == last else f'{first}-{last}'
        x = 48 + 265 * (i // 4)
        y = 613 - 16 * (i % 4)
        text(canvas, x, y, f'{page_range}   {part.label}', 10)
    tile_first, tile_last = index[2][1], index[3][2]
    text(canvas, 36, 532, f'If both Week 7 courses are ready to reuse, skip pages {tile_first}-{tile_last}.', 10)
    text(canvas, 36, 517, 'Use the page ranges above. Page 2 lists the standalone Week 7 course page numbers.', 10, MUTED)

    y = section(canvas, '1  Set up both courses', 491)
    y = item(canvas, y, 'Reprinting? Check the 5 cm ruler on the guide. Trim and join rows A-H, L left of R. '
             'Match the paired ticks and tape from behind. Sort the two sets before cutting.')
    y = item(canvas, y, f'Tape each {COURSE_W} x {COURSE_H} cm course flat. Check {TIMED_LENGTH} cm from START '
             f'(row A) to FINISH (row D) and {RUNOUT} cm of printed runout. Leave clear floor at both ends.')

    y = section(canvas, '2  Rehearse the saved programs', y - 2)
    y = checks(canvas, y, [
        'Kit A serves T1/T2. Kit B serves T3/T4. Verify A left, B right, hub pairing and Stop.',
        'Open each team\'s saved Week 7 project offline. Match its recorded travel, approved speed, '
        'tray and cube to a 3/3 valid set. Use the kit that ran it in Week 7.',
        'Align the fixed chassis mark with START. Rehearse each saved configuration on its actual '
        'lane. Confirm the mark crosses, the cube stays aboard and the robot stops inside the runout.',
        'Start the stopwatch at first movement after the ready pause. Stop when that same mark '
        'crosses FINISH. Watch until the robot fully stops and confirm it stayed in the lane.',
    ])
    y = item(canvas, y, 'If a setup fails, use a rehearsed backup on its matching course or have the team show '
             'its Week 7 trial evidence. Use the marker fallback on a separately rehearsed marker lane.')
    y = section(canvas, '3  Stage the showcase', y - 2)
    y = item(canvas, y, 'Set out two stopwatches, saved cradles, cubes, repair kits and signs. Give each child a final '
             'check before coaching. Allow six minutes per team to rehearse and four minutes to present.')
    y = item(canvas, y, 'Assign one timekeeper per course. Alternate runs if both lanes cannot be supervised.')
    finish(canvas, y, 'W08_showcase.pptx')


def team_sheet(canvas):
    text(canvas, 36, 753, 'WEEK 8 / TEAM SHEET', 10, TEAL, True)
    text(canvas, 36, 721, 'Timed delivery showcase', 25, bold=True)
    text(canvas, 36, 695, 'Team __________   Kit __________   Date __________', 11)
    stroke(canvas, LINE)
    canvas.line(36, 681, 576, 681)

    text(canvas, 36, 658, 'Our tested setup', 13, TEAL, True)
    text(canvas, 36, 634, 'Saved project _____________________________   Tray or cradle ___________________', 11)
    text(canvas, 36, 607, 'Travel ______ wheel degrees     Speed ______ wheel degrees per second', 11)
    text(canvas, 36, 580, 'Week 7 evidence     Valid runs ____ / 3     Mean time (if 3/3) ____ s', 11)
    text(canvas, 36, 553, 'Our delivery job ____________________________________________________________', 11)

    text(canvas, 36, 514, 'Rehearse and record', 13, TEAL, True)
    para(canvas, 36, 491, 'Predict whether the loaded robot will cross the finish, keep its cube, stay in the lane '
         'and stop in the runout. A mentor times from first movement to the fixed chassis mark crossing FINISH.',
         535, 10.5, 14)
    text(canvas, 36, 449, 'Our prediction _____________________________________________________________', 11)
    canvas.setFillColor(HexColor(PALE))
    canvas.rect(36, 397, 540, 26, stroke=0, fill=1)
    for x, label in ((48, 'Run'), (196, 'Time (s) or DNF'), (314, 'Valid? Y/N'), (398, 'What happened?')):
        text(canvas, x, 406, label, 10, bold=True)
    stroke(canvas, LINE)
    for y, label in ((379, 'Rehearsal 1'), (348, 'Rehearsal 2'), (317, 'Rehearsal 3'), (286, 'Showcase')):
        text(canvas, 48, y, label, 11)
        canvas.line(36, y - 12, 576, y - 12)
    text(canvas, 36, 252, 'Record tenths of a second. DNF means the mark never crossed FINISH.', 10, MUTED)

    text(canvas, 36, 213, 'Give each teammate one speaking part', 13, TEAL, True)
    text(canvas, 36, 185, '__________ explains who the robot helps and what it delivers.', 11)
    text(canvas, 36, 158, '__________ explains one choice in the saved program.', 11)
    text(canvas, 36, 131, '__________ shows a build change and what the test showed.', 11)
    text(canvas, 36, 84, 'Our next test ______________________________________________________________', 11)
    text(canvas, 36, 28, 'MechaRAMS / Cheshire YMCA', 8, MUTED)
    canvas.showPage()


def make_page(path, label, draw):
    canvas = Canvas(str(path), pagesize=letter, invariant=1)
    canvas.setTitle(label)
    canvas.setAuthor('MechaRAMS / Cheshire YMCA')
    draw(canvas)
    canvas.save()


def build_packet():
    writer = PdfWriter()
    writer.add_metadata({'/Title': 'Week 8 Timed Delivery Showcase Class Print Packet',
                         '/Author': 'MechaRAMS / Cheshire YMCA'})
    writer.create_viewer_preferences()
    writer.viewer_preferences[NameObject('/PrintScaling')] = NameObject('/None')
    writer.viewer_preferences[NameObject('/Duplex')] = NameObject('/Simplex')
    for part, start, _ in indexed_sections(PLAN):
        pages = (part.first - 1, part.last)
        for _ in range(part.copies):
            writer.append(part.source, pages=pages, import_outline=False)
        writer.add_outline_item(part.label, start - 1)
    writer.write(PACKET)


if __name__ == '__main__':
    make_page(CHECKLIST, 'Week 8 Showcase Mentor Setup Checklist', checklist)
    make_page(TEAM_SHEET, 'Week 8 Timed Delivery Showcase Team Sheet', team_sheet)
    build_packet()
