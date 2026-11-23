"""Build the full-size Week 5 sensor lane and a movable matte-dark strip template."""

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.units import cm
from reportlab.pdfgen.canvas import Canvas

from build_w04_w05_mission_prints import INK, LINE, MUTED, OUTPUT, PALE, TEAL, para, stroke, text

PAGE = landscape(letter)
LANE_WIDTH = 24
TILE_LENGTH = 20
START = 8
FIRST_MARK = 25
RETEST_MARK = 20
STRIP_DEPTH = 6
TILES = ('A', 'B', 'C')
LANE_LENGTH = len(TILES) * TILE_LENGTH
LEFT = (PAGE[0] - LANE_WIDTH * cm) / 2
BOTTOM = (PAGE[1] - TILE_LENGTH * cm) / 2


def heading(canvas, title, subtitle):
    text(canvas, 36, 574, 'MECHARAMS / CHESHIRE YMCA / WEEK 5', 9, TEAL, True)
    text(canvas, 36, 539, title, 28, bold=True)
    text(canvas, 36, 512, subtitle, 11, MUTED)
    stroke(canvas, LINE)
    canvas.line(36, 498, 756, 498)


def ruler(canvas, x, y):
    stroke(canvas, INK, 0.9)
    end = x + 5 * cm
    canvas.lines([(x, y, end, y), (x, y - 4, x, y + 4), (end, y - 4, end, y + 4)])
    text(canvas, end + 12, y - 3, 'This line must measure 5 cm.', 9, MUTED)


def instructions(canvas):
    heading(canvas, 'Print the delivery-strip field',
            f'Three US Letter tiles make a {LANE_WIDTH} x {LANE_LENGTH} cm lane.')
    paragraphs = (
        ('1  Print at actual size',
         'Print pages 2-5 on matte white US Letter in landscape at 100% or Actual Size. '
         'Pages 2-4 are the lane. Page 5 is the separate dark strip. Check the 5 cm ruler.'),
        ('2  Join A, B and C',
         'Use a ruler to cut each end straight between the dashed marks at the sides. '
         'Cut the two long sides on their dashed lines. Butt the cut edges together, '
         'match the paired ticks and tape the seams from behind. Tape the lane flat.'),
        ('3  Place the strip and start the robot',
         'Cut out the strip and put its near edge at the 25 cm marks on B. Secure only '
         'the ends with low-tack tape so teams can move it to 20 cm for a retest. Center the '
         'downward sensor between the START marks on A and face toward C.'),
        ('4  Check detection and runout',
         'Measure reflection on the white lane, at the seams and on the dark strip. Use '
         'matte black tape or card if printed black gives weak contrast. Remove the strip '
         'and rehearse the full run on each kit. The robot should finish with L. Leave '
         'clear floor beyond C for the full robot to stop.'),
    )
    for (title, body), y in zip(paragraphs, (466, 373, 273, 172)):
        text(canvas, 36, y, title, 13, TEAL, True)
        para(canvas, 36, y - 20, body, 460, 10.5, 14)

    x, y, unit = 565, 112, 5
    for index, (label, caption) in enumerate(zip(TILES, ('START', 'STRIP', 'RUNOUT'))):
        base = y + index * TILE_LENGTH * unit
        canvas.setFillColor(HexColor(PALE))
        stroke(canvas, TEAL)
        canvas.rect(x, base, LANE_WIDTH * unit, TILE_LENGTH * unit, stroke=1, fill=1)
        text(canvas, x + 60, base + 34, f'{label} / {caption}', 11, TEAL, True, True)
    canvas.setFillColorCMYK(0, 0, 0, 1)
    canvas.rect(x, y + (START + FIRST_MARK) * unit,
                LANE_WIDTH * unit, STRIP_DEPTH * unit, stroke=0, fill=1)
    stroke(canvas, TEAL, 1.1)
    canvas.lines([(705, 123, 705, 400), (701, 393, 705, 400), (709, 393, 705, 400)])
    text(canvas, 705, 420, 'TRAVEL', 9, TEAL, True, True)
    text(canvas, 625, 93, '52 cm from START to lane end', 9, MUTED, centered=True)
    text(canvas, 625, 77, 'Leave clear floor past C.', 9, MUTED, centered=True)
    ruler(canvas, 36, 48)
    canvas.showPage()


def cut_lines(canvas, tile):
    """Keep the transverse cutting and registration marks out of the sensor path."""
    right = LEFT + LANE_WIDTH * cm
    top = BOTTOM + TILE_LENGTH * cm
    stroke(canvas, INK, 0.7)
    canvas.setDash(5, 3)
    canvas.lines([(LEFT, BOTTOM, LEFT, top), (right, BOTTOM, right, top)])
    for y in (BOTTOM, top):
        canvas.lines([(LEFT, y, LEFT + 4 * cm, y), (right - 4 * cm, y, right, y)])
    canvas.setDash()

    stroke(canvas, MUTED, 0.75)
    for edge, direction, shared in (
        (BOTTOM, 1, tile > 0), (top, -1, tile < len(TILES) - 1),
    ):
        if shared:
            for distance in (2.5, 2.75, 21.25, 21.5):
                x = LEFT + distance * cm
                canvas.line(x, edge, x, edge + direction * 0.45 * cm)


def lane_sign(canvas, height, label, subtitle):
    """A split line marks a position without interrupting the blank sensor corridor."""
    y = BOTTOM + height * cm
    right = LEFT + LANE_WIDTH * cm
    stroke(canvas, TEAL, 1.5)
    canvas.lines([(LEFT + cm, y, LEFT + 4.5 * cm, y),
                  (right - 4.5 * cm, y, right - cm, y)])
    text(canvas, LEFT + cm, y + 7, label, 10, TEAL, True)
    text(canvas, LEFT + cm, y - 15, subtitle, 8, MUTED)


def side_title(canvas, title, x, y):
    canvas.saveState()
    canvas.translate(x, y)
    canvas.rotate(90)
    text(canvas, 0, 0, title, 9, INK, True, True)
    canvas.restoreState()


def field_tile(canvas, tile):
    label = TILES[tile]
    side_title(canvas, f'WEEK 5 / TILE {label} / {("START", "APPROACH", "RUNOUT")[tile]}',
               32, PAGE[1] / 2)
    side_title(canvas, 'TRAVEL UP TOWARD C / CUT ON DASHED EDGE MARKS',
               PAGE[0] - 31, PAGE[1] / 2)
    stroke(canvas, LINE, 0.6)
    for offset in (0.8, LANE_WIDTH - 0.8):
        x = LEFT + offset * cm
        canvas.line(x, BOTTOM + 0.5 * cm, x, BOTTOM + (TILE_LENGTH - 0.5) * cm)

    if tile == 0:
        lane_sign(canvas, START, 'SENSOR START', 'Center sensor between marks')
    elif tile == 1:
        lane_sign(canvas, START + FIRST_MARK - TILE_LENGTH, '25 CM', 'First strip position')
        lane_sign(canvas, START + RETEST_MARK - TILE_LENGTH, '20 CM', 'Retest position')
    else:
        text(canvas, LEFT + 1.15 * cm, BOTTOM + 18 * cm, 'RUNOUT', 10, TEAL, True)
        text(canvas, LEFT + 1.15 * cm, BOTTOM + 17.3 * cm, 'Keep end clear', 8, MUTED)
    cut_lines(canvas, tile)
    canvas.showPage()


def marker_strip(canvas):
    heading(canvas, 'Cut out the movable strip',
            f'Actual size / {LANE_WIDTH} cm across the lane x {STRIP_DEPTH} cm along the direction of travel')
    para(canvas, 36, 463, 'Cut along the outside of the black rectangle. Line up the near edge '
         'with the chosen side marks on tile B. Use small pieces of low-tack tape at the ends.', 720)
    canvas.setFillColorCMYK(0, 0, 0, 1)
    canvas.rect(LEFT, 200, LANE_WIDTH * cm, STRIP_DEPTH * cm, stroke=0, fill=1)
    text(canvas, LEFT, 176, 'NEAR EDGE / FACE THIS EDGE TOWARD START', 10, TEAL, True)
    para(canvas, 36, 121, 'If the printed strip gives inconsistent readings, use this as a cutting guide '
         'for matte black card or matte black tape. Measure the surface under classroom lighting.', 720)
    ruler(canvas, 36, 48)
    canvas.showPage()


if __name__ == '__main__':
    canvas = Canvas(str(OUTPUT / 'W05_Delivery_Strip_Full_Size_Field.pdf'), pagesize=PAGE, invariant=1)
    canvas.setTitle('Week 5 Delivery Strip - Full-Size Tiled Field')
    canvas.setAuthor('MechaRAMS / Cheshire YMCA')
    instructions(canvas)
    for tile in range(len(TILES)):
        field_tile(canvas, tile)
    marker_strip(canvas)
    canvas.save()
