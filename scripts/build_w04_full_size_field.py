"""Tile the Week 4 rematch field at 1:1 scale on nine US Letter sheets."""

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.pdfgen.canvas import Canvas

from build_w04_w05_mission_prints import (
    AXLE_START, CONE_RADIUS, FIELD_SIZE, HOME_RADIUS, INK, LINE, MUTED, ORANGE,
    OUTPUT, PALE, TEAL, WHITE, circle, cross, field_geometry, footer, heading, para,
    stroke, text,
)

TILE_SIZE = FIELD_SIZE // 3
SIDE = TILE_SIZE * cm
LEFT = (letter[0] - SIDE) / 2
BOTTOM = (letter[1] - SIDE) / 2
TILES = ('ABC', 'DEF', 'GHI')


def scale_check(canvas, x, y):
    stroke(canvas, INK, 1)
    end = x + 5 * cm
    canvas.lines([(x, y, end, y), (x, y - 4, x, y + 4), (end, y - 4, end, y + 4)])
    text(canvas, end + 13, y - 3, 'This line must measure 5 cm.', 9, MUTED)


def instructions(canvas):
    heading(canvas, 4, 'Print the cone rematch field', 'Nine US Letter tiles make a 60 x 60 cm playfield.')
    text(canvas, 36, 645, '1  Print pages 2-10', 14, TEAL, True)
    para(canvas, 36, 624, 'Set the printer to US Letter, portrait, single-sided, '
         '100% or Actual Size. Check the 5 cm line before printing the whole set.', 295)

    text(canvas, 36, 552, '2  Lay out A through I', 14, TEAL, True)
    para(canvas, 36, 531, 'Keep the tile headings upright and arrange the sheets '
         'as shown. If you will shuffle them after trimming, pencil each letter on the back first.', 295)

    text(canvas, 36, 459, '3  Trim and join', 14, TEAL, True)
    para(canvas, 36, 438, 'Cut all four edges of each square on the dashed trim lines. '
         'Butt cut edges together, match the paired ticks and grid lines, and tape the seams from behind.', 295)

    for row, letters in enumerate(TILES):
        for column, label in enumerate(letters):
            x, y = 373 + column * 63, 551 - row * 63
            stroke(canvas, TEAL, 1)
            canvas.setFillColor(HexColor(PALE))
            canvas.rect(x, y, 63, 63, stroke=1, fill=1)
            text(canvas, x + 31.5, y + 25, label, 17, TEAL, True, True)
    text(canvas, 468, 411, 'TOP ROW A-B-C', 9, MUTED, True, True)
    text(canvas, 468, 392, 'START is on tile G', 9, MUTED, centered=True)

    text(canvas, 36, 341, '4  Tape the field flat and rehearse', 14, TEAL, True)
    y = para(canvas, 36, 320, 'Tape down the outer edges, then leave about 20 cm of clear floor around '
             'the field as a starting layout. Increase clearance if the robot or pusher needs more room.')
    para(canvas, 36, y - 11, 'Align the drive axle midpoint over START. Face the arrow and load Cone 1 '
         'first. Use the dashed 4 cm circles for the cone starts and the solid 8 cm circles for their homes. '
         'Rehearse with each robot and adjust the marks with tape if needed.')
    scale_check(canvas, 36, 164)
    footer(canvas, 'WEEK 4 / ASSEMBLY GUIDE / PAGE 1 OF 10')


def draw_field(canvas, geometry):
    """Render the whole field in points, including sections that cross seams."""
    for i in range(0, FIELD_SIZE + 1, 5):
        stroke(canvas, LINE, 0.55 if i % 10 == 0 else 0.27)
        canvas.line(i * cm, 0, i * cm, FIELD_SIZE * cm)
        canvas.line(0, i * cm, FIELD_SIZE * cm, i * cm)

    for axle, pivot, _, home in geometry:
        stroke(canvas, INK, 1.3)
        canvas.line(*(v * cm for v in (*axle, *pivot)))
        stroke(canvas, MUTED, 0.8)
        canvas.setDash(4, 3)
        canvas.line(*(v * cm for v in (*pivot, *home)))
        canvas.setDash()

    for i, (_, _, cone, home) in enumerate(geometry, 1):
        for position, radius, color, label, dashed in (
            (cone, CONE_RADIUS, ORANGE, f'CONE {i}', True),
            (home, HOME_RADIUS, TEAL, f'HOME {i}', False),
        ):
            x, y = (v * cm for v in position)
            circle(canvas, x, y, radius * cm, color, dashed, fill=WHITE if dashed else PALE)
            cross(canvas, x, y, color)
            label_y = y - 25 if dashed else y + 30
            text(canvas, x, label_y, label, 11 if dashed else 16, color, True, True)

    x, y = (v * cm for v in AXLE_START)
    stroke(canvas, INK, 1.45)
    canvas.lines([(x - 30, y, x + 30, y), (x, y, x, y + 60),
                  (x - 9, y + 48, x, y + 60), (x + 9, y + 48, x, y + 60)])
    text(canvas, x, y - 20, 'START / AXLE MIDPOINT', 11, bold=True, centered=True)


def registration(canvas, row, column):
    """Draw matching double ticks inside shared edges where the cut preserves them."""
    stroke(canvas, MUTED, 0.8)
    for x, direction, shared in ((LEFT, 1, column > 0), (LEFT + SIDE, -1, column < 2)):
        if shared:
            for distance in (3, 3.25, 16, 16.25):
                y = BOTTOM + distance * cm
                canvas.line(x, y, x + direction * 0.42 * cm, y)
    # The center column's second pair stays clear of the Home 2 center.
    second_tick = 9 if column == 1 else 16
    for y, direction, shared in ((BOTTOM, 1, row < 2), (BOTTOM + SIDE, -1, row > 0)):
        if shared:
            for distance in (3, 3.25, second_tick, second_tick + 0.25):
                x = LEFT + distance * cm
                canvas.line(x, y, x, y + direction * 0.42 * cm)


def tile(canvas, geometry, row, column):
    label = TILES[row][column]
    page = 2 + 3 * row + column
    text(canvas, LEFT, 748, f'WEEK 4 CONE REMATCH / TILE {label}', 10, TEAL, True)
    text(canvas, LEFT, 708, f'Row {row + 1}, column {column + 1}', 25, bold=True)
    text(canvas, LEFT, 689, 'Keep this heading at the top. Cut the square on all four dashed lines.',
         10, MUTED)

    canvas.saveState()
    square = canvas.beginPath()
    square.rect(LEFT, BOTTOM, SIDE, SIDE)
    canvas.clipPath(square, stroke=0, fill=0)
    canvas.translate(LEFT - column * SIDE, BOTTOM - (2 - row) * SIDE)
    draw_field(canvas, geometry)
    canvas.restoreState()

    registration(canvas, row, column)
    stroke(canvas, INK, 0.9)
    canvas.setDash(5, 3)
    canvas.rect(LEFT, BOTTOM, SIDE, SIDE, stroke=1, fill=0)
    canvas.setDash()

    text(canvas, LEFT, 85, 'TRIM SQUARE / 20 x 20 cm', 9, MUTED, True)
    scale_check(canvas, LEFT, 61)
    footer(canvas, f'WEEK 4 / TILE {label} / PAGE {page} OF 10 / ACTUAL SIZE')


if __name__ == '__main__':
    canvas = Canvas(str(OUTPUT / 'W04_Cone_Rematch_Full_Size_Field.pdf'),
                    pagesize=letter, invariant=1)
    canvas.setTitle('Week 4 Cone Rematch - Full-Size Tiled Field')
    canvas.setAuthor('MechaRAMS / Cheshire YMCA')
    instructions(canvas)
    geometry = field_geometry()
    for row, labels in enumerate(TILES):
        for column in range(len(labels)):
            tile(canvas, geometry, row, column)
    canvas.save()
