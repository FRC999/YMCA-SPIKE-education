"""Build the cone rematch and sensor mission printouts."""

import ast
from math import cos, sin
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.lib.utils import simpleSplit
from reportlab.pdfgen.canvas import Canvas

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / '02_Student/Printouts'
INK = '#142939'
TEAL = '#15665F'
ORANGE = '#9C4618'
MUTED = '#4B626E'
LINE = '#C5D1D7'
PALE = '#EAF4F1'
WHITE = '#FFFFFF'
AXLE_START = (15, 10)
FIELD_SIZE = 60
WHEEL_CIRCUMFERENCE = 17.6
WHEEL_TRACK = 12
TIP_REACH = 10
CONE_RADIUS = 2
NOSE_GAP = 3
HOME_RADIUS = 4


def text(canvas, x, y, value, size=11, color=INK, bold=False, centered=False):
    canvas.setFillColor(HexColor(color))
    canvas.setFont('Helvetica-Bold' if bold else 'Helvetica', size)
    draw = canvas.drawCentredString if centered else canvas.drawString
    draw(x, y, value)


def para(canvas, x, y, value, width=538, size=11, leading=15):
    for part in simpleSplit(value, 'Helvetica', size, width):
        text(canvas, x, y, part, size)
        y -= leading
    return y


def stroke(canvas, color, width=1):
    canvas.setStrokeColor(HexColor(color))
    canvas.setLineWidth(width)


def area(canvas, x, y, w, h, color=PALE):
    canvas.setFillColor(HexColor(color))
    canvas.roundRect(x, y, w, h, 6, stroke=0, fill=1)


def heading(canvas, week, title, subtitle):
    text(canvas, 36, 753, f'MECHARAMS / CHESHIRE YMCA / WEEK {week}', 9, TEAL, True)
    text(canvas, 36, 715, title, 30, bold=True)
    text(canvas, 36, 692, subtitle, 11, MUTED)
    stroke(canvas, LINE)
    canvas.line(36, 676, 576, 676)


def footer(canvas, label):
    stroke(canvas, LINE)
    canvas.line(36, 44, 576, 44)
    text(canvas, 36, 27, label, 8, MUTED)
    canvas.showPage()


def cross(canvas, x, y, color):
    stroke(canvas, color)
    canvas.lines([(x - 5, y, x + 5, y), (x, y - 5, x, y + 5)])


def circle(canvas, x, y, radius, color, dashed=False, fill=WHITE):
    stroke(canvas, color, 1.3)
    canvas.setFillColor(HexColor(fill))
    if dashed:
        canvas.setDash(4, 3)
    canvas.circle(x, y, radius, stroke=1, fill=1)
    canvas.setDash()


def starter_route():
    tree = ast.parse((ROOT / '04_Python/W04_cone_rematch.py').read_text(encoding='utf-8'))
    recipe = next(node for node in tree.body
                  if isinstance(node, ast.AsyncFunctionDef) and node.name == 'student_recipe')
    return ast.literal_eval(recipe.body[0].value)


def field_geometry():
    """Example axle, cone and home centers, in cm from the bottom-left corner."""
    axle = AXLE_START
    heading_rad = 0
    field = []
    for forward, turn in starter_route():
        travel = forward / 360 * WHEEL_CIRCUMFERENCE
        dx, dy = sin(heading_rad), cos(heading_rad)
        cone_reach = TIP_REACH + CONE_RADIUS + NOSE_GAP
        home_reach = travel + TIP_REACH + CONE_RADIUS
        next_axle = (axle[0] + dx * travel, axle[1] + dy * travel)
        cone = (axle[0] + dx * cone_reach, axle[1] + dy * cone_reach)
        home = (axle[0] + dx * home_reach, axle[1] + dy * home_reach)
        field.append((axle, next_axle, cone, home))
        axle = next_axle
        heading_rad += 2 * (turn / 360 * WHEEL_CIRCUMFERENCE) / WHEEL_TRACK
    return field


def field_map(canvas):
    heading(canvas, 4, 'Cone challenge rematch', 'Tape a 60 x 60 cm field and leave clear floor around it.')
    field = field_geometry()
    base_x, base_y, scale = 36, 286, 6

    def point(pair):
        return base_x + pair[0] * scale, base_y + pair[1] * scale

    stroke(canvas, LINE, 0.5)
    for i in range(0, FIELD_SIZE + 1, 10):
        canvas.line(*point((i, 0)), *point((i, FIELD_SIZE)))
        canvas.line(*point((0, i)), *point((FIELD_SIZE, i)))
    for axle, pivot, _, home in field:
        stroke(canvas, INK, 1.25)
        canvas.line(*point(axle), *point(pivot))
        stroke(canvas, MUTED, 0.75)
        canvas.setDash(3, 3)
        canvas.line(*point(pivot), *point(home))
        canvas.setDash()
    for i, (_, _, cone, home) in enumerate(field, 1):
        x, y = point(home)
        circle(canvas, x, y, HOME_RADIUS * scale, TEAL, fill=PALE)
        text(canvas, x, y - 4, f'H{i}', 11, TEAL, True, True)
        x, y = point(cone)
        circle(canvas, x, y, CONE_RADIUS * scale, ORANGE, dashed=True)
        text(canvas, x, y - 4, f'C{i}', 9, ORANGE, True, True)
    x, y = point(AXLE_START)
    stroke(canvas, INK, 1.3)
    canvas.lines([(x - 13, y, x + 13, y), (x, y, x, y + 24),
                  (x - 4, y + 18, x, y + 24), (x + 4, y + 18, x, y + 24)])
    text(canvas, x + 18, y - 4, 'START', 9, bold=True)
    text(canvas, base_x, 268, '(0, 0) lower-left corner', 9, MUTED)
    text(canvas, 418, 637, 'Set the floor', 13, TEAL, True)
    para(canvas, 418, 617, 'Measure right and up from the lower-left corner. All positions below are circle centers.', 154)
    text(canvas, 418, 548, 'Place the robot', 13, TEAL, True)
    para(canvas, 418, 528, 'Center its drive axle at START. Point it toward the top edge.', 154)
    text(canvas, 418, 468, 'Aim toward Cone 2', 13, TEAL, True)
    para(canvas, 418, 448, 'The second leg crosses the field diagonally. Turn until the pusher faces the cone head-on.', 154)
    text(canvas, 418, 371, 'Check both kits', 13, TEAL, True)
    para(canvas, 418, 351, 'Dry-run the starter recipe on the floor. Adjust the marks or the baseline for each robot before class.', 154)
    text(canvas, 36, 239, 'Mark the centers in centimeters', 13, TEAL, True)
    text(canvas, 36, 220, 'START / axle center  (15.0, 10.0)', 11, bold=True)
    for i, (_, _, cone, home) in enumerate(field, 1):
        y = 195 - (i - 1) * 24
        text(canvas, 36, y, f'C{i}   ({cone[0]:.1f}, {cone[1]:.1f})', 11, ORANGE, True)
        text(canvas, 280, y, f'H{i}   ({home[0]:.1f}, {home[1]:.1f})', 11, TEAL, True)
    para(canvas, 36, 112, 'Dashed circles are 4 cm cone starts. Solid circles are 8 cm homes. '
         'Use the cutouts on page 3 or mark the circles with tape. Start with Cone 1 only.', size=11)
    footer(canvas, 'WEEK 4 / MENTOR FIELD MAP / SCALE DRAWING, 10 CM GRID')


def rematch_card(canvas):
    heading(canvas, 4, 'Can you get the cone home?', 'Team __________________   Robot ________')
    text(canvas, 36, 644, '1  Try one cone', 14, TEAL, True)
    para(canvas, 36, 623, 'Set Cone 1 on its dashed circle. Run the starter program. Watch the first '
         'push and the turn. One point if the cone finishes upright with all of its base inside Home 1.')
    text(canvas, 36, 562, '2  Find the first thing to change', 14, TEAL, True)
    area(canvas, 36, 449, 540, 94)
    text(canvas, 50, 520, 'What you saw', 10, TEAL, True)
    text(canvas, 303, 520, 'One change to try', 10, TEAL, True)
    for y, seen, change in (
        (499, 'Robot stopped short or went too far', 'Change the drive number for that leg.'),
        (480, 'Robot pointed past the next cone', 'Change the turn number in the previous row.'),
        (461, 'Cone tipped or followed the robot', 'Hand-test a lower tip or more beam clearance.'),
    ):
        text(canvas, 50, y, seen, 10)
        text(canvas, 303, y, change, 10)
    text(canvas, 36, 420, '3  Run again from the same start', 14, TEAL, True)
    para(canvas, 36, 399, 'Predict what your change will do. Keep the other settings and the cone marks '
         'fixed. After one cone works, add Cone 2 for the diagonal leg. Add Cone 3 when ready.')
    for y, prompt in (
        (343, 'First run / What happened?'),
        (270, 'We changed one thing / What did we expect?'),
        (197, 'Retest / What did the robot and cone actually do?'),
    ):
        text(canvas, 36, y, prompt, 11, bold=True)
        stroke(canvas, LINE)
        canvas.line(36, y - 31, 576, y - 31)
    text(canvas, 36, 126, 'Cones in their homes ______ / ______ placed', 11, bold=True)
    text(canvas, 36, 85, 'Driver runs the code. Navigator resets the field. Observer records the result. Rotate.', 10, MUTED)
    footer(canvas, 'WEEK 4 / TEAM CARD')


def floor_markers(canvas):
    heading(canvas, 4, 'Cut out the starts and homes', 'Print this page at Actual Size (100%) on US Letter.')
    rows = [(1, 156, 526), (2, 438, 526), (3, 156, 260)]
    for i, x, y in rows:
        circle(canvas, x, y, HOME_RADIUS * cm, TEAL, fill=PALE)
        cross(canvas, x, y, TEAL)
        text(canvas, x, y + 33, f'HOME {i}', 19, TEAL, True, True)
        text(canvas, x, y - 37, 'Entire base inside', 11, TEAL, centered=True)
    for i, (x, y) in enumerate(((354, 305), (501, 305), (428, 172)), 1):
        circle(canvas, x, y, CONE_RADIUS * cm, ORANGE, dashed=True)
        cross(canvas, x, y, ORANGE)
        text(canvas, x, y - 23, f'CONE {i}', 12, ORANGE, True, True)
    stroke(canvas, INK)
    canvas.line(36, 80, 36 + 5 * cm, 80)
    for x in (36, 36 + 5 * cm):
        canvas.line(x, 76, x, 84)
    text(canvas, 193, 77, 'Check that this line measures 5 cm.', 10)
    footer(canvas, 'WEEK 4 / FLOOR MARKERS / CUT AND TAPE FLAT')


def sensor_card(canvas):
    heading(canvas, 5, 'Stop at the delivery strip', 'Team __________________   Robot ________')
    text(canvas, 36, 646, '1  Build a delivery lane', 14, TEAL, True)
    para(canvas, 36, 626, 'Make a flat light road. Tape a wide dark strip across the sensor path '
         'and build a delivery bay beside the road. Slide the proxy through to check clearance.')
    area(canvas, 36, 490, 540, 91)
    text(canvas, 50, 555, 'START at sensor', 10, bold=True)
    text(canvas, 263, 555, 'About 25 cm to strip', 10, centered=True)
    stroke(canvas, MUTED, 1.4)
    canvas.line(84, 528, 504, 528)
    canvas.lines([(82, 520, 82, 536), (260, 528, 251, 533), (260, 528, 251, 523)])
    canvas.setFillColor(HexColor(INK))
    canvas.rect(373, 512, 31, 35, stroke=0, fill=1)
    text(canvas, 388, 497, '6 cm wide', 9, centered=True)
    text(canvas, 465, 555, 'Clear runout', 10, MUTED)
    text(canvas, 36, 458, '2  Read the floor and choose a threshold', 14, TEAL, True)
    para(canvas, 36, 437, 'Measure each surface twice with the wheels still. Choose a number above '
         'both dark readings and below both light readings. Enter it in the marker program.')
    text(canvas, 36, 388, 'Dark ______ and ______      Light ______ and ______      Threshold ______', 11, bold=True)
    text(canvas, 36, 347, '3  Send the robot to the bay', 14, TEAL, True)
    para(canvas, 36, 326, 'Predict where it will stop. Run from the marked start. A delivery counts when '
         'the sensor is over the strip and the hub shows M. L means the robot reached its move limit.')
    for y, prompt in (
        (264, 'First run / Where was the sensor when the robot stopped?'),
        (194, 'Retest / What changed and what did you see?'),
    ):
        text(canvas, 36, y, prompt, 11, bold=True)
        stroke(canvas, LINE)
        canvas.line(36, y - 30, 576, y - 30)
    text(canvas, 36, 119, 'If the strip moves, where will the robot stop now?', 11, bold=True)
    text(canvas, 36, 81, 'Take turns as driver, navigator and observer.', 10, MUTED)
    footer(canvas, 'WEEK 5 / TEAM MISSION CARD')


def make_pdf(name, title, pages):
    canvas = Canvas(str(OUTPUT / name), pagesize=letter, invariant=1)
    canvas.setTitle(title)
    canvas.setAuthor('MechaRAMS / Cheshire YMCA')
    for page in pages:
        page(canvas)
    canvas.save()


if __name__ == '__main__':
    make_pdf('W04_Cone_Rematch.pdf', 'Week 4 Cone Challenge Rematch',
             (field_map, rematch_card, floor_markers))
    make_pdf('W05_Sensor_Mission.pdf', 'Week 5 Stop at the Delivery Strip', (sensor_card,))
