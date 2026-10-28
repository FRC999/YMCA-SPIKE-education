# Project context for continuing this work

Last reviewed: October 27, 2026. This is a curated handoff of the project’s decisions and known state, not a full chat transcript. Read the current [preparation tracker](SESSION_PREP.md) for subsequent results and corrections.

## Purpose and people

Alex is preparing a Cheshire, Connecticut YMCA robotics program with MechaRAMS / FRC Team 999. The audience is confirmed as 12 children in grades 5–6. High-school juniors and seniors will teach under an adult educator. The program should provide useful community learning and a voluntary path toward future high-school robotics participation. Evidence may support team outreach/award narratives, but no learning gains, recruitment outcomes, or award eligibility are assumed.

The curriculum was originally prepared as a proposal and Alex reported it accepted on October 23, 2026. On October 27 Alex reported that the first session went very well, the children stayed engaged and the activities fitted the hour. The group seemed more advanced than expected and asked how fast the robot could run. The current phase is preparing the remaining sessions; no detailed kit acceptance results or later dates were supplied with that report.

## Accepted course design

- Eight weekly sessions, one hour each, using two existing SPIKE Prime kits.
- Confirmed October 25: 12 children in four teams of three, two teams per kit, 4–6 student instructors and an adult lead. Four laptops are available; bring two for robot control and two for build references. Dates and local assignments remain open.
- Alex confirmed the first class is October 27, 2026 ("today"). The original proposal's October 21 start is superseded; later dates remain unconfirmed. Use the [complete readiness guide](01_Instructor/Class_Preparation/W01_Readiness_Guide.md) and its four-page PDF; the linked 16-page class packet contains exact copy quantities.
- Start with scaffolded real Python in SPIKE App 3. Students edit a small `student_recipe` in a complete supplied program. This is not drag-and-drop Python, desktop Python, Pybricks, or the older `from spike import PrimeHub` API. A mentor-tested Word Blocks fallback can preserve the learning goal.
- Weeks: signals/sequence; delivery/calibration; dance/loops; distance-based parking; dark-marker sensing; passive rescue attachment/functions; chosen community mission; showcase/reflection.
- After Week 1: keep Weeks 2–6 in order and offer readiness-based extensions. The [remaining-sessions plan](01_Instructor/Remaining_Sessions_Plan.md) adds a complete optional Week 7 timed delivery challenge: fixed 60 cm course, removable cargo cradle, repeated stopwatch trials and controlled speed/design comparisons. It replaces the original Week 7 mission if selected and physically rehearsed. Week 8 uses the saved result within its existing schedule. Do not compress the course based only on a successful first class.
- Keep both official practice driving bases assembled. Use the same base throughout the course; students build removable attachments or course models every week.

## Hardware and programming decisions

Alex has both SPIKE kits physically available, an EV3 Home set, and many personal LEGO parts. Personal parts may supplement builds if logged and identifiable for return. Working electronics and enough parts for the teaching bases come before counting every small element.

Course wiring overrides the official PDF if different: left wheel motor A, right wheel motor B, viewed from behind toward the labeled front. The auxiliary motor can remain mechanically installed but electrically unplugged. Distance sensor C and downward color sensor D are introduced later; neither is needed for the Week 1 recipe.

The supplied programs have offline syntax/mock-logic checks from initial preparation. Physical operation on the two actual SPIKE kits is still unreported. Do not equate a passing software check with a bench test. Wheel degrees are not centimeters or robot heading degrees. Sensor thresholds and physical mounts need calibration.

## Separate first-session demonstration

Alex specifically wants something exciting and autonomous, not a robot merely driven by remote. The selected model is EV3 Home **R3PTAR**. Approved behavior: creep forward, detect a cardboard target, hiss and strike, retract, back away, turn, and resume when clear. Use bounded movement and a finite run duration; a taped boundary does not make the robot sense an edge. Keep both SPIKE bases available to learners.

Confirmed October 23: the EV3 powered on. Legacy LEGO MINDSTORMS EV3 Home Edition was found on the original Windows computer. On October 26 Alex reported assembly complete, supplied screenshots showing the finished R3PTAR 03 program, reported no download errors, and confirmed the snake moved. Full infrared/strike/retreat response, untethered restart after power-off and demo acceptance remain unverified. Installed Mission 3 (Hunting) uses A steering, B drive, D strike and infrared 4. See [connection and first-run instructions](01_Instructor/R3PTAR_Setup_and_First_Run.md). The factory program uses an unlimited loop; classroom speed/timing adaptation and acceptance testing are still required. The October 27 guide distinguishes a brief continuously supervised manually stopped demonstration from the still-unverified automatic duration limit. A new computer needs its own software/device setup; the old installation does not travel with Git.

EV3 Home uses an infrared sensor; do not assume an Education-set ultrasonic sensor or gyro. EV3 and SPIKE electronics are not directly interchangeable, although many mechanical Technic pieces can be shared.

## First-session teaching plan

October 27 correction from Alex: children already answered prior-experience questions. Begin with welcome, curiosity and a robot demonstration, without a technical quiz or a request to admit what they do not know. The old baseline is retired. Record learning through dated work, mentor observations and final explanations; do not claim pre/post score gains without a concept baseline.

Both SPIKE bases should be assembled and tested before children arrive. The official build PDF is in `06_References/LEGO_Practice_Driving_Base.pdf` (37 pages, steps 1–34).

Use `03_Presentations/W01_signal_with_speaker_notes.pptx` as the current Week 1 deck and `01_Instructor/Speaker_Notes/W01_signal_Speaker_Notes.md` as its browser-readable companion. Both Week 1 PPTX filenames now contain the same revised six-slide deck with detailed notes. Read the PDF directly on GitHub.

The hour is 0–5 welcome and introductions; 5–10 demonstration (about three minutes EV3 and two SPIKE); 10–14 combined code/prediction; 14–26 first robot/build rotation; 26–38 switch; 38–44 T1/T3 retest; 44–50 T2/T4 retest; 50–54 reflection; 54–60 save/reset. Rotate three jobs every four minutes in the initial turns and every two in retests. There is no opening quiz, ability rating or repeated prior-experience survey. Mentors notice support needs during coached activities. Week 8 has its own showcase schedule.

The slide prompt “move the last line to the top” differs from the paper task “swap first and last.” Keep the intended operation clear. For the original signal/pause/drive recipe, the former gives drive/signal/pause; the latter gives drive/pause/signal.

## Separate class notes and prep checklist

All eight classes now have separate detailed DOCX and generated Markdown speaker notes in [01_Instructor/Speaker_Notes](01_Instructor/Speaker_Notes/README.md), with one preparation page and one page per slide. All notes now follow the six-slide decks and revised teams, roles and build activities. Week 8 has its own assessment/rehearsal/showcase schedule. Future edits must keep affected documents, slides, programs and reading copies aligned.

Alex initially requested clickable prep checkmarks. On October 25 he clarified a preference for Markdown and questioned the need for local HTML or cloning on teaching PCs. The local HTML checkbox editor and duplicate HTML references were retired. [SESSION_PREP.md](SESSION_PREP.md) remains the sole preparation record, with every existing checkbox and result preserved. Authorized collaborators can edit `[ ]`/`[x]` directly on GitHub; [instructions](CHECKLIST_INSTRUCTIONS.md) explain the workflow. Teaching PCs read GitHub and download the needed class files; cloning is optional for curriculum maintenance with Codex.

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

1. Prepare and rehearse Week 2 delivery and its cargo-tray build on both kits. Use the existing checklist and notes, with optional stretches from the remaining-sessions plan.
2. Record actual kit issues or acceptance results as reported. First-session success does not establish later sensor calibration, full inventory or unreported EV3 behavior.
3. Rehearse the later sensor lessons in advance. For the optional Week 7 speed lesson, confirm floor space and calibrate each kit's fixed travel and approved speeds. Its shipped program refuses motion until the mentor configures travel.
4. Confirm later class dates and mentor assignments locally. Enrollment, age group, available mentors and four laptops are settled. Preserve the successful hour and three-role rotations.

Do not repeat settled design questions or redesign the course merely because this is a new chat. If the user gives a different immediate task, follow it and preserve these decisions unless explicitly changed.
