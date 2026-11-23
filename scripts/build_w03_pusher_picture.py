"""Render the centered cone pusher assembly reference."""

from math import atan2, cos, pi, sin
from pathlib import Path

import reportlab
from PIL import Image, ImageDraw, ImageFont

PRINTS = Path(__file__).resolve().parents[1] / '02_Student' / 'Printouts'
INK = '#142939'
TEAL = '#15665F'
ORANGE = '#9C4618'
GRAY = '#526572'
GRID = '#DEE6EA'


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

    label(54, 39, 'MECHARAMS  /  CONE PUSHER ASSEMBLY', 22, TEAL, True)
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
    make_picture()
