"""Assemble the Week 4 and Week 5 print packets without scaling source pages."""

from dataclasses import dataclass
from io import BytesIO
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen.canvas import Canvas

from build_w04_w05_mission_prints import INK, PALE, TEAL, text

ROOT = Path(__file__).resolve().parents[1]
PREP = ROOT / '01_Instructor' / 'Class_Preparation'
PRINTS = ROOT / '02_Student' / 'Printouts'


@dataclass(frozen=True)
class Section:
    label: str
    source: Path
    first: int = 1
    last: int = 1
    copies: int = 1

    @property
    def sheets(self):
        return (self.last - self.first + 1) * self.copies


def print_plan(week):
    if week == 4:
        field = PRINTS / 'W04_Cone_Rematch_Full_Size_Field.pdf'
        return (
            Section('Mentor checklist', PREP / 'W04_cone_rematch_Setup_Checklist.pdf'),
            Section('Field assembly guide', field),
            Section('Kit A field tiles', field, 2, 10),
            Section('Kit B field tiles', field, 2, 10),
            Section('Team cards (4 teams + spare)', PRINTS / 'W04_Cone_Rematch.pdf', 2, 2, 5),
            Section('Attendance', PRINTS / 'Attendance.pdf'),
            Section('Paper cone templates (8 cones)', PRINTS / 'W03_Paper_Cone_Template.pdf', copies=2),
        )
    field = PRINTS / 'W05_Delivery_Strip_Full_Size_Field.pdf'
    return (
        Section('Mentor checklist', PREP / 'W05_sensor_mission_Setup_Checklist.pdf'),
        Section('Lane assembly guide', field),
        Section('Kit A lane tiles and strip', field, 2, 5),
        Section('Kit B lane tiles and strip', field, 2, 5),
        Section('Team cards (4 teams + spare)', PRINTS / 'W05_Sensor_Mission.pdf', copies=5),
        Section('Attendance', PRINTS / 'Attendance.pdf'),
    )


def indexed_sections(plan):
    start = 1
    for section in plan:
        end = start + section.sheets - 1
        yield section, start, end
        start = end + 1


def packet_instructions(index):
    """Add a packet-specific page map below the existing checklist."""
    stream = BytesIO()
    canvas = Canvas(stream, pagesize=letter, invariant=1)
    text(canvas, 448, 753, 'CLASS PRINT PACKET', 9, TEAL, True)
    text(canvas, 251, 663, 'For reference when printing individual files', 9, TEAL)
    canvas.setFillColor(HexColor(PALE))
    canvas.roundRect(36, 54, 540, 100, 6, stroke=0, fill=1)
    text(canvas, 48, 136, f'Print this {index[-1][2]}-page packet once', 13, TEAL, True)
    text(canvas, 48, 119, 'US Letter / Actual Size (100%) / Single-sided / Auto page orientation',
         10, INK)
    for i, (section, first, last) in enumerate(index[1:]):
        x = 48 if i < 3 else 312
        y = 101 - 15 * (i % 3)
        pages = str(first) if first == last else f'{first}-{last}'
        text(canvas, x, y, f'{pages}   {section.label}', 9.6, INK)
    canvas.showPage()
    canvas.save()
    stream.seek(0)
    return PdfReader(stream).pages[0]


def build_packet(week, filename, title):
    plan = print_plan(week)
    index = list(indexed_sections(plan))
    writer = PdfWriter()
    writer.add_metadata({'/Title': title, '/Author': 'MechaRAMS / Cheshire YMCA'})
    writer.create_viewer_preferences()
    writer.viewer_preferences[NameObject('/PrintScaling')] = NameObject('/None')
    writer.viewer_preferences[NameObject('/Duplex')] = NameObject('/Simplex')

    for section, start, _ in index:
        source = PdfReader(section.source)
        if section.last > len(source.pages):
            raise ValueError(f'Page {section.last} is missing from {section.source}')
        for _ in range(section.copies):
            for number in range(section.first, section.last + 1):
                page = writer.add_page(source.pages[number - 1])
                if start == 1:
                    page.merge_page(packet_instructions(index))
        writer.add_outline_item(section.label, start - 1)
    writer.write(PRINTS / filename)


if __name__ == '__main__':
    build_packet(4, 'W04_Class_Print_Packet.pdf', 'Week 4 Cone Rematch Class Print Packet')
    build_packet(5, 'W05_Class_Print_Packet.pdf', 'Week 5 Delivery Strip Class Print Packet')
