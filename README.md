# MechaRAMS YMCA SPIKE Education

An eight-session LEGO SPIKE Prime robotics course for grades 7–8 at the Cheshire YMCA, led by MechaRAMS high-school mentors with adult supervision.

## Continue on another computer

Open [CONTINUE_HERE.md](CONTINUE_HERE.md) for clone/setup instructions and a copy-and-paste prompt for a new Codex chat. The repository carries [project context](PROJECT_CONTEXT.md), [AI instructions](AGENTS.md), a [project-local skill](.agents/skills/ymca-spike-maintenance/SKILL.md), and a [maintenance backlog](MAINTENANCE.md). Keep those files current as decisions and actual test results change.

## Trainer session

For the two-hour, student-led preparation session, use the [facilitator plan](01_Instructor/Trainer_Session_Plan.md) and give each kit group the [student trainer work orders](01_Instructor/Trainer_Work_Orders.md). Start by assembling and testing both SPIKE bases, then rehearse Week 1 and practice teaching. The work orders include all build/program links and blank readiness records.

## Start here

- [Session preparation tracker](SESSION_PREP.md): current decisions, kit inventory, hardware checks, autonomous EV3 R3PTAR demo, borrowed parts, and backlog.
- [Week 1 presentation with detailed speaker notes](03_Presentations/W01_signal_with_speaker_notes.pptx)
- [Week 1 printable speaker notes and assembly preparation](01_Instructor/W01_Detailed_Speaker_Notes.html)
- [SPIKE teaching-base assembly instructions](06_References/LEGO_Practice_Driving_Base.pdf)
- [Program proposal and resources](00_Start_Here/Program_Proposal_and_Resources.md) · [Word download](00_Start_Here/Program_Proposal_and_Resources.docx)
- [Instructor and mentor guide](01_Instructor/Instructor_and_Mentor_Guide.md) · [Word download](01_Instructor/Instructor_and_Mentor_Guide.docx)
- [Student workbook](02_Student/Student_Workbook.md) · [Word download](02_Student/Student_Workbook.docx)
- [Evaluation and partner forms](05_Evaluation/Evaluation_and_Partner_Forms.md) · [Word download](05_Evaluation/Evaluation_and_Partner_Forms.docx)

The four core documents are readable directly on GitHub as Markdown, with matching Word downloads for printing and editing. Download or clone this repository and open `START_HERE.html` locally for a linked index of all materials. GitHub displays HTML source rather than the rendered teaching pages; open the HTML companions locally. PowerPoint files include speaker notes.

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

Follow [MAINTENANCE.md](MAINTENANCE.md). Update DOCX sources first, then regenerate their Markdown mirrors:

```sh
python scripts/sync_documents.py --write
python scripts/sync_documents.py --check
python -m unittest discover -s tests -v
```

The script needs Python 3.10+ and no extra packages. The [Document sync check](https://github.com/FRC999/YMCA-SPIKE-education/actions/workflows/document-sync.yml) runs on pushes and pull requests and flags missing or stale mirrors. It does not automatically rewrite files.

Update `SESSION_PREP.md` with actual operational results and `PROJECT_CONTEXT.md` with material decisions and the next handoff. Commit and push all completed project updates, as requested by Alex. There is no background sync of an uncommitted local folder.

Temporary rendering output and build caches in `.build/` are intentionally excluded. The local distribution ZIP is also excluded because its contents are already represented by individual files here.

LEGO and FIRST reference materials retain their owners' rights. Their inclusion does not grant a new license to those materials. This is an independent MechaRAMS teaching resource; no blanket license has been assigned to the repository.

