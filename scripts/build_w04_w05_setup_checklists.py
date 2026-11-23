"""Build the one-page mentor setup checklists for the two tiled fields."""

from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import simpleSplit
from reportlab.pdfgen.canvas import Canvas

from build_w04_w05_mission_prints import INK, LINE, MUTED, PALE, TEAL, stroke, text

OUTPUT = Path(__file__).resolve().parents[1] / '01_Instructor' / 'Class_Preparation'
REPO = 'https://github.com/FRC999/YMCA-SPIKE-education/blob/main/'
LEFT, RIGHT = 36, 576
KIT_A, KIT_B = 507, 553


def box(canvas, x, y):
    stroke(canvas, INK, 0.8)
    canvas.rect(x, y, 9, 9, fill=0, stroke=1)


def title(canvas, week, lesson):
    text(canvas, LEFT, 753, f'WEEK {week} / MENTOR SETUP CHECKLIST', 10, TEAL, True)
    text(canvas, LEFT, 721, lesson, 25, bold=True)
    text(canvas, LEFT, 696, 'Date __________________  Lead __________________  Two robots / Four teams', 10, MUTED)
    stroke(canvas, LINE)
    canvas.line(LEFT, 682, RIGHT, 682)


def section(canvas, label, y):
    text(canvas, LEFT, y, label, 13, TEAL, True)
    return y - 19


def item(canvas, y, description, source=None):
    box(canvas, LEFT, y - 1)
    lines = simpleSplit(description, 'Helvetica', 10.1, RIGHT-LEFT-20)
    for line in lines:
        text(canvas, LEFT + 19, y, line, 10.1)
        y -= 13
    if source:
        text(canvas, LEFT + 19, y, source, 9, TEAL)
        width = canvas.stringWidth(source, 'Helvetica', 9)
        canvas.linkURL(REPO + '02_Student/Printouts/' + source,
                       (LEFT + 19, y - 2, LEFT + 19 + width, y + 9), relative=0)
        y -= 12
    return y - 5


def checks(canvas, y, rows):
    canvas.setFillColor(HexColor(PALE))
    canvas.rect(LEFT, y - 6, RIGHT-LEFT, 20, fill=1, stroke=0)
    text(canvas, LEFT+8, y, 'Check after a pass on the actual floor', 9.5, TEAL, True)
    text(canvas, KIT_A, y, 'Kit A', 9.5, TEAL, True, True)
    text(canvas, KIT_B, y, 'Kit B', 9.5, TEAL, True, True)
    y -= 22
    for description in rows:
        lines = simpleSplit(description, 'Helvetica', 9.8, KIT_A-LEFT-28)
        box(canvas, KIT_A-4.5, y-1)
        box(canvas, KIT_B-4.5, y-1)
        for line in lines:
            text(canvas, LEFT + 8, y, line, 9.8)
            y -= 12
        stroke(canvas, LINE, 0.45)
        canvas.line(LEFT, y+5, RIGHT, y+5)
        y -= 5
    return y - 4


def finish(canvas, y, deck):
    y = item(canvas, y, f'Open {deck} in Presenter View. Set two robot stations '
             'and two build tables. Assign mentors and confirm where to stop and reset.')
    text(canvas, LEFT, y-5, 'Notes for the teaching team', 10, TEAL, True)
    stroke(canvas, LINE, 0.6)
    for space in (22, 43):
        canvas.line(LEFT, y-space, RIGHT, y-space)
    if y - 43 < 51:
        raise ValueError(f'Checklist text extends into the footer at {y:.1f} pt')
    stroke(canvas, LINE)
    canvas.line(LEFT, 45, RIGHT, 45)
    text(canvas, LEFT, 28, 'MechaRAMS / Cheshire YMCA', 8, MUTED)
    text(canvas, 382, 28, 'Keep this page at the mentor station.', 8, MUTED)
    canvas.showPage()


def week4(canvas):
    title(canvas, 4, 'Cone challenge rematch')
    y = section(canvas, '1  Print for two fields', 663)
    y = item(canvas, y, 'Field tiles: pages 2-10, two sets (18 sheets). Letter portrait, '
             'single-sided at Actual Size. Page 1 has the assembly diagram.',
             'W04_Cone_Rematch_Full_Size_Field.pdf')
    y = item(canvas, y, 'Team card: page 2, five copies (four teams and one spare).',
             'W04_Cone_Rematch.pdf')
    y = item(canvas, y, 'Attendance.pdf: one copy. Class print total is 24 sheets. '
             'If making cones, two extra template sheets yield eight.',
             'W03_Paper_Cone_Template.pdf')
    y = section(canvas, '2  Set up the fields', y - 1)
    y = item(canvas, y, 'Check the 5 cm ruler. Trim all four edges. Join A-B-C / D-E-F / G-H-I by '
             'matching paired ticks. Butt the edges and tape the seams from behind.')
    y = item(canvas, y, 'Tape both 60 x 60 cm fields flat. Start with about 20 cm of clear floor around each. '
             'Align the axle midpoint at START on tile G and face the arrow.')
    y = item(canvas, y, 'Put only Cone 1 on its dashed start. Set out six cones plus spares, '
             'two mentor pushers, four build packs or team pushers, and four mounting proxies.')
    y = section(canvas, '3  Rehearse on both robots', y - 1)
    y = checks(canvas, y - 1, [
        'Load W04_cone_rematch.py at SPEED = 200. Verify A left, B right, hub pairing, forward motion and Stop.',
        'Fit the low centered rounded tip with the robot stopped. Check floor, wheel and turn clearance.',
        'Dry-run without cones. Check axle stops and heading after each turn. Check the entire swept path.',
        'Run Cone 1. It releases on the turn and stays upright with its base inside Home 1 after the run.',
        'Stretch: test the diagonal to Cone 2, then Cone 3. Check that earlier homes stay clear.',
    ])
    text(canvas, LEFT, y, 'Tested course', 10, TEAL, True)
    text(canvas, LEFT+88, y, 'Kit A ____________________  Kit B ____________________', 10)
    y -= 16
    y = item(canvas, y, 'Save each kit baseline. If the full route is unreliable, use one cone '
             'and note the usable start and settings.')
    finish(canvas, y - 3, 'W04_cone_rematch.pptx')


def week5(canvas):
    title(canvas, 5, 'Stop at the delivery strip')
    y = section(canvas, '1  Print for two lanes', 663)
    y = item(canvas, y, 'Lane and strip: pages 2-5, two sets (8 sheets). Letter landscape, '
             'single-sided at Actual Size. Pages 2-4 are tiles, page 5 is the strip.',
             'W05_Delivery_Strip_Full_Size_Field.pdf')
    y = item(canvas, y, 'Team mission card: five copies (four teams and one spare). '
             'Attendance.pdf: one copy. Class print total is 14 sheets.', 'W05_Sensor_Mission.pdf')
    y = section(canvas, '2  Set up the lanes and wall demo', y - 1)
    y = item(canvas, y, 'Check the 5 cm ruler. Use a straightedge between the side marks to trim the '
             'ends. Join A-B-C by matching paired ticks, tape from behind, and tape the lanes flat.')
    y = item(canvas, y, 'Cut out the 24 x 6 cm strip. Set its near edge at 25 cm on B and tape only its '
             'ends. Keep the center blank and leave clear floor beyond C. Use 20 cm for the retest.')
    y = item(canvas, y, 'Wall demo on one kit: sensor C faces a broad wall from about 30 cm. Run '
             'W05_distance_demo.py at 150 and 200 mm. Confirm 200 stops farther away. Reload the marker project.')
    y = section(canvas, '3  Rehearse on both robots', y - 1)
    y = checks(canvas, y - 1, [
        'Load W05_marker.py. Verify A left, B right, hub pairing, forward motion and Stop.',
        'Center sensor D between START marks facing C. Adjust its height from about 1-2 cm.',
        'Read white and dark twice each, and check seams. Choose a whole-number threshold above both dark readings and below both light readings.',
        'With the strip at 25 cm, the robot shows M with its sensor over the strip. Try the 20 cm retest.',
        'Remove the strip. Run the full routine through L and confirm there is room for the whole robot to stop.',
    ])
    text(canvas, LEFT, y, 'Saved threshold', 10, TEAL, True)
    text(canvas, LEFT+99, y, 'Kit A _________________  Kit B _________________', 10)
    y -= 16
    y = item(canvas, y, 'If readings overlap or a seam triggers M, flatten the lane, adjust sensor height '
             'or use matte black card. Remeasure and retest.')
    finish(canvas, y - 3, 'W05_marker.pptx')


def make_pdf(filename, label, page):
    canvas = Canvas(str(OUTPUT / filename), pagesize=letter, invariant=1)
    canvas.setTitle(label)
    canvas.setAuthor('MechaRAMS / Cheshire YMCA')
    page(canvas)
    canvas.save()


if __name__ == '__main__':
    make_pdf('W04_cone_rematch_Setup_Checklist.pdf', 'Week 4 Mentor Setup Checklist', week4)
    make_pdf('W05_sensor_mission_Setup_Checklist.pdf', 'Week 5 Mentor Setup Checklist', week5)
