# MechaRAMS / Cheshire YMCA — session preparation tracker

Updated: October 25, 2026

Repository: [FRC999/YMCA-SPIKE-education](https://github.com/FRC999/YMCA-SPIKE-education) (private). Initial upload completed October 25, 2026 using `atsekhan`. This folder is the local Git checkout; later changes require a commit and push.

Project continuity: [new-computer continuation prompt](CONTINUE_HERE.md), [project context](PROJECT_CONTEXT.md), and [maintenance rules/backlog](MAINTENANCE.md). Four core DOCX documents have generated Markdown reading copies; update the Word sources and run the sync script whenever their content changes.

Use the [interactive checklist](SESSION_PREP_CHECKLIST.html) locally to click and save these checkboxes. Follow the [save and GitHub sync instructions](CHECKLIST_INSTRUCTIONS.md). The [eight-class speaker-note index](01_Instructor/Speaker_Notes/README.md) links separate DOCX and Markdown notes for each class.

## Current status and decisions

- [x] Curriculum accepted (reported by Alex).
- [x] Two SPIKE Prime kits are physically available.
- [x] Personal EV3 Home set and a large collection of other LEGO parts are available.
- [x] Demo requirement: an autonomous robot with a memorable sensor-driven response; remote driving alone does not meet the requirement.
- [ ] Inspect and test the two SPIKE kits. Neither is certified complete or working yet.
- [x] Confirm EV3 powers on (Alex, October 23, 2026).
- [ ] Check EV3 motors, infrared sensor, and ability to load/run a program.
- [x] Demo selected by Alex: autonomous EV3 R3PTAR — creep forward, detect a target, hiss and strike, back away, turn, and resume. Build and functional validation remain pending.
- [ ] Confirm actual first-session date, enrollment, devices, and staffing.

The existing curriculum assumes eight students, two kits, and two to four laptops. Six students per kit was discussed as an upper practical limit, not a confirmed enrollment change. Its original proposed October 21 start has passed; replace the proposed calendar once dates are agreed.

Week 1 teaching materials: [detailed slide-by-slide notes and assembly preparation](01_Instructor/W01_Detailed_Speaker_Notes.html) and [presentation with embedded notes](03_Presentations/W01_signal_with_speaker_notes.pptx). Preassemble both SPIKE driving bases before students arrive. The first-session demonstration slot uses about three minutes for R3PTAR and two minutes for the SPIKE starter; the standalone EV3 rehearsal script below remains a five-minute maximum.

## Student trainer preparation session

Two hours confirmed for October 25, 2026. Use the [facilitator plan](01_Instructor/Trainer_Session_Plan.md) and [student trainer work orders](01_Instructor/Trainer_Work_Orders.md). This session begins with assembling and testing the two teaching bases, followed by Week 1 practice and individual teaching rehearsals. It replaces the broad mentor-workshop agenda for today.

- [x] Prepare the two-hour session plan and independent work orders.
- [ ] Conduct the workshop and record the result for each kit.
- [ ] Record each trainer’s operating and teaching practice; assign follow-up where needed.
- [ ] Assign first-session jobs, resolve kit blockers, and confirm storage/charging.

## Next work, in order

1. Label the kits A and B; photograph each open kit before mixing or borrowing parts.
2. Do the electronics inventory below, charge both hubs, and run basic tests.
3. Build the two official practice driving bases. This is the practical test of whether the kits contain enough parts for the course.
4. Record shortages and fill only those gaps from personal parts, using the loan log.
5. Check the EV3 Home electronics and programming setup before investing in the demo build.
6. Build R3PTAR and implement/rehearse the autonomous behavior described below.
7. Rehearse Week 1 with the actual laptops, cables, kits, slides, and room layout.

## SPIKE inventory — check the important parts first

Enter actual counts and test results. A dash means unknown, not missing. Use the printed element overview on the back of the kit's top card for the full small-parts inventory.

| Item | Expected per Prime core kit | Kit A | Kit B | Notes / action |
|---|---:|---|---|---|
| Large hub, with rechargeable battery | 1 | — | — | Label and charge |
| Medium angular motor | 2 | — | — | Test each separately |
| Large angular motor | 1 | — | — | Test separately |
| Distance sensor | 1 | — | — | Needed for parking lessons |
| Color sensor | 1 | — | — | Needed for marker lessons |
| Force sensor | 1 | — | — | Inventory/test; not essential to current lesson sequence |
| USB data cable compatible with hub | 1 | — | — | A charge-only cable is insufficient |
| Matched wheels and tires for teaching base | 1 pair | — | — | Check tire condition and free rotation |
| Required beams, frames, pins, axles, gears and caster parts | Per base instructions | — | — | Build the base to identify actual shortages |
| Sorting trays, box and inventory card | Check present | — | — | Organization rather than robot functionality |

- [ ] Look beneath trays for large pieces before declaring them missing.
- [ ] Separate spare elements from required inventory; do not assume every loose piece belongs to that kit.
- [ ] Check plugs, integral cables, axle holes, tires and battery area for visible damage.
- [ ] Count the remaining small elements only after checking course readiness.

A kit can be ready for this curriculum without every optional decorative part. Record both “course ready” and “full inventory complete” separately.

## Functional checks — both SPIKE kits

Start with the current SPIKE app on an actual teaching device. Use its guided component tests/examples as needed.

- [ ] Hub A: charges, powers on, connects, downloads and runs a program.
- [ ] Hub B: charges, powers on, connects, downloads and runs a program.
- [ ] Check all three motors individually for commanded motion and abnormal binding/noise.
- [ ] Check distance readings change when a flat target approaches and retreats.
- [ ] Check color/reflection readings on the actual light surface and dark marker tape.
- [ ] Check force sensor reports released and pressed states.
- [ ] Use a known-working component to check each hub port where practical.
- [ ] Run both hubs untethered through a rehearsal; record battery behavior.
- [ ] Name hubs distinctly in the app and match physical labels to avoid connecting to the wrong robot.

Existing diagnostic files:

- [Motor smoke test](04_Python/00_mentor_smoke_test.py): tests the paired A/B drive motors; initially raise the wheels clear of the surface. It does not test all motors, sensors, or ports.
- [Sensor readings](04_Python/00_sensor_readings.py): choose distance on C or reflection on D; repeat for both sensor modes and both kits. It does not test the force sensor.
- [Code guide](04_Python/Code_Guide.html): setup and limitations.
- [Official practice driving base instructions](06_References/LEGO_Practice_Driving_Base.pdf).

Course wiring: A = left drive motor, B = right drive motor, C = distance sensor, D = color sensor. Follow the instructor guide for mounts. The base's extra motor is not electrically used by the current course programs. Check forward motion with a short command before running a course.

| Acceptance record | Kit A | Kit B |
|---|---|---|
| Electronics counted / date | — | — |
| Electronics tested / date | — | — |
| Teaching base assembled | — | — |
| Week 1 program rehearsed | — | — |
| Parking and marker programs rehearsed | — | — |
| Battery rehearsal passed | — | — |
| Course ready / remaining blocker | — | — |
| Full inventory complete / shortages | — | — |

## First-session wow demo — selected: autonomous R3PTAR

**Goal:** A moving snake that creeps forward, detects a target, hisses and strikes, then backs away, turns, and resumes. Alex approved this autonomous demonstration on October 23, 2026. The instructor starts the program once; subsequent movement and reactions follow the program.

**Recommended build:** LEGO EV3 Home R3PTAR. Its snake shape and moving fang mechanism make the reaction visible from across a small classroom. The Home set includes an infrared sensor; use its proximity mode. Keep both SPIKE hubs and teaching bases available for students.

**Proposed behavior to implement and test** (a custom presentation sequence, not a claim that a downloaded program already does all of this):

1. CREEP: move forward slowly in short, bounded increments, checking infrared proximity between increments. Limit the total demonstration duration so it cannot roam indefinitely.
2. NOTICE: when a large cardboard target enters the calibrated detection zone, stop forward motion, show an alert expression, and play a short hiss.
3. STRIKE: perform one bounded fang/head action using the model's mechanism, then retract to its starting position.
4. RETREAT / TURN / REARM: back away a short tested distance, make a bounded turn, and resume creeping only when the target is clear. If still blocked, remain stopped. Require clearance and a short cooldown before another strike.
5. STOP: the mentor can immediately stop the program using the brick controls.

Implement this in whichever EV3 programming environment proves functional on the available computer. Do not translate the SPIKE Python files by changing imports. The precise motor ports, motion amounts, sensor threshold and reset behavior must be established from the build and bench tests.

### EV3 readiness gate

- [ ] Find EV3 brick, battery supply, USB cable, motor/sensor cables, two large motors, medium motor, and infrared sensor.
- [x] EV3 powered on successfully (Alex, October 23, 2026). Sustained battery operation remains to be tested.
- [ ] Inspect the battery compartment and confirm battery condition before the demo rehearsal.
- [ ] Test each motor and the infrared sensor, using the brick's built-in tools where available.
- [x] Located legacy LEGO MINDSTORMS EV3 Home Edition on this Windows computer (October 23, 2026): `C:\Program Files (x86)\LEGO Software\LEGO MINDSTORMS EV3 Home Edition\MindstormsEV3.exe`. Installed executable and registry entries confirmed; successful launch and brick connection remain untested.
- [ ] Prove a small program can be transferred and run untethered before the full build.
- [ ] Compare available mechanical parts with R3PTAR instructions; log borrowed substitutions.
- [ ] Assemble and test the fang mechanism at a gentle speed before adding the full reaction sequence.

### Demo acceptance criteria

- [ ] Starts from a repeatable physical position without manually forcing a motor.
- [ ] Detects the chosen cardboard target reliably in the actual room lighting.
- [ ] Creeps predictably with no target; stops and reacts when the target enters the intended zone.
- [ ] Gives one strike per encounter, retracts fully, backs away and turns reliably, and rearms only after clearance.
- [ ] Completes five consecutive approach/withdrawal cycles without a jam or manual reset.
- [ ] Restarts successfully after switching the brick off and on.
- [ ] Runs from battery with no remote or laptop commands during the demonstration.
- [ ] Mentor can stop it immediately; children and fingers remain outside the moving mechanism.
- [ ] Rehearsed in a clear floor area with room for forward motion, retreat and turning. Mentor stops/resets it before it leaves the area; floor tape is a visual boundary, not a boundary the robot detects.
- [ ] Total run duration is bounded and tested; it stops at the limit even if no target is detected.

### Five-minute presentation

Use the existing Week 1 demonstration slot after the brief baseline activity.

- 0:00–0:30: Introduce the snake and ask what would make a machine “notice” something.
- 0:30–1:30: Bring in the cardboard target; let the autonomous reaction happen.
- 1:30–2:30: Have a student predict what happens when the target stays near, then moves away and returns.
- 2:30–3:30: Repeat to show the rule is consistent. Let a student move the target with mentor supervision if the space permits.
- 3:30–4:30: Point to sensor → program decision → motor action. Explain that the snake is following a rule rather than thinking.
- 4:30–5:00: Connect to the SPIKE kits: the same input/decision/output idea, starting with simpler programs today.

### Alternatives if R3PTAR cannot be made reliable

- **EV3 GRIPP3R:** an autonomous pickup-and-delivery performance: detect a presented object, close the gripper, execute a short bounded transport, and release at a marked destination. Requires its own tested program and a repeatable setup; remote driving does not satisfy the demo requirement.
- **SPIKE creature:** removable decorative head and a sensor-triggered greeting/retreat sequence on one teaching base. Use only if the EV3 is unavailable, and restore the teaching setup before student work. A separate elaborate SPIKE build would consume one of the two teaching hubs.

Personal mechanical parts can enhance appearance, but they do not supply a third programmable hub. Reliability and a visible autonomous response take priority over adding mechanisms.

## Personal-parts loan log

Keep personal EV3 equipment together as a separately labeled demo kit. For loose parts borrowed into teaching kits, photograph and log them before use. Use removable identification on a non-contact surface; keep markings and tape off gears, axle fits, connector holes, electrical contacts and sensor optics. For tiny parts that cannot be marked reliably, use counted bags and build photos.

| Date | Owner | Part description / color / size | Quantity | Mark or photo reference | Destination kit/build | Returned quantity / date |
|---|---|---|---:|---|---|---|
| — | Alex | — | — | — | — | — |

- [ ] Photograph completed bases and the demo from several sides.
- [ ] Keep an empty labeled return bag with each kit.
- [ ] Reconcile personal parts when changing builds and after the final session.

## Gotchas to keep visible

- SPIKE and EV3 mechanical Technic parts can often be combined, but their electronics use different connectors and programming systems. Do not plug EV3 motors/sensors into SPIKE hubs.
- EV3 Home has an infrared sensor; do not assume an Education-set ultrasonic sensor or gyro is available.
- EV3 infrared proximity is a relative reading, not the SPIKE distance sensor's millimeter value. Calibrate it using the actual target and lighting.
- Older SPIKE examples using `from spike import PrimeHub` belong to the older API. The supplied curriculum files target SPIKE App 3.
- Building instructions alone do not establish that a program will work with the installed software. Prove the download/run workflow early.
- An official SPIKE element-overview link inspected during preparation led to the **45681 expansion** inventory. Check that an inventory is for **45678 Prime core**, or use the kit's printed card.
- Motors and sensors can be present but faulty; counting alone is insufficient.
- Dark tape, floor color, sensor mounting height, wheel traction and low batteries can change physical behavior. Rehearse on the actual course materials.
- Classroom Wi-Fi should not be a dependency for the live demo. Save required files and prove the robot runs untethered beforehand.
- The demo should leave enough time for students to use the robots themselves. Keep it to the existing five-minute slot.

## Backlog / open decisions

### Before the first session

- [ ] Confirm dates, headcount, room, adult lead and teen mentors.
- [ ] Confirm student laptop count, permissions, installed app, cables and charging access.
- [ ] If enrollment differs from eight, revise group roles and station rotations before printing.
- [ ] Finish kit acceptance records and missing-parts list.
- [x] Choose R3PTAR and the autonomous moving demonstration.
- [ ] Confirm the installed EV3 Home Edition launches and connects to the brick.
- [ ] Build, program and rehearse the autonomous demo.
- [ ] Prepare tape, cardboard target, student materials, name labels and transport boxes.
- [ ] Assign one mentor to demo setup/reset and one to preparing student stations.
- [ ] Rehearse the complete first hour, including packing and cleanup.

### During the course

- [ ] Log battery or connection failures and damaged/missing parts after each session.
- [ ] Record what students actually completed and adjust the next lesson's starting point.
- [ ] Capture attendance and learning evidence using the existing evaluation forms.
- [ ] Track personal parts whenever a build changes.

### Later improvements

- [ ] Finish the full element-by-element inventory if not needed for initial readiness.
- [ ] Make a reusable demo setup card with tested ports, settings, target distance and reset steps.
- [ ] Consider a more complex autonomous demonstration after the first one is reliable.
- [ ] Reconcile and return personal parts at program close.

## Change log

| Date | Update |
|---|---|
| 2026-10-25 | Added separate detailed DOCX/Markdown speaker notes for all eight classes and a local interactive prep checklist with save/pull/push instructions. Physical readiness results remain unchanged. |
| 2026-10-25 | Added four DOCX/Markdown pairs, generator/checker and CI, maintenance backlog, repository AI instructions, project context, skill, and new-computer continuation prompt. Physical readiness statuses remain unchanged. |
| 2026-10-25 | Added the two-hour trainer session plan and student-led work orders. First task: assemble and test both SPIKE bases. Blank kit and trainer records distinguish the planned session from completed checks. |
| 2026-10-25 | Confirmed the first-session preassembly plan; added detailed notes for all seven Week 1 slides, a printable companion, and a revised presentation preserving the original. Hardware assembly and testing remain pending. |
| 2026-10-25 | Created private FRC999/YMCA-SPIKE-education repository using atsekhan and uploaded curriculum, references, and prep tracker; added README and excluded temporary build/preview files. |
| 2026-10-23 | Alex approved autonomous moving R3PTAR: creep, detect, hiss/strike, retreat, turn, resume. EV3 power-on passed; EV3 Home Edition installation located, launch/connection untested. |
| 2026-10-23 | Curriculum accepted; moved to physical kit preparation. Two SPIKE kits available. EV3 Home and personal parts confirmed. Autonomous wow demo required. R3PTAR recommended, pending hardware/software check. |

## Official resources

- [SPIKE preparation and inventory guidance](https://education.lego.com/en-us/teacher-resources/lego-education-spike-prime/start-here/lego-education-spike-prime-start-here-prepare-to-teach/)
- [SPIKE app download](https://education.lego.com/en-us/downloads/spike-app/software/)
- [SPIKE Prime building instructions](https://education.lego.com/en-us/product-resources/spike-prime/downloads/building-instructions/)
- [EV3 Home 31313 set information](https://www.lego.com/en-us/product/lego-mindstorms-ev3-31313)
- [EV3 31313 building-instruction selection](https://www.lego.com/en-us/service/building-instructions/31313)
- [Official R3PTAR build instructions (PDF)](https://www.lego.com/cdn/cs/set/assets/bltfa9d17de847b8936/31313_R3PTAR_2016.pdf)
- [EV3 user guide, including infrared proximity mode (PDF)](https://www.lego.com/cdn/cs/set/assets/bltbef4d6ce0f40363c/LMSUser_Guide_LEGO_MINDSTORMS_EV3_11_Tablet_ENUS.pdf)

EV3 power-on is confirmed. Remaining physical inventory, builds and functional tests are pending until performed and recorded. This tracker distinguishes planned behavior from verified results.






