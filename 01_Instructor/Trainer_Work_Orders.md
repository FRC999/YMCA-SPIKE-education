# Student trainer work orders

**Today’s assignment:** assemble and test both SPIKE teaching robots, learn the first lesson, and practice teaching it to a partner. Work in the group assigned to Kit A or Kit B. Follow these work orders in sequence and record what you actually observe.

The [facilitator plan](Trainer_Session_Plan.md) contains the schedule and adult checkpoints. Your group should be able to work from this document without waiting for a presentation.

## Open these files now

| You need | File / link | Use it for |
|---|---|---|
| Build instructions | [Official Practice Driving Base PDF](../06_References/LEGO_Practice_Driving_Base.pdf) | Assemble one robot per kit; 37 pages, steps 1–34 |
| Motor test source | [00_mentor_smoke_test.py](../04_Python/00_mentor_smoke_test.py) | First motor check, wheels raised |
| Full Week 1 program | [W01_signal.py](../04_Python/W01_signal.py) | Letter, wait, short move |
| Code setup | [Code Guide](../04_Python/Code_Guide.md) | App, complete file, recipe area, units |
| Lesson instructions | [Week 1 detailed speaker notes](Speaker_Notes/W01_signal_Speaker_Notes.md) | What to say, ask, demonstrate, and do |
| Student slides | [Week 1 deck with notes](../03_Presentations/W01_signal.pdf) | Rehearse the lesson |
| Student materials | [Workbook](../02_Student/Student_Workbook.md) and [Week 1 station card](../02_Student/Station_Task_Cards.md) | Baseline and work away from the robot |

On GitHub, open a Python file and use **Raw** or download the file to copy its plain text. On a training computer, open the downloaded `.py` file in a text editor. HTML guides should be opened locally in a browser; GitHub normally shows their source. The repository is public for reading; use Markdown and PDF links directly, and keep offline copies for the session.

## When you need help

Reread the current step, compare the real robot or code with the source, and ask a partner to check it. If you are still blocked after about three minutes, ask the adult and report the step, expected result, actual result, and what you already tried. For unexpected motion, stop immediately rather than continuing this troubleshooting sequence. Keep a useful parallel job going, such as recording a missing part or reading the next test, while the adult helps.

## Work order 1 — assemble your teaching robot

**Target: minutes 5–45. Read this section, then start building.**

### Assign jobs

Write your kit label and group members on the completion record below. Choose a builder, instruction reader, checker, and recorder. With two people, combine builder/recorder and reader/checker. Rotate jobs about every ten minutes. Everyone should handle parts and check an instruction.

### Check essentials and build

1. Photograph your open kit and keep its parts separate from the other kit. Find the hub and battery, the motors required by the build, wheels and tires, necessary frame pieces, pins, axles, and a USB data cable. The official base uses an auxiliary attachment motor as well as the two drive motors. Do not spend this block counting every spare element.
2. Open the [Practice Driving Base instructions](../06_References/LEGO_Practice_Driving_Base.pdf). Follow numbered steps **1–34**. The step numbers are not the PDF page numbers. Check axle lengths, pin positions, and motor orientation against the pictures.
3. If a part seems missing, look under the tray and in the correct compartment. Record the build step and part description. Ask the adult about a replacement; do not silently take it from the other kit. Log borrowed personal pieces in the [prep tracker](../SESSION_PREP.md#personal-parts-loan-log).
4. Check that the wheels turn freely, tires are seated, the hub is secure, and the chassis sits properly. Keep loose cables clear of wheels.
5. Label the robot’s front. Stand behind the robot looking toward that front. Trace the **left wheel motor cable to port A**, and the **right wheel motor cable to port B**. This curriculum’s wiring takes precedence over a different wiring diagram in the build PDF.
6. Leave the auxiliary attachment motor electrically unplugged and secure its cable. It can remain part of the physical build. The distance sensor and color sensor are not needed for Week 1; ports C and D are reserved for them later.
7. Label the hubs clearly, such as **YMCA A** and **YMCA B**. A kit label and a motor port are different things: both robots use motor ports A and B.

**Checkpoint 1:** show the adult your completed base. Each person should be able to point to the front, trace one drive cable, and explain why the extra motor is unplugged. Show your shortage list if anything is unresolved. Do not run the motors until the adult has checked the setup and stop controls.

## Work order 2 — connect and test your own kit

**Target: minutes 45–65. Record the result of each test for your kit.**

### Connect and prepare

1. Open **SPIKE App 3**, choose SPIKE Prime, and create a **Python** project. Use a USB data connection for the initial setup if available. Confirm the connected hub matches your kit label. Ask the adult to handle installation, permission, or firmware-update blockers.
2. Ask the adult to show the actual app and hub stop controls. Every trainer points them out and demonstrates the agreed stop procedure before floor testing. Confirm that the robot is stopped before lifting, resetting, or changing cables.
3. Place the robot on the prepared support with **both drive wheels clear**. The support must not obstruct the wheels or tip when they turn.

### Run the smoke test

4. Copy the **entire contents** of [00_mentor_smoke_test.py](../04_Python/00_mentor_smoke_test.py) into the Python project, replacing the default sample. Save it as a clearly named motor-test project for this kit. Do not run this file with ordinary desktop Python.
5. Predict: the hub should show **T**, and the paired drive wheels should turn briefly, then stop. One trainer starts the run and another watches. The test commands 90 wheel degrees at a low speed; it does not need either sensor.
6. Observe whether the motors cooperate to drive the chassis forward. If they oppose one another or the chassis configuration seems wrong, stop and check the instructions, front label, and physical A/B cables with the adult. Do not experiment by randomly changing the motor code.
7. After adult approval, put the robot on the floor at the taped start, check the lane, and repeat. Confirm short, straight movement in the labeled forward direction. If it reverses, spins, or binds, stop and record the problem; that kit has not passed yet.

### Run the lesson starter

8. Create a **separate** Python project and paste the full [W01_signal.py](../04_Python/W01_signal.py). Save a clean copy named, for example, **W01_STARTER_A** or **W01_STARTER_B**. Keep the motor-test project too.
9. Find `student_recipe()` and the comments `STUDENT RECIPE START` / `END`. Read the three lines aloud. Leave the supporting code below unchanged.
10. Run once with wheels raised, then in the clear floor lane after the raised-wheel test passes. Expected order: display **Y**, wait **500 milliseconds**, then drive **90 wheel degrees** and stop. The raised-wheel run still turns the motors; displaying a letter does not make this a display-only program.
11. Record the actual result. A clean run from the other kit is not evidence for your kit.

**Checkpoint 2:** show the adult the successful floor run, the saved starter, and the test record. If either test fails, report the last successful step and the exact error or behavior.

## Work order 3 — become the learner

**Target: minutes 65–80. Every trainer edits, predicts, and runs at least once.**

1. Make a practice copy of the clean starter, such as **W01_PRACTICE_A**. Keep `drive(90)` unchanged.
2. Trainer 1 changes `"Y"` to a different single letter, keeping the quotes. Another trainer predicts the order. Run and compare the result with the prediction.
3. Change the operator. The next trainer changes `pause(500)` to `pause(1000)`. Predict before running: what changes, and what stays the same?
4. Continue changing operators until everyone has had a turn. With a third trainer, move the signal line after the drive line and predict the resulting order. With a fourth, restore the original order and explain it. In all cases, keep the complete program and indentation intact.
5. Each person explains these points in their own words:
   - A program is a set of instructions.
   - `signal("Y")` chooses the displayed text.
   - `pause(500)` waits half a second; `pause(1000)` waits one second.
   - `drive(90)` requests a quarter rotation of the drive wheels, not 90 centimeters and not a 90-degree heading change.
   - A longer pause changes waiting time, not the requested wheel rotation.
   - In this recipe, `await` lets the current action finish before the next instruction runs.
6. Save the practice result, then demonstrate how to reopen the clean starter.

If someone finishes quickly, have them act as the navigator and ask questions. Do not use the extra time for faster driving or modifying the support functions.

## Work order 4 — prepare to teach

**Target: minutes 80–90. Read selectively, not the entire instructor manual.**

1. Everyone reads the **Preparation and assembly** section and **slides 3–5** in the [Week 1 detailed notes](Speaker_Notes/W01_signal_Speaker_Notes.md).
2. Divide the remaining sections: one trainer reads slides 1–2, another reads slides 6–7. With more trainers, split those sections further. Each reader gives the group a thirty-second explanation of the important timing or task.
3. Open the **Week 1 station task card**. Build and hand-test the removable mascot using a clearance template. At the robot, practice the short prediction and result record. Notice that swapping first and last actions differs from moving the last action to the top; say which operation you mean.
4. Each trainer prepares a three-minute teaching attempt using the recipe. Include:
   - One plain-language explanation.
   - One prediction question and time for the learner to answer.
   - One small edit made by the learner.
   - One observed result and a question about it.
5. Agree the teaching order. During the next block, each person must teach; reading the material alone does not complete the training.

## Work order 5 — teach a trainer who acts as a beginner

**Target: minutes 90–110. Use up to four five-minute rounds per kit group.**

For each round, assign a teacher and learner. Other group members observe and keep time; with two people, the learner also gives feedback. Use **three minutes to teach and two minutes for feedback and reset**. Switch the teacher each round. Both kit groups run their rounds at the same time.

Suggested rounds:

1. Explain the original sequence and help the learner change the letter.
2. Help the learner change 500 to 1000 and predict the difference.
3. Help the learner move the signal after the drive and explain the new order.
4. Help a learner recover a simple syntax error, or practice a fair driver/navigator swap.

For the syntax scenario, use a **practice copy** with one missing quotation mark. Let the learner read the error and inspect the changed line. Do not introduce mechanical faults or change cables to create a rehearsal problem.

The learner should act like a beginner, not try to defeat the teacher. Ask a realistic question such as “Does 90 mean centimeters?” or “Why didn’t the robot travel farther when we doubled the pause?”

Observers give feedback using these checks:

- Did the teacher explain accurately without a long lecture?
- Did the learner predict before Run?
- Did the learner make the edit or direct an accessible equivalent?
- Did the teacher ask what happened before giving a fix?
- Did the teacher leave room for the learner to answer and handle a role swap fairly?

Use this feedback sentence: **“One thing that helped me learn was ____. Next time, try ____.”** With spare rounds, repeat after feedback or rehearse a learner who monopolizes the keyboard. The adult may ask for a repeat before a trainer leads independently.

## Work order 6 — leave a ready teaching station

**Target: minutes 110–120.**

1. Reopen the clean Week 1 starter. Save the practice files separately and confirm the saved project can be found again.
2. Complete both the kit record and individual practice record below. Mark blocked items honestly.
3. Photograph your finished chassis and A/B wiring for future setup; keep people out of the reference pictures.
4. Leave the base assembled. Store loose parts and borrowed parts in their labeled locations. Confirm the charging and storage assignment with the adult.
5. Give the adult one short report: **“Kit ___ is ready / blocked. We verified ___. The remaining task is ___, owned by ___, to be checked by ___.”**
6. Confirm your first-session role. The learner baseline happens before the demonstrations; children switch driver/navigator roles; the last six minutes are reserved for saving and cleanup. R3PTAR has its own assigned operator and rehearsal.

## Kit completion record

Use one record for each kit. Blank means not checked. Use **Pass**, **Blocked**, or **Not checked**; include what you observed.

Kit: ______  Date: ______  Group: ______  Adult reviewer: ______

| Check | Result and observation |
|---|---|
| Official base assembled; wheels and cables clear | ______ |
| Front labeled; left motor traced to A, right to B | ______ |
| Auxiliary motor unplugged; cable secured | ______ |
| Correct hub connected; battery suitable for rehearsal | ______ |
| App and hub stop procedure demonstrated | ______ |
| Raised-wheel smoke test: T, brief motion, stop | ______ |
| Floor smoke test: short forward movement | ______ |
| Week 1 starter: Y → wait → move → stop | ______ |
| Pause changed to 1000; longer wait observed | ______ |
| Clean starter saved and reopened | ______ |
| Final configuration photographed | ______ |
| Storage and charging owner assigned | ______ |

Saved project names / locations: ______________________________

Missing or borrowed parts: ____________________________________

**Kit status:** Ready for Week 1 / Blocked

Remaining issue: __________________  Owner: __________  Next check: __________

This certifies only the recorded Week 1 checks. Later sensor lessons still need their own preparation and testing.

## Individual practice record

| Trainer | Operated robot | Explained recipe and units | Used stop procedure | Taught a learner | Follow-up practice |
|---|---|---|---|---|---|
| ______ | ______ | ______ | ______ | ______ | ______ |
| ______ | ______ | ______ | ______ | ______ | ______ |
| ______ | ______ | ______ | ______ | ______ | ______ |
| ______ | ______ | ______ | ______ | ______ | ______ |

Adult follow-up: record who can lead a kit station and who will assist until another practice check. Transfer actual kit results and open issues into the [preparation tracker](../SESSION_PREP.md).

## October 25 feedback and current class plan

Student instructors practiced and supplied feedback. The class is now confirmed as 12 children in grades 5–6 with 4–6 student instructors and four available laptops. Read [Grouping and roles](Grouping_and_Roles.md), rehearse three rotating jobs, and use [the Week 1 print-and-bring checklist](Class_Preparation/W01_signal_Checklist.md). Actual kit test results and individual readiness records remain to be supplied.
