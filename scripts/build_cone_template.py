"""Generate the four printable Week 3 paper cones on one US Letter sheet."""

from math import cos, degrees, hypot, pi, sin
from pathlib import Path

from reportlab.lib.colors import HexColor, black
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.pdfgen.canvas import Canvas

OUTPUT = Path(__file__).resolve().parents[1] / '02_Student/Printouts/W03_Paper_Cone_Template.pdf'
HEIGHT_MM = 50
BASE_RADIUS_MM = 20
SLANT_MM = hypot(HEIGHT_MM, BASE_RADIUS_MM)
# The curved edge becomes the base circumference when the seam is closed.
SECTOR_ANGLE = 2 * pi * BASE_RADIUS_MM / SLANT_MM
HALF_ANGLE = SECTOR_ANGLE / 2


def draw_cone(canvas, x, y, label):
    def point(angle, radius=SLANT_MM):
        return x + radius * mm * cos(angle), y + radius * mm * sin(angle)

    def tab_point(radius, width):
        return (
            x + mm * (radius * cos(HALF_ANGLE) - width * sin(HALF_ANGLE)),
            y - mm * (radius * sin(HALF_ANGLE) + width * cos(HALF_ANGLE)),
        )

    seam_end = point(-HALF_ANGLE)
    outer_tab = tab_point(SLANT_MM - 4, 6)
    inner_tab = tab_point(8, 3)

    tab = canvas.beginPath()
    tab.moveTo(x, y)
    for corner in (seam_end, outer_tab, inner_tab):
        tab.lineTo(*corner)
    tab.close()
    canvas.setFillColor(HexColor('#E6E6E6'))
    canvas.drawPath(tab, stroke=0, fill=1)
    canvas.setFillColor(black)

    outline = canvas.beginPath()
    outline.moveTo(x, y)
    for step in range(241):
        outline.lineTo(*point(HALF_ANGLE - SECTOR_ANGLE * step / 240))
    outline.lineTo(*outer_tab)
    outline.lineTo(*inner_tab)
    outline.close()
    canvas.setLineWidth(0.85)
    canvas.drawPath(outline)

    canvas.saveState()
    canvas.setDash(4, 3)
    canvas.setLineWidth(0.65)
    canvas.line(x, y, *seam_end)
    canvas.restoreState()

    canvas.setFont('Helvetica-Bold', 11)
    canvas.drawString(x + 15 * mm, y + 7, label)
    canvas.setFont('Helvetica', 9)
    canvas.drawString(x + 15 * mm, y - 8, '5 cm tall')
    canvas.drawString(x + 15 * mm, y - 21, '4 cm base diameter')

    for position, tilt, text in (
        (point(HALF_ANGLE - 0.12, 20), HALF_ANGLE, 'FREE EDGE'),
        (point(-HALF_ANGLE + 0.16, 25), -HALF_ANGLE, 'SEAM'),
        (tab_point(25, 3.6), -HALF_ANGLE, 'TAB'),
    ):
        canvas.saveState()
        canvas.translate(*position)
        canvas.rotate(degrees(tilt))
        canvas.setFont('Helvetica', 7)
        canvas.drawString(0, 0, text)
        canvas.restoreState()


def main():
    canvas = Canvas(str(OUTPUT), pagesize=letter, pageCompression=1, invariant=1)
    canvas.setTitle('Week 3 Paper Cones')
    canvas.setAuthor('MechaRAMS / Cheshire YMCA')
    canvas.setFont('Helvetica-Bold', 20)
    canvas.drawString(36, 752, 'Paper cones for the robot dance')
    canvas.setFont('Helvetica', 11)
    canvas.drawString(36, 731, 'Two sets on one page. Make one cone and one spare for each robot.')
    canvas.setFont('Helvetica-Bold', 10)
    canvas.drawString(36, 710, 'US Letter / print single-sided at 100% or Actual size')
    canvas.setFont('Helvetica', 9)
    canvas.drawString(36, 694, 'Cut along the solid outlines. Use the dashed lines to align the seams.')

    scale_start = 413
    scale_end = scale_start + 50 * mm
    canvas.setLineWidth(0.7)
    canvas.line(scale_start, 699, scale_end, 699)
    for tick in (scale_start, scale_end):
        canvas.line(tick, 695, tick, 703)
    canvas.setFont('Helvetica', 8)
    canvas.drawCentredString((scale_start + scale_end) / 2, 708, 'Check that this line measures 5 cm')

    for x, y, label in (
        (78, 520, 'Set A / cone'),
        (348, 520, 'Set B / cone'),
        (78, 225, 'Set A / spare'),
        (348, 225, 'Set B / spare'),
    ):
        draw_cone(canvas, x, y, label)

    canvas.setFont('Helvetica', 9)
    canvas.drawString(36, 65, '1. Cut out each shape with its tab. Curl the paper gently into a cone.')
    canvas.drawString(36, 52, '2. Bring the FREE EDGE to the dashed SEAM. Tuck the TAB inside and tape the seam flat.')
    canvas.drawString(36, 39, '3. Stand the cone on its curved rim. Check that it slides with a gentle push and turn.')
    canvas.setFont('Helvetica', 8)
    canvas.drawString(36, 23, 'Use light cardstock if available. Use the same cone for all three repeats of the dance.')
    canvas.save()
    print(OUTPUT)


if __name__ == '__main__':
    main()
