# Project context for continuing this work

Last reviewed: October 25, 2026. This is a curated handoff of the project’s decisions and known state, not a full chat transcript. Read the current [preparation tracker](SESSION_PREP.md) for subsequent results and corrections.

## Purpose and people

Alex is preparing a Cheshire, Connecticut YMCA robotics program with MechaRAMS / FRC Team 999. The audience is confirmed as 12 children in grades 5–6. High-school juniors and seniors will teach under an adult educator. The program should provide useful community learning and a voluntary path toward future high-school robotics participation. Evidence may support team outreach/award narratives, but no learning gains, recruitment outcomes, or award eligibility are assumed.

The curriculum was originally prepared as a proposal and Alex reported it accepted on October 23, 2026. The current phase is preparing equipment and student trainers for the first session.

## Accepted course design

- Eight weekly sessions, one hour each, using two existing SPIKE Prime kits.
- Confirmed October 25: 12 children in four teams of three, two teams per kit, 4–6 student instructors and an adult lead. Four laptops are available; bring two for robot control and two for build references. Dates and local assignments remain open.
- The original proposal included an October 21 start and November/December dates. Those are illustrative, not booked dates; the start has passed. Confirm the actual calendar before revising it.
- Start with scaffolded real Python in SPIKE App 3. Students edit a small `student_recipe` in a complete supplied program. This is not drag-and-drop Python, desktop Python, Pybricks, or the older `from spike import PrimeHub` API. A mentor-tested Word Blocks fallback can preserve the learning goal.
- Weeks: signals/sequence; delivery/calibration; dance/loops; distance-based parking; dark-marker sensing; passive rescue attachment/functions; chosen community mission; showcase/reflection.
- Keep both official practice driving bases assembled. Use the same base throughout the course; students build removable attachments or course models every week.

## Hardware and programming decisions

Alex has both SPIKE kits physically available, an EV3 Home set, and many personal LEGO parts. Personal parts may supplement builds if logged and identifiable for return. Working electronics and enough parts for the teaching bases come before counting every small element.

Course wiring overrides the official PDF if different: left wheel motor A, right wheel motor B, viewed from behind toward the labeled front. The auxiliary motor can remain mechanically installed but electrically unplugged. Distance sensor C and downward color sensor D are introduced later; neither is needed for the Week 1 recipe.

The supplied programs have offline syntax/mock-logic checks from initial preparation. Physical operation on the two actual SPIKE kits is still unreported. Do not equate a passing software check with a bench test. Wheel degrees are not centimeters or robot heading degrees. Sensor thresholds and physical mounts need calibration.

## Separate first-session demonstration

Alex specifically wants something exciting and autonomous, not a robot merely driven by remote. The selected model is EV3 Home **R3PTAR**. Approved behavior: creep forward, detect a cardboard target, hiss and strike, retract, back away, turn, and resume when clear. Use bounded movement and a finite run duration; a taped boundary does not make the robot sense an edge. Keep both SPIKE bases available to learners.

Confirmed October 23: the EV3 powered on. Legacy LEGO MINDSTORMS EV3 Home Edition was found on the original Windows computer. Successful software launch/brick connection, motor/IR checks, assembly, and a reliable demo program have not been reported. A new computer needs its own software/device setup; the old installation does not travel with Git.

EV3 Home uses an infrared sensor; do not assume an Education-set ultrasonic sensor or gyro. EV3 and SPIKE electronics are not directly interchangeable, although many mechanical Technic pieces can be shared.

## First-session teaching plan

Both SPIKE bases should be assembled and tested before children arrive. The official build PDF is in `06_References/LEGO_Practice_Driving_Base.pdf` (37 pages, steps 1–34).

Use `03_Presentations/W01_signal_with_speaker_notes.pptx` as the current Week 1 deck and `01_Instructor/W01_Detailed_Speaker_Notes.html` as its printable companion. Both Week 1 PPTX filenames now contain the same revised six-slide deck with detailed notes. Read the PDF directly on GitHub.

The hour is 0–5 baseline/welcome; 5–10 demonstration (about three minutes EV3 and two SPIKE); 10–14 combined code/prediction; 14–26 first robot/build rotation; 26–38 switch; 38–44 T1/T3 retest; 44–50 T2/T4 retest; 50–54 reflection; 54–60 save/reset. Rotate three jobs every four minutes in the initial turns and every two in retests. The baseline comes before coaching. Week 8 has its own showcase schedule.

The slide prompt “move the last line to the top” differs from the paper task “swap first and last.” Keep the intended operation clear. For the original signal/pause/drive recipe, the former gives drive/signal/pause; the latter gives drive/pause/signal.

## Separate class notes and prep checklist

All eight classes now have separate detailed DOCX and generated Markdown speaker notes in [01_Instructor/Speaker_Notes](01_Instructor/Speaker_Notes/README.md), with one preparation page and one page per slide. All notes now follow the six-slide decks and revised teams, roles and build activities. Week 8 has its own assessment/rehearsal/showcase schedule. Future edits must keep affected documents, slides, programs and Week 1 HTML aligned.

Alex requested clickable prep checkmarks and instructions for use on another laptop. The local [checklist page](SESSION_PREP_CHECKLIST.html) opens and saves the actual prep Markdown; [instructions](CHECKLIST_INSTRUCTIONS.md) cover cloning, pulling, opening, saving, reviewing and pushing. GitHub also permits editing the `[ ]`/`[x]` source directly. There is no automatic sync or independent status database. No physical readiness check was completed by creating these tools.

## Student trainer session

Alex requested a student-driven train-the-trainer session for October 25 and confirmed about two hours. First task: assemble and test the two teaching bases. The facilitator gives work orders and checks progress rather than lecturing throughout.

Current files: `01_Instructor/Trainer_Session_Plan.md` and `01_Instructor/Trainer_Work_Orders.md`. Their agenda supersedes the broader original mentor workshop for this preparation session: 0–5 brief; 5–45 build; 45–65 test; 65–80 recipe practice; 80–90 read/prepare; 90–110 teach-back; 110–120 readiness/handoff. It has a late-build recovery schedule and blank individual/kit records. Do not mark the workshop or tests complete until Alex supplies results.

## October 25 instructional revision

Confirmed: 12 children in grades 5–6, 4–6 student instructors, two SPIKE kits and four available laptops. Use four triads, two robot stations and two build tables. See Grouping_and_Roles.md for the explicit driver, navigator/handler and observer jobs, build roles and timings. Bring four laptops; two only display build references. Students build a mascot, tray, dancer, garage, marker road, rescue guide, mission scene and final exhibit. Prepare two mentor samples for teams that use robots before building. Keep predictions and brief results at the robot.

All eight decks combine the old slides 3/4 and use new learning/observation prompts on the final slide. Markdown and PDF copies enable GitHub reading. Per-session checklists give exact print and bring quantities for 12 children. Hardware and inventory checks remain open until observed or reported. The repository is now public at Alex’s explicit request; blank forms are public but completed student records must stay private.

## Repository and continuity

Public repository (read access requested and verified October 25): [FRC999/YMCA-SPIKE-education](https://github.com/FRC999/YMCA-SPIKE-education). Account `atsekhan` had administrator access when the repository was created. Verify authentication on the current computer rather than copying credentials.

The original working folder was `S:/Projects/MechaRAMS-YMCA-Robotics-Fall-2026`; a new clone may live anywhere. This is separate from the competition robot-code repository. Temporary build/render files were excluded intentionally and are not portable source dependencies. Edit the existing artifacts with appropriate tools; do not assume the old `.build` generators exist on another PC.

A Windows Git certificate issue on the original machine was resolved by setting that checkout’s `http.sslBackend` to `schannel`. This is a machine-specific troubleshooting fact, not a setting to apply on every computer. Do not disable certificate validation.

Alex explicitly requested GitHub sync after all project changes, Markdown copies matching DOCX, a maintained backlog/rules file, and a portable AI handoff with a continuation prompt. See [MAINTENANCE.md](MAINTENANCE.md), [AGENTS.md](AGENTS.md), and [CONTINUE_HERE.md](CONTINUE_HERE.md).

## Next useful work

1. Obtain actual results from the trainer session: kit completion, shortages, connectivity, trainer readiness, and remaining owners/tasks. Update the tracker with dated evidence.
2. Finish any outstanding SPIKE tests and first-session rehearsal.
3. Complete EV3 connectivity, motor/IR checks, R3PTAR build, program, and repeated autonomous tests.
4. Confirm first-session dates and local assignments. Enrollment, age group, available mentors and four laptops are settled.

Do not repeat settled design questions or redesign the course merely because this is a new chat. If the user gives a different immediate task, follow it and preserve these decisions unless explicitly changed.
