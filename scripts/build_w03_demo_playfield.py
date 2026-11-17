"""Make the full-size Week 3 demo tiles and a separate pusher assembly picture."""

from math import atan2, cos, hypot, pi, sin
from pathlib import Path
from textwrap import wrap

import reportlab
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.pdfgen.canvas import Canvas

PRINTS = Path(__file__).resolve().parents[1] / '02_Student' / 'Printouts'
INK = '#142939'
TEAL = '#15665F'
ORANGE = '#9C4618'
GRAY = '#526572'
FILL = '#EDF5F3'
GRID = '#DEE6EA'
# Millimeters from the starting axle midpoint, with forward along +y.
ADVANCE = 110
START_REACH = 150
HOME_REACH = 270
START_RADIUS = 20
HOME_RADIUS = 32
POSES = ((0, 0, 0, 1), (0, ADVANCE, 1, 0), (ADVANCE, ADVANCE, 0, -1))
PIVOTS = ((0, ADVANCE), (ADVANCE, ADVANCE), (ADVANCE, 0))
TILES = (('A', -65, 50), ('B', 125, 50), ('C', -65, -200), ('D', 125, -200))
TILE_W, TILE_H = 200, 260
SEAM_X, SEAM_Y = 130, 55
RECIPE = (
    'async def student_recipe():',
    '    C_MM = 176      # replace with measured wheel circumference',
    '    FACE_MM = 100   # replace with axle-to-pusher distance',
    '    TURN_90 = 161   # tune until the robot pivots 90 degrees right',
    f'    push_mm = {HOME_REACH - START_RADIUS} - FACE_MM',
    '    push_deg = round(push_mm * 360 / C_MM)',
    f'    back_deg = round((push_mm - {ADVANCE}) * 360 / C_MM)',
    '    for beat in range(3):',
    '        await drive(push_deg)',
    '        await motor_pair.move_for_degrees(PAIR, -back_deg, 0, velocity=SPEED)',
    '        await turn(TURN_90)',
    '    await signal("D")',
)


def text(canvas, x, y, value, size=10, color=INK, bold=False, centered=False):
    canvas.setFillColor(HexColor(color))
    canvas.setFont('Helvetica-Bold' if bold else 'Helvetica', size)
    draw = canvas.drawCentredString if centered else canvas.drawString
    draw(x, y, value)


def lines(canvas, x, y, value, width=91, size=10, leading=14):
    for line in wrap(value, width):
        text(canvas, x, y, line, size)
        y -= leading
    return y


def setup_page(canvas):
    text(canvas, 37, 752, 'MECHARAMS  /  WEEK 3 DEMO CHALLENGE', 9, TEAL, bold=True)
    text(canvas, 37, 720, 'Three cones, three homes', 29, bold=True)
    text(canvas, 37, 699, 'Push each cone straight into its matching home, back away, and turn right.', 11)
    canvas.setStrokeColor(HexColor(GRID))
    canvas.line(37, 680, 575, 680)

    text(canvas, 37, 658, '1  Print and join the field', 13, TEAL, bold=True)
    lines(canvas, 37, 639, 'Print pages 2-5 on US Letter at Actual Size (100%). '
          'The distance between adjacent grid lines must be 1 cm.', 68)
    lines(canvas, 37, 605, 'Lay out A and B above C and D with all letters upright. '
          'Cut along the dashed TRIM lines. Butt the cut edges, match the grid and the double ticks, '
          'then tape the seams from the back.', 68)
    lines(canvas, 37, 551, 'Tape the outer edges flat on a smooth floor. The marked '
          'field is 39 x 51 cm. Leave space around it for the robot to turn.', 68)
    for i, (label, _, _) in enumerate(TILES):
        x, y = 455 + (i % 2) * 55, 606 - (i // 2) * 49
        canvas.setStrokeColor(HexColor(TEAL))
        canvas.setFillColor(HexColor(FILL))
        canvas.rect(x, y, 55, 49, stroke=1, fill=1)
        text(canvas, x + 27.5, y + 19, label, 14, TEAL, bold=True, centered=True)

    text(canvas, 37, 504, '2  Set up and score', 13, TEAL, bold=True)
    lines(canvas, 37, 484, 'Center the drive axle over START and face the arrow. Put the three 4 cm cones on the '
          'dashed START circles, centered on their crosses. Keep the solid HOME circles empty.', 100)
    lines(canvas, 37, 448, 'Score 1 point per upright cone with its entire base inside its own HOME circle after '
          'the final turn. All three homes filled is 3/3. Rehearse with one cone before loading all three.', 100)

    text(canvas, 37, 399, '3  Set the demo program', 13, TEAL, bold=True)
    lines(canvas, 37, 379, 'In a copy of the full W03_dance.py project, replace student_recipe with the code below. '
          'It uses the helpers and motor settings already in the file.', 101)
    canvas.setFillColor(HexColor(FILL))
    canvas.roundRect(37, 158, 538, 187, 5, stroke=0, fill=1)
    canvas.setFillColor(HexColor(INK))
    canvas.setFont('Courier', 9)
    for i, line in enumerate(RECIPE):
        canvas.drawString(48, 328 - 14 * i, line)

    text(canvas, 37, 136, 'Calibrate for the actual robot and floor', 11, TEAL, bold=True)
    lines(canvas, 37, 119, 'Measure wheel circumference and the distance from the drive axle midpoint to the '
          'front face of the pusher (in mm). Aim for a pusher face about 100 mm ahead of the axle.', 100)
    lines(canvas, 37, 83, 'Dry-run with the pusher fitted. Tune TURN_90 so the robot faces east at P1 and south '
          'at P2. After each reverse, the axle midpoint should reach the marked pivot. Verify the '
          'robot clears the waiting cones during turns before running all three.', 100)
    text(canvas, 37, 26, 'FIELD MAP AND PROGRAM STARTING VALUES  /  CHECK ON THE DEMO FLOOR', 8, GRAY)
    canvas.showPage()


def draw_field(canvas):
    """Draw a single metric field. Each page clips a different window into it."""
    canvas.setStrokeColor(HexColor(GRID))
    canvas.setLineWidth(0.35)
    for x in range(-60, 321, 10):
        canvas.line(x * mm, -200 * mm, x * mm, 310 * mm)
    for y in range(-200, 311, 10):
        canvas.line(-65 * mm, y * mm, 325 * mm, y * mm)
    canvas.rect(-65 * mm, -200 * mm, 390 * mm, 510 * mm, stroke=1, fill=0)

    canvas.setStrokeColor(HexColor(GRAY))
    canvas.setLineWidth(0.8)
    canvas.setDash(3, 3)
    for x, y, dx, dy in POSES:
        canvas.line(x * mm, y * mm, (x + dx * HOME_REACH) * mm, (y + dy * HOME_REACH) * mm)
    canvas.setDash()
    canvas.setFillColor(HexColor(INK))
    canvas.setStrokeColor(HexColor(INK))
    canvas.setLineWidth(1.25)
    canvas.line(-60 * mm, 0, 60 * mm, 0)
    canvas.line(0, 0, 0, 21 * mm)
    canvas.lines(((0, 21 * mm, -3 * mm, 16 * mm), (0, 21 * mm, 3 * mm, 16 * mm)))
    text(canvas, -34 * mm, -7 * mm, 'START / axle midpoint', 10, bold=True)
    for number, (x, y) in enumerate(PIVOTS, start=1):
        canvas.setFillColor(HexColor('#FFFFFF'))
        canvas.setStrokeColor(HexColor(GRAY))
        canvas.circle(x * mm, y * mm, 3 * mm, fill=1, stroke=1)
        text(canvas, (x + 5) * mm, (y + 4) * mm, f'P{number}', 9, GRAY, bold=True)

    for i, (x, y, dx, dy) in enumerate(POSES, start=1):
        for reach, radius, name, color in (
            (START_REACH, START_RADIUS, 'CONE', ORANGE),
            (HOME_REACH, HOME_RADIUS, 'HOME', TEAL),
        ):
            cx, cy = (x + dx * reach) * mm, (y + dy * reach) * mm
            canvas.setStrokeColor(HexColor(color))
            canvas.setFillColor(HexColor('#FFFFFF' if name == 'CONE' else FILL))
            canvas.setDash(4, 3) if name == 'CONE' else canvas.setDash()
            canvas.setLineWidth(1.3)
            canvas.circle(cx, cy, radius * mm, fill=1, stroke=1)
            canvas.setDash()
            canvas.line(cx - 3 * mm, cy, cx + 3 * mm, cy)
            canvas.line(cx, cy - 3 * mm, cx, cy + 3 * mm)
            text(canvas, cx, cy + 6 * mm, f'{name} {i}', 12, color, bold=True, centered=True)
            if name == 'CONE':
                text(canvas, cx, cy - 9 * mm, 'START', 8, color, centered=True)


def trim_lines(canvas, left, bottom):
    canvas.setStrokeColor(HexColor(INK))
    canvas.setLineWidth(0.8)
    canvas.setDash(6, 3)
    canvas.line(SEAM_X * mm, bottom * mm, SEAM_X * mm, (bottom + TILE_H) * mm)
    canvas.line(left * mm, SEAM_Y * mm, (left + TILE_W) * mm, SEAM_Y * mm)
    canvas.setDash()
    vertical_marks = (170, 260) if bottom > 0 else (-195, 19)
    horizontal_marks = (-45, 91) if left < 0 else (164, 280)
    for y in vertical_marks:
        for delta in (0, 2):
            canvas.line((SEAM_X - 4) * mm, (y + delta) * mm, (SEAM_X + 4) * mm, (y + delta) * mm)
    for x in horizontal_marks:
        for delta in (0, 2):
            canvas.line((x + delta) * mm, (SEAM_Y - 4) * mm, (x + delta) * mm, (SEAM_Y + 4) * mm)
    trim_x = SEAM_X + 3.5 if left < 0 else SEAM_X - 1.5
    trim_y = SEAM_Y - 4 if bottom > 0 else SEAM_Y + 2
    canvas.saveState()
    canvas.translate(trim_x * mm, (bottom + TILE_H - 17) * mm)
    canvas.rotate(90)
    text(canvas, 0, 0, 'TRIM', 6, bold=True)
    canvas.restoreState()
    text(canvas, (left + TILE_W / 2 - 4) * mm, trim_y * mm, 'TRIM', 6, bold=True)


def field_tile(canvas, label, left, bottom):
    margin_x = (letter[0] - TILE_W * mm) / 2
    margin_y = (letter[1] - TILE_H * mm) / 2
    canvas.saveState()
    bounds = canvas.beginPath()
    bounds.rect(margin_x, margin_y, TILE_W * mm, TILE_H * mm)
    canvas.clipPath(bounds, stroke=0, fill=0)
    canvas.translate(margin_x - left * mm, margin_y - bottom * mm)
    draw_field(canvas)
    trim_lines(canvas, left, bottom)
    canvas.restoreState()

    row = 'TOP' if bottom > 0 else 'BOTTOM'
    column = 'LEFT' if left < 0 else 'RIGHT'
    # Keep the ID inside the printer margins and beyond either trim line.
    y = margin_y + (TILE_H - 7 if bottom > 0 else 4) * mm
    text(canvas, margin_x + 9 * mm, y, f'TILE {label} / {row} {column}', 10, bold=True)
    text(canvas, margin_x + 88 * mm, y, 'US LETTER  /  ACTUAL SIZE  /  1 CM GRID', 8, GRAY)
    canvas.showPage()


def make_pdf():
    canvas = Canvas(str(PRINTS / 'W03_Three_Cone_Demo_Playfield.pdf'), pagesize=letter, invariant=1)
    canvas.setTitle('Week 3 Three-Cone Demo Playfield')
    canvas.setAuthor('MechaRAMS / Cheshire YMCA')
    setup_page(canvas)
    for tile in TILES:
        field_tile(canvas, *tile)
    canvas.save()


def make_picture():
    picture = Image.new('RGB', (1600, 1100), '#FFFFFF')
    art = ImageDraw.Draw(picture)
    font_dir = Path(reportlab.__file__).parent / 'fonts'

    def label(x, y, value, size=29, color=INK, bold=False, anchor='la'):
        font = ImageFont.truetype(str(font_dir / ('VeraBd.ttf' if bold else 'Vera.ttf')), size)
        art.text((x, y), value, font=font, fill=color, anchor=anchor)

    def arrow(start, end, color=GRAY, width=4):
        art.line([start, end], fill=color, width=width)
        angle = atan2(end[1] - start[1], end[0] - start[0])
        corners = [
            (end[0] - 14 * cos(angle + offset), end[1] - 14 * sin(angle + offset))
            for offset in (-pi / 5, pi / 5)
        ]
        art.polygon([end, *corners], fill=color)

    def beam(box, holes, fill, edge):
        art.rounded_rectangle(box, radius=21, fill=fill, outline=edge, width=4)
        for x, y in holes:
            art.ellipse((x - 10, y - 10, x + 10, y + 10), fill='#FFFFFF', outline=edge, width=3)

    def pin(x, y):
        art.ellipse((x - 10, y - 10, x + 10, y + 10), fill=INK)
        art.line((x - 5, y + 4, x + 5, y - 4), fill='#FFFFFF', width=2)

    label(54, 39, 'MECHARAMS  /  WEEK 3 DEMO CHALLENGE', 22, TEAL, True)
    label(54, 78, 'Build the centered cone pusher', 53, INK, True)
    label(54, 151, 'Two Technic arms, one straight liftarm and friction pins', 27, GRAY)
    art.line((54, 217, 1546, 217), fill=GRID, width=3)
    label(56, 244, 'TOP VIEW', 25, TEAL, True)

    # Chassis in gray. Arms continue the two rails toward the cone.
    art.rounded_rectangle((267, 590, 767, 968), radius=35, fill='#EEF1F3', outline='#9FAEB6', width=4)
    for x in (226, 758):
        art.rounded_rectangle((x, 741, x + 49, 885), radius=19, fill='#556772')
    for x in (385, 649):
        beam((x - 28, 582, x + 28, 864), [(x, y) for y in range(608, 849, 40)], '#CBD5DA', GRAY)
    label(517, 893, 'SPIKE driving base', 28, GRAY, False, 'ma')

    for x in (385, 649):
        beam((x - 27, 417, x + 27, 677), [(x, y) for y in range(448, 650, 40)], '#CAE8E0', TEAL)
        pin(x, 608)
        pin(x, 648)
    beam((261, 419, 773, 475), [(x, 448) for x in range(286, 749, 33)], '#9FD4C9', TEAL)
    for x in (385, 649):
        pin(x, 448)

    art.ellipse((443, 267, 591, 415), fill='#FFF3E8', outline=ORANGE, width=4)
    art.line((491, 341, 543, 341), fill=ORANGE, width=3)
    art.line((517, 315, 517, 367), fill=ORANGE, width=3)
    art.line((517, 415, 517, 419), fill=ORANGE, width=2)
    label(609, 317, 'Cone on', 26, ORANGE, True)
    label(609, 353, 'centerline', 26, ORANGE, True)
    arrow((194, 510), (378, 488), TEAL)
    label(57, 519, 'Short arm', 26, TEAL, True)
    arrow((180, 687), (372, 651), GRAY)
    label(57, 695, 'Friction pins', 24, GRAY, True)
    arrow((800, 418), (767, 432), TEAL)
    label(795, 374, 'Straight beam', 25, TEAL, True)
    label(795, 449, 'Both ends open', 22, GRAY)

    # Side view shows floor clearance and the low contact area.
    label(1019, 244, 'SIDE VIEW', 25, TEAL, True)
    label(1238, 318, 'About 100 mm axle to beam face', 20, GRAY, False, 'ma')
    arrow((1238, 362), (1115, 362))
    arrow((1238, 362), (1360, 362))
    art.line((1115, 362, 1115, 475), fill=GRID, width=3)
    art.line((1360, 362, 1360, 509), fill=GRID, width=3)
    art.line((1009, 563, 1548, 563), fill=GRAY, width=4)
    art.rounded_rectangle((1045, 410, 1220, 513), radius=18, fill='#EEF1F3', outline='#9FAEB6', width=4)
    art.ellipse((1073, 479, 1156, 562), fill='#556772', outline=INK, width=3)
    art.ellipse((1097, 503, 1132, 538), fill='#DCE4E8')
    art.line((1190, 453, 1328, 453, 1328, 514), fill=TEAL, width=18, joint='curve')
    art.rounded_rectangle((1308, 513, 1361, 547), radius=8, fill='#9FD4C9', outline=TEAL, width=4)
    art.polygon([(1358, 562), (1414, 403), (1470, 562)], fill='#FFF3E8', outline=ORANGE, width=3)
    arrow((1450, 612), (1364, 541), GRAY)
    label(1148, 613, 'Leave a few mm', 24, GRAY, True)
    label(1148, 645, 'of floor clearance', 24, GRAY, True)

    for i, (heading, details) in enumerate((
        ('1  Mount the arms', ('Pin the arms to two existing front mounts.', 'Use two pin holes per side where available.')),
        ('2  Add the crossbar', ('Pin one straight beam across the two arms.', 'Use a beam long enough to reach both.')),
        ('3  Set the height', ('Use matching drop links if needed.', 'Check that the beam meets the cone low.')),
    )):
        y = 713 + i * 106
        label(1019, y, heading, 23, TEAL, True)
        for j, detail in enumerate(details):
            label(1019, y + 34 + 28 * j, detail, 19)
    art.line((54, 1042, 1546, 1042), fill=GRID, width=3)
    label(54, 1058, 'Assembly schematic  /  Match the mounting holes and height on your own robot.', 20, GRAY)
    picture.save(PRINTS / 'W03_Centered_LEGO_Pusher.png')


if __name__ == '__main__':
    make_pdf()
    make_picture()
