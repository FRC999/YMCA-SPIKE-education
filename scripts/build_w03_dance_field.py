"""Build the three-cone field for the original Week 3 drive-and-turn recipe."""

from math import cos, sin
from pathlib import Path
from textwrap import wrap

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.units import mm
from reportlab.pdfgen.canvas import Canvas

OUTPUT = (Path(__file__).resolve().parents[1] /
          '02_Student/Printouts/W03_Dance_Three_Cone_Field.pdf')
NAVY = '#142939'
TEAL = '#15665F'
ORANGE = '#9C4618'
GRAY = '#526572'
LIGHT = '#EDF5F3'
LINE = '#B8C6CD'
WHITE = '#FFFFFF'

# All coordinates are millimeters. Rehearsal on the actual floor sets the final marks.
WHEEL_CIRCUMFERENCE = 176
WHEEL_TRACK = 120
DRIVE_MM = WHEEL_CIRCUMFERENCE / 4
TURN_RAD = 2 * DRIVE_MM / WHEEL_TRACK
TIP_REACH = 100
CONE_RADIUS = 20
FIRST_GAP = 6
HOME_RADIUS = 30
AXLE_START = (38, 11)


def text(canvas, x, y, value, size=10, color=NAVY, bold=False, centered=False):
    canvas.setFillColor(HexColor(color))
    canvas.setFont('Helvetica-Bold' if bold else 'Helvetica', size)
    draw = canvas.drawCentredString if centered else canvas.drawString
    draw(x * mm, y * mm, value)


def paragraph(canvas, x, y, value, width, size=10):
    for line in wrap(value, width):
        text(canvas, x, y, line, size)
        y -= 4.6
    return y


def stroke(canvas, color, width=1):
    canvas.setStrokeColor(HexColor(color))
    canvas.setLineWidth(width)


def line(canvas, x1, y1, x2, y2):
    canvas.line(x1 * mm, y1 * mm, x2 * mm, y2 * mm)


def cross(canvas, x, y, size=2):
    line(canvas, x - size, y, x + size, y)
    line(canvas, x, y - size, x, y + size)


def circle(canvas, x, y, radius, fill=None):
    if fill:
        canvas.setFillColor(HexColor(fill))
    canvas.circle(x * mm, y * mm, radius * mm, stroke=1, fill=bool(fill))


def home(canvas, x, y, number):
    stroke(canvas, TEAL, 1.35)
    circle(canvas, x, y, HOME_RADIUS, LIGHT)
    cross(canvas, x, y)
    text(canvas, x, y + 10, f'HOME {number}', 14, TEAL, True, True)
    text(canvas, x, y - 12, 'Entire base inside', 8, TEAL, centered=True)


def start_cone(canvas, x, y, number, radius=CONE_RADIUS):
    stroke(canvas, ORANGE, 1.15)
    canvas.setDash(4, 3)
    circle(canvas, x, y, radius)
    canvas.setDash()
    cross(canvas, x, y)
    text(canvas, x, y - (9 if radius == CONE_RADIUS else 5),
         f'CONE {number}', 10 if radius == CONE_RADIUS else 7, ORANGE, True, True)


def geometry():
    fields = []
    axle_x, axle_y = AXLE_START
    for beat in range(3):
        dx, dy = sin(beat * TURN_RAD), cos(beat * TURN_RAD)
        start_dist = TIP_REACH + CONE_RADIUS + FIRST_GAP
        goal_dist = TIP_REACH + DRIVE_MM + CONE_RADIUS
        cone = (axle_x + dx * start_dist, axle_y + dy * start_dist)
        goal = (axle_x + dx * goal_dist, axle_y + dy * goal_dist)
        previous_pose = (axle_x, axle_y)
        axle_x += dx * DRIVE_MM
        axle_y += dy * DRIVE_MM
        fields.append((previous_pose, (axle_x, axle_y), cone, goal))
    return fields


def playfield(canvas):
    fields = geometry()
    for number, (_, _, _, goal) in enumerate(fields, 1):
        home(canvas, *goal, number)
    for number, (axle, pivot, cone, _) in enumerate(fields, 1):
        stroke(canvas, GRAY, 0.85)
        line(canvas, *axle, *pivot)
        stroke(canvas, LINE, 0.65)
        canvas.setDash(2, 3)
        line(canvas, *pivot, *cone)
        canvas.setDash()
        stroke(canvas, GRAY, 0.8)
        circle(canvas, *pivot, 2.1, WHITE)
        text(canvas, pivot[0] - 8, pivot[1] + 3, f'P{number}', 8, GRAY, True)
        start_cone(canvas, *cone, number)

    x, y = AXLE_START
    stroke(canvas, NAVY, 1.3)
    line(canvas, x - 23, y, x + 23, y)
    line(canvas, x, y, x, y + 19)
    line(canvas, x, y + 19, x - 3, y + 14)
    line(canvas, x, y + 19, x + 3, y + 14)
    text(canvas, 64, 9, 'START / axle midpoint', 10, bold=True)
    text(canvas, 53, 40, 'P1-P3 mark the axle at each turn.', 9, GRAY)

    text(canvas, 185, 201, 'Week 3 cone homes', 19, bold=True)
    text(canvas, 185, 192, 'US Letter landscape / print at 100%', 10, GRAY)
    text(canvas, 185, 183, 'drive(90), turn(90) x 3, then D', 10, TEAL, True)
    stroke(canvas, NAVY, 0.9)
    line(canvas, 187, 164, 237, 164)
    for x in (187, 237):
        line(canvas, x, 162, x, 166)
    text(canvas, 212, 168, 'This line must measure 5 cm', 8, centered=True)

    text(canvas, 130, 59, 'Set the cone bases on the dashed circles', 11, TEAL, True)
    paragraph(canvas, 130, 52, 'Match cone numbers to homes. Tape the sheet flat and leave '
              'clear floor around it. Use the rounded pusher tip shown on page 2.', 74)
    text(canvas, 130, 36, 'Starter layout: 44 mm drives, about 42-degree right pivots,', 9, GRAY)
    text(canvas, 130, 31, 'and a 100 mm axle-to-tip reach. Use page 2 to fit your robot.', 9, GRAY)
    text(canvas, 130, 19, 'Score 1 point per upright cone entirely in its home after', 10, bold=True)
    text(canvas, 130, 14, 'the final turn. A clear run scores 3/3.', 10, bold=True)
    canvas.showPage()


def pusher_sketch(canvas):
    text(canvas, 187, 104, 'Centered pusher tip / top view', 12, TEAL, True)
    stroke(canvas, GRAY, 0.9)
    canvas.setFillColor(HexColor(LIGHT))
    canvas.roundRect(198 * mm, 52 * mm, 50 * mm, 16 * mm, 2 * mm, stroke=1, fill=1)
    line(canvas, 202, 63, 202, 71)
    line(canvas, 244, 63, 244, 71)
    stroke(canvas, TEAL, 2.1)
    line(canvas, 195, 71, 251, 71)
    line(canvas, 223, 71, 223, 82)
    circle(canvas, 223, 83.5, 2.4, LIGHT)
    stroke(canvas, ORANGE, 0.9)
    circle(canvas, 223, 91, 4.3)
    stroke(canvas, GRAY, 0.7)
    line(canvas, 226, 83.5, 234, 83.5)
    text(canvas, 236, 82.5, 'Round tip', 8)
    text(canvas, 223, 58, 'Driving base', 9, centered=True)
    paragraph(canvas, 187, 43, 'Pin a short arm to the middle of the beam. Fit a smooth round '
              'Technic connector on a vertical axle at its tip, a few mm above the floor.', 52, 9)
    paragraph(canvas, 187, 23, 'Start with the tip about 25 mm ahead of the beam. '
              'Check that the beam swings clear of the cone on the turn.', 51, 9)


def setup(canvas):
    text(canvas, 12, 199, 'Fit the field to your robot', 24, bold=True)
    text(canvas, 12, 189, 'Optional cutouts / print this page at 100% if the starter marks need to move.',
         11, GRAY)
    for number, x in enumerate((48, 136, 224), 1):
        home(canvas, x, 151, number)
        start_cone(canvas, x + 39, 151, number, 8)

    text(canvas, 12, 104, 'Rehearse with the class program', 12, TEAL, True)
    paragraph(canvas, 12, 96, '1. Tape a repeatable axle start and heading. Run the full Week 3 '
              'program with no cones. Use video from above to see where the tip points at the start '
              'and immediately after turns 1 and 2.', 87)
    paragraph(canvas, 12, 76, '2. Put each cone directly ahead of the tip at its own start, with '
              'about 6 mm between the tip and the nearest base edge. Try one cone per full run. '
              'Check that it stays upright in place as the pusher turns away.', 87)
    paragraph(canvas, 12, 56, '3. If needed, use the cutouts to mark the corrected starts and center '
              'each home on its cone\'s resting spot. Tape the cutouts flat or trace them with '
              'painter\'s tape. Leave the marks fixed and run all three cones together.', 87)
    text(canvas, 12, 29, 'Keep SPEED = 200 and the three original drive/turn repeats.', 10, bold=True)
    text(canvas, 12, 20, 'Each 90 is in wheel degrees. Let the robot show you the heading.', 10, GRAY)
    pusher_sketch(canvas)
    canvas.showPage()


if __name__ == '__main__':
    pdf = Canvas(str(OUTPUT), pagesize=landscape(letter), invariant=1)
    pdf.setTitle('Week 3 Three Cone Field - Original Dance Program')
    pdf.setAuthor('MechaRAMS / Cheshire YMCA')
    playfield(pdf)
    setup(pdf)
    pdf.save()
