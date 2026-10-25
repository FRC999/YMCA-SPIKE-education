# MechaRAMS YMCA SPIKE Education

An eight-session LEGO SPIKE Prime robotics course for grades 7–8 at the Cheshire YMCA, led by MechaRAMS high-school mentors with adult supervision.

## Trainer session

For the two-hour, student-led preparation session, use the [facilitator plan](01_Instructor/Trainer_Session_Plan.md) and give each kit group the [student trainer work orders](01_Instructor/Trainer_Work_Orders.md). Start by assembling and testing both SPIKE bases, then rehearse Week 1 and practice teaching. The work orders include all build/program links and blank readiness records.

## Start here

- [Session preparation tracker](SESSION_PREP.md): current decisions, kit inventory, hardware checks, autonomous EV3 R3PTAR demo, borrowed parts, and backlog.
- [Week 1 presentation with detailed speaker notes](03_Presentations/W01_signal_with_speaker_notes.pptx)
- [Week 1 printable speaker notes and assembly preparation](01_Instructor/W01_Detailed_Speaker_Notes.html)
- [SPIKE teaching-base assembly instructions](06_References/LEGO_Practice_Driving_Base.pdf)
- [Program proposal and resources](00_Start_Here/Program_Proposal_and_Resources.docx)
- [Instructor and mentor guide](01_Instructor/Instructor_and_Mentor_Guide.docx)
- [Student workbook](02_Student/Student_Workbook.docx)
- [Evaluation and partner forms](05_Evaluation/Evaluation_and_Partner_Forms.docx)

Download or clone this repository and open `START_HERE.html` locally for a linked index of all materials. GitHub displays HTML source rather than the rendered teaching pages. Word and PowerPoint files can be downloaded and edited in their respective applications.

## Contents

| Folder | Materials |
|---|---|
| `00_Start_Here` | Program proposal |
| `01_Instructor` | Detailed instructor and mentor guide |
| `02_Student` | Workbook and printable station task cards |
| `03_Presentations` | Proposal, mentor workshop, and eight weekly slide decks |
| `04_Python` | Eight lesson programs, two diagnostics, and code guide |
| `05_Evaluation` | Evaluation and partner forms |
| `06_References` | Research sources and official LEGO practice driving-base instructions |

## Course sequence

1. Signals and instruction order
2. Delivery and distance calibration
3. Dance and counted loops
4. Parking with distance sensing
5. Detecting a floor marker
6. Building a rescue attachment
7. Community robot mission
8. Showcase and reflection

The baseline plan uses two SPIKE Prime kits, eight students, and eight one-hour sessions. Dates, final enrollment, devices, and staffing still need confirmation. The original proposal calendar is provisional; consult the preparation tracker for current status.

## Hardware and programming

The lesson programs target **SPIKE App 3 Python**, using its `hub`, `motor_pair`, and `runloop` APIs. They are intended to be transferred to SPIKE Prime hubs, not executed as ordinary desktop Python programs. See [the code guide](04_Python/Code_Guide.html).

The separate first-session demonstration uses **EV3 Home R3PTAR** with a planned autonomous creep → detect → hiss/strike → retreat → turn sequence. EV3 power-on has been confirmed and EV3 Home Edition software located. Motor/sensor tests, software connection, assembly, and demonstration programming remain to be completed.

Offline checks of the teaching programs and document layouts were completed during preparation. Physical behavior must still be rehearsed on both actual SPIKE kits. No EV3 demo program is included yet.

## Maintaining this repository

Update `SESSION_PREP.md` as checks are completed, decisions change, or issues are found. Commit and push changes to share them with the team. This initial upload is a point-in-time sync; ongoing automatic synchronization is not configured.

Temporary rendering output and build caches in `.build/` are intentionally excluded. The local distribution ZIP is also excluded because its contents are already represented by individual files here.

LEGO and FIRST reference materials retain their owners' rights. Their inclusion does not grant a new license to those materials. This is an independent MechaRAMS teaching resource; no blanket license has been assigned to the repository.

