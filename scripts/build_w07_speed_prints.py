"""Build the full-size timed delivery course, checklist, and one-print packet."""

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.units import cm
from reportlab.pdfgen.canvas import Canvas

from build_w04_w05_mission_prints import INK, LINE, MUTED, ORANGE, PALE, TEAL, para, stroke, text
from build_w04_w05_print_packets import PREP, PRINTS, Section, build_packet
from build_w04_w05_setup_checklists import (
    LEFT as CHECK_LEFT, checks, finish, item, make_pdf, section, title as check_title,
)
from build_w05_full_size_field import ruler, side_title

COURSE = PRINTS / 'W07_Speed_Trial_Full_Size_Course.pdf'
PACKET = 'W07_speed_trial_Class_Print_Packet.pdf'
CHECKLIST = PREP / 'W07_speed_trial_Checklist.pdf'
PAGE = landscape(letter)
TILE_W, TILE_H = 25, 20
ROWS = 'ABCDEFGH'
COURSE_W, COURSE_H = TILE_W * 2, TILE_H * len(ROWS)
START, TIMED_LENGTH = 10, 60
FINISH = START + TIMED_LENGTH
RUNOUT = COURSE_H - FINISH
LEFT = (PAGE[0] - TILE_W * cm) / 2
BOTTOM = (PAGE[1] - TILE_H * cm) / 2


def instructions(canvas):
    text(canvas, 36, 575, 'MECHARAMS / CHESHIRE YMCA / WEEK 7 TIMED DELIVERY', 9, TEAL, True)
    text(canvas, 36, 539, 'Assemble the full-size timed course', 28, bold=True)
    text(canvas, 36, 515, f'{COURSE_W} x {COURSE_H} cm / {TIMED_LENGTH} cm from START to FINISH', 11, MUTED)
    stroke(canvas, LINE)
    canvas.line(36, 499, 756, 499)
    steps = (
        ('1  Print and trim',
         'Print pages 2-17 on landscape US Letter at 100% or Actual Size. Check the 5 cm ruler. '
         'Trim all four edges of each tile along the dashed lines. Pencil the tile ID on its back before cutting.'),
        ('2  Join the rows',
         'Build eight rows from A at the near end to H at the far end. '
         'Put L to the left of R while facing the direction of travel. Butt the edges, '
         'match the paired ticks and tape from behind. Tape the finished course flat.'),
        ('3  Check the distance and stopping space',
         'Measure 60 cm from START (row A) to FINISH (row D). The printed runout extends 90 cm '
         'past FINISH. Leave clear floor at both ends. Extend the runout on the floor if the robot '
         'approaches the far edge in rehearsal.'),
        ('4  Set the start and time the crossing',
         'Align a fixed chassis mark with START and face FINISH. Time from first physical movement '
         'to the same mark crossing FINISH. Keep watching until the robot stops to judge cargo, '
         'lane and stopping success.'),
    )
    for (label, content), y in zip(steps, (468, 376, 282, 185)):
        text(canvas, 36, y, label, 13, TEAL, True)
        para(canvas, 36, y - 19, content, 476, 10.5, 14)

    x, base, scale = 574, 88, 2.12
    for row, value in enumerate(ROWS):
        for col, side in enumerate('LR'):
            left = x + col * TILE_W * scale
            bottom = base + row * TILE_H * scale
            stroke(canvas, TEAL, 0.8)
            canvas.setFillColor(HexColor(PALE))
            canvas.rect(left, bottom, TILE_W * scale, TILE_H * scale, stroke=1, fill=1)
            text(canvas, left + TILE_W * scale / 2, bottom + 30, f'{value}-{side}', 9, TEAL, True, True)
    for mark, name, color in ((START, 'START', TEAL), (FINISH, 'FINISH', ORANGE)):
        y = base + mark * scale
        stroke(canvas, color, 1.6)
        canvas.line(x, y, x + COURSE_W * scale, y)
        text(canvas, x + COURSE_W * scale + 9, y - 3, name, 8.5, color, True)
    text(canvas, x+53, 448, 'FAR END', 9, TEAL, True, True)
    text(canvas, x+53, 67, 'NEAR END', 9, MUTED, centered=True)
    ruler(canvas, 36, 52)
    canvas.showPage()


def alignment(canvas, row, column):
    stroke(canvas, INK, 0.75)
    canvas.setDash(5, 3)
    canvas.rect(LEFT, BOTTOM, TILE_W * cm, TILE_H * cm, stroke=1, fill=0)
    canvas.setDash()
    stroke(canvas, MUTED, 0.75)
    x = LEFT + TILE_W * cm if column == 0 else LEFT
    direction = -1 if column == 0 else 1
    for distance in (3, 3.25, 16, 16.25):
        y = BOTTOM + distance * cm
        canvas.line(x, y, x + direction * 0.45 * cm, y)

    top = BOTTOM + TILE_H * cm
    for y, direction, shared in ((BOTTOM, 1, row > 0), (top, -1, row < len(ROWS)-1)):
        if shared:
            for distance in (4, 4.25, 20, 20.25):
                x = LEFT + distance * cm
                canvas.line(x, y, x, y + direction * 0.45 * cm)


def timing_line(canvas, height, label, description, color):
    y = BOTTOM + height * cm
    stroke(canvas, color, 1.9)
    canvas.line(LEFT, y, LEFT + TILE_W * cm, y)
    text(canvas, LEFT + 18, y + 13, label, 22, color, True)
    text(canvas, LEFT + 18, y - 22, description, 10, MUTED)


def tile(canvas, row, col):
    label = f'{ROWS[row]}-{"LR"[col]}'
    side_title(canvas, f'WEEK 7 / TILE {label} / TRAVEL UP', 25, PAGE[1] / 2)
    side_title(canvas, 'TRIM ALL FOUR EDGES / ALIGN PAIRED TICKS', PAGE[0] - 27, PAGE[1] / 2)
    for height, name, description, color in (
        (START, 'START', 'Align the fixed chassis mark here.', TEAL),
        (FINISH, 'FINISH', 'Stop the stopwatch when the same mark crosses.', ORANGE),
    ):
        if row*TILE_H <= height < (row+1)*TILE_H:
            timing_line(canvas, height-row*TILE_H, name, description, color)
    if row == len(ROWS)-1:
        text(canvas, LEFT + 18, BOTTOM + 16*cm, 'RUNOUT END', 17, TEAL, True)
        text(canvas, LEFT + 18, BOTTOM + 16*cm-18, 'Keep clear floor beyond this edge.', 10, MUTED)
    alignment(canvas, row, col)
    canvas.showPage()


def make_course():
    canvas = Canvas(str(COURSE), pagesize=PAGE, invariant=1)
    canvas.setTitle('Week 7 Timed Delivery Full-Size Course')
    canvas.setAuthor('MechaRAMS / Cheshire YMCA')
    instructions(canvas)
    for row in range(len(ROWS)):
        for col in range(2):
            tile(canvas, row, col)
    canvas.save()


def checklist_page(canvas):
    check_title(canvas, 7, 'Timed delivery challenge')
    y = section(canvas, '1  Print for two courses', 663)
    y = item(canvas, y, 'Course sets: pages 2-17, two sets (32 sheets). Landscape Letter at Actual Size. '
             'Page 1 is the assembly guide.', COURSE.name)
    y = item(canvas, y, 'Five team sheets (four teams and a spare), four build cards and one attendance '
             'sheet. Class print total is 42 sheets before the guide and checklist.',
             'W07_speed_trial_Team_Sheet.pdf')
    y = section(canvas, '2  Set up the courses', y - 1)
    y = item(canvas, y, 'Check the 5 cm ruler. Trim and join rows A-H, L to the left of R. Match paired '
             'ticks, tape seams from behind and tape each 50 x 160 cm course flat.')
    y = item(canvas, y, 'Verify 60 cm between START and FINISH, with 90 cm of printed runout. '
             'Mark a fixed point on each chassis. Pack two stopwatches, two mentor trays and six cubes.')
    y = section(canvas, '3  Rehearse on both robots', y - 1)
    y = checks(canvas, y - 1, [
        'Load W07_speed_trial.py. Check A left, B right, hub pairing and Stop. Fit the loaded tray.',
        'Use speed 200. Start travel calibration at 180 wheel degrees. Increase in small steps to cross and stop inside the runout (limit 1440). Save the fixed travel value.',
        'Pass three loaded runs at 200. Trial 300 next, then optionally 400. Approve a higher setting only after three loaded passes at that setting.',
        'Practice timing from first movement to chassis mark crossing FINISH. Verify cargo, lane and stop.',
    ])
    for kit in ('A','B'):
        text(canvas, CHECK_LEFT, y, f'Kit {kit}', 10, TEAL, True)
        text(canvas, CHECK_LEFT+46, y, 'Travel degrees __________  Approved speeds __________  Initials ________', 10)
        y -= 15
    y = item(canvas, y, 'Alternate runs if staffing is limited. If one kit passes, share its lane at 200. '
             'If neither passes, hand-test cradles and walk through the timing cues.')
    finish(canvas, y-3, 'W07_speed_trial.pptx')


def make_checklist():
    make_pdf(CHECKLIST.name, 'Week 7 Timed Delivery Mentor Setup Checklist', checklist_page)


def print_plan():
    return (
        Section('Mentor checklist', CHECKLIST),
        Section('Course assembly guide', COURSE),
        Section('Kit A course tiles', COURSE, 2, 17),
        Section('Kit B course tiles', COURSE, 2, 17),
        Section('Team sheets (4 teams + spare)', PRINTS / 'W07_speed_trial_Team_Sheet.pdf', copies=5),
        Section('Build cards (one per team)', PRINTS / 'W07_speed_trial_Build_Card.pdf', copies=4),
        Section('Attendance', PRINTS / 'Attendance.pdf'),
    )


if __name__ == '__main__':
    make_course()
    make_checklist()
    build_packet(7, PACKET, 'Week 7 Timed Delivery Class Print Packet', plan=print_plan())
