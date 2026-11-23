"""Make the full-size Week 6 field, mentor checklist, and one-print packet."""

from io import BytesIO

from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import HexColor
from reportlab.lib.units import cm
from reportlab.pdfgen.canvas import Canvas

from build_w04_w05_mission_prints import INK, LINE, MUTED, PALE, TEAL, para, stroke, text
from build_w04_w05_print_packets import PREP, PRINTS, Section, build_packet
from build_w04_w05_setup_checklists import (
    LEFT, checks, finish, item, make_pdf, section, title as checklist_title,
)
from build_w05_full_size_field import FIRST_MARK, LANE_LENGTH, LANE_WIDTH, PAGE, START, STRIP_DEPTH, ruler

WEEK_5_FIELD = PRINTS / 'W05_Delivery_Strip_Full_Size_Field.pdf'
RESCUE_FIELD = PRINTS / 'W06_Rescue_Full_Size_Field.pdf'
CHECKLIST = PREP / 'W06_rescue_Checklist.pdf'


def heading(canvas, title, subtitle):
    text(canvas, 36, 575, 'MECHARAMS / CHESHIRE YMCA / WEEK 6', 9, TEAL, True)
    text(canvas, 36, 539, title, 28, bold=True)
    text(canvas, 36, 515, subtitle, 11, MUTED)
    stroke(canvas, LINE)
    canvas.line(36, 500, 756, 500)


def guide(canvas):
    heading(canvas, 'Set up the rescue field',
            f'{LANE_WIDTH} x {LANE_LENGTH} cm lane / Week 5 sensor start and dark strip')
    steps = (
        ('1  Assemble the three lane tiles',
         'Print pages 2-6 on landscape US Letter at Actual Size. Trim the sides and use a ruler '
         'between the end marks. Join A-B-C at the paired ticks, tape from behind and tape the lane '
         'flat. Page 5 is the strip. Page 6 has the rescue tabs.'),
        ('2  Set the strip and sensor start',
         f'Set the near edge of the {STRIP_DEPTH} cm dark strip at the {FIRST_MARK} cm marks on B. '
         'Tape its ends. Center downward sensor D between START marks on A. Keep the taped seams '
         'flat and leave clear runout past C.'),
        ('3  Rehearse and mark the cube position',
         'Fit the mentor plow and place a lightweight cube just ahead of it. Mark the cube center '
         'with the CUBE START tabs at the sides. Recheck the Week 5 threshold with the plow fitted, '
         'then run W06_rescue.py.'),
        ('4  Place the rescue bay',
         'After a stop with M and the cube still controlled, use the bay tabs to mark near and far edges around the '
         'resting cube. Put tabs at the sides, with arrows pointing across the lane. Save these '
         'positions for both trials on that kit. Score the cube separately from the sensor stop.'),
    )
    for (label, content), y in zip(steps, (470, 374, 279, 182)):
        text(canvas, 36, y, label, 13, TEAL, True)
        para(canvas, 36, y - 19, content, 478, 10.5, 14)

    x, y, units = 579, 131, 4.7
    for i, label in enumerate(('A / START', 'B / STRIP', 'C / RUNOUT')):
        bottom = y + i * 20 * units
        stroke(canvas, TEAL)
        canvas.setFillColor(HexColor(PALE))
        canvas.rect(x, bottom, LANE_WIDTH * units, 20 * units, stroke=1, fill=1)
        text(canvas, x + 12 * units, bottom + 26, label, 10, TEAL, True, True)
    canvas.setFillColorCMYK(0, 0, 0, 1)
    canvas.rect(x, y + (FIRST_MARK + START) * units, LANE_WIDTH * units,
                STRIP_DEPTH * units, stroke=0, fill=1)
    stroke(canvas, TEAL)
    canvas.lines([(714, 148, 714, 403), (709, 394, 714, 403), (719, 394, 714, 403)])
    text(canvas, 714, 422, 'TRAVEL', 8, TEAL, True, True)
    text(canvas, 636, 106, 'Place cube and bay tabs after', 8.5, MUTED, centered=True)
    text(canvas, 636, 92, 'rehearsing on each robot.', 8.5, MUTED, centered=True)
    ruler(canvas, 36, 51)
    canvas.showPage()


def tabs(canvas):
    heading(canvas, 'Cut out the rescue tabs', 'Use one left and one right tab for each mark.')
    para(canvas, 36, 465, 'Tape the tabs along the outside edges of the lane, with the arrows pointing '
         'toward each other. Use the paired CUBE START tabs to line up the cube center before each run. '
         'Keep the center of the lane clear.', 715)
    for i, label in enumerate(('CUBE START', 'BAY / NEAR EDGE', 'BAY / FAR EDGE')):
        y = 348 - 75*i
        for x, side in ((172, 'LEFT'), (462, 'RIGHT')):
            stroke(canvas, TEAL, 0.8)
            canvas.setDash(5, 3)
            canvas.rect(x, y, 158, 52, fill=0, stroke=1)
            canvas.setDash()
            text(canvas, x+79, y+31, label, 11, TEAL, True, True)
            text(canvas, x+79, y+13, side, 9, MUTED, centered=True)
            tip = x+146 if side == 'LEFT' else x+12
            inset = -5 if side == 'LEFT' else 5
            canvas.lines([(tip+3*inset,y+16,tip,y+16), (tip+inset,y+20,tip,y+16),
                          (tip+inset,y+12,tip,y+16)])
    para(canvas, 36, 124, 'Set the two bay edges around the cube position you measured in the mentor '
         'trial. A rescue counts when the sensor stops with M and the cube finishes with its full '
         'base inside the marked bay.', 710)
    ruler(canvas, 36, 51)
    canvas.showPage()


def make_field():
    stream = BytesIO()
    canvas = Canvas(stream, pagesize=PAGE, invariant=1)
    guide(canvas)
    tabs(canvas)
    canvas.save()
    stream.seek(0)
    rescue = PdfReader(stream)
    week5 = PdfReader(WEEK_5_FIELD)
    writer = PdfWriter()
    writer.add_metadata({'/Title': 'Week 6 Full-Size Rescue Field', '/Author': 'MechaRAMS / Cheshire YMCA'})
    writer.add_page(rescue.pages[0])
    for page in week5.pages[1:5]:
        writer.add_page(page)
    writer.add_page(rescue.pages[1])
    writer.write(RESCUE_FIELD)


def checklist(canvas):
    checklist_title(canvas, 6, 'Rescue attachment')
    y = section(canvas, '1  Print for two rescue fields', 663)
    y = item(canvas, y, 'Field sets: pages 2-6, two sets (10 sheets). Landscape Letter at Actual Size. '
             'Page 1 is the assembly guide.', RESCUE_FIELD.name)
    y = item(canvas, y, 'Five team sheets (four teams and a spare), four build cards and one attendance '
             'sheet. Class print total is 20 sheets before the guide and checklist.',
             'W06_rescue_Team_Sheet.pdf')
    y = section(canvas, '2  Set up both lanes', y - 1)
    y = item(canvas, y, 'Check the 5 cm ruler. Match the paired ticks and tape A-B-C from behind. '
             'Tape the lane flat. Set the Week 5 dark strip at 25 cm and keep the runout clear.')
    y = item(canvas, y, 'Set out six lightweight cubes (one per robot and one per build team), '
             'two tested mentor plows, four build packs and four mounting proxies.')
    y = item(canvas, y, 'Put the cube just ahead of the plow. Use the side tabs to mark its center at '
             'the start. Mark each rescue bay around the cube after a successful mentor run.')
    y = section(canvas, '3  Rehearse on both robots', y - 1)
    y = checks(canvas, y - 1, [
        'Load W06_rescue.py. Verify A left, B right, hub pairing, forward motion and Stop.',
        'Mount the passive plow. Check wheel and floor clearance and the view of downward sensor D.',
        'Recheck the Week 5 threshold on white, seams and dark strip with the plow fitted. Set the start.',
        'Remove strip and cube for a full miss run. Confirm L and clear floor for the whole robot.',
        'Restore strip and cube. Confirm M and separately check that the whole cube base reaches the bay.',
    ])
    text(canvas, LEFT, y, 'Saved threshold', 10, TEAL, True)
    text(canvas, LEFT + 101, y, 'Kit A _________________  Kit B _________________', 10)
    y = item(canvas, y-17, 'Keep the cube, start, strip and code fixed for team comparisons. '
             'Approve and hand-check each student attachment before a robot run.')
    finish(canvas, y - 3, 'W06_rescue.pptx')


def print_plan():
    return (
        Section('Mentor checklist', CHECKLIST),
        Section('Rescue field assembly guide', RESCUE_FIELD),
        Section('Kit A field, strip and rescue tabs', RESCUE_FIELD, 2, 6),
        Section('Kit B field, strip and rescue tabs', RESCUE_FIELD, 2, 6),
        Section('Team sheets (4 teams + spare)', PRINTS / 'W06_rescue_Team_Sheet.pdf', copies=5),
        Section('Build cards (one per team)', PRINTS / 'W06_rescue_Build_Card.pdf', copies=4),
        Section('Attendance', PRINTS / 'Attendance.pdf'),
    )


if __name__ == '__main__':
    make_field()
    make_pdf(CHECKLIST.name, 'Week 6 Rescue Mentor Setup Checklist', checklist)
    build_packet(6, 'W06_Class_Print_Packet.pdf', 'Week 6 Rescue Class Print Packet', plan=print_plan())
