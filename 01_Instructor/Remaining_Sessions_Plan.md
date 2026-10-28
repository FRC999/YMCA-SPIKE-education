# Plan for sessions 2 through 8

Alex reported that the October 27 first session went very well, the children stayed engaged, the group seemed more advanced than expected, and the activities fitted the hour. Keep the eight-session sequence and successful rotation schedule. Offer more reasoning and code ownership as teams become ready; do not make longer programs the measure of progress.

**Recommended adjustment:** keep sessions 2–6, offer the timed delivery challenge in session 7, and use session 8 to demonstrate the team's tested result. The original community mission remains available if the room, hardware rehearsal or class interest favors it. Choose one Week 7 route for the class before preparing the stations; the speed lesson replaces that week's mission, not another week or an extra hour.

## The remaining sequence

Each linked notes document supplies the teaching script, questions, expected reasoning, robot procedure, rotation schedule and troubleshooting. Its matching PPTX has embedded speaker notes for rehearsal. The [main materials table](../README.md#weekly-materials) links every slide deck, team sheet, build card, checklist and program.

| Session | Robot and Python work | Hands-on build and test | Optional stretch after the core works |
|---|---|---|---|
| [2 Delivery](Speaker_Notes/W02_delivery_Speaker_Notes.md) | Change `travel`, measure 180 and 360 wheel degrees, estimate a 40 cm delivery | Removable cargo tray; add a rail and compare a gentle tilt | Repeat one command three times and describe the spread. Predict the next value before a mentor suggests one. Keep speed fixed for the main comparison. |
| [3 Dance](Speaker_Notes/W03_dance_Speaker_Notes.md) | Trace a counted loop and change its repeated actions | Dancer with a hinge or moving arm; move it by hand ten times | Write a short routine with two or three commands inside the loop. Add a signal outside it and explain why it appears once. Keep 2–3 repeats. |
| [4 Parking](Speaker_Notes/W04_parking_Speaker_Notes.md) | Compare valid distance readings with a threshold; interpret near, invalid and limit | Broad, braced garage wall; hand-test a footprint proxy | Trace the helper's negative-reading check, near decision and short move. Predict a reading exactly at the threshold. Keep the movement limit. |
| [5 Floor marker](Speaker_Notes/W05_marker_Speaker_Notes.md) | Measure light and dark, choose a threshold, explain repeated checks | Flat road and a wide stopping band; check for tape edges and catches | Have a student explain or annotate the bounded loop and its final reading. Test one surface or lighting change and recalibrate. |
| [6 Rescue](Speaker_Notes/W06_rescue_Speaker_Notes.md) | Call `deliver()` and distinguish sensor success from payload success | Passive scoop/guide; compare a flat edge with side guides | Sketch the function's sequence, then explain what each action contributes. Compare three trials per design if time permits. |
| [7 Timed delivery option](Speaker_Notes/W07_speed_trial_Speaker_Notes.md) | Pass a speed into `sprint(speed)`; compare repeated runs over a fixed distance | Removable cargo cradle; compare its delivery reliability with a mentor tray | Compare 200 and a rehearsed 300 wheel degrees/s. Try 400 only if already approved and time remains. Optional average speed is distance/time. |
| [8 Showcase](Speaker_Notes/W08_showcase_Speaker_Notes.md) | Reopen the saved Week 7 project; each child explains one choice and one result | Repair the exhibit and add a sign showing the job and evidence | Explain a limitation and a next experiment. For timed delivery, show successful trials and mean time; do not introduce a new speed on showcase day. |

## Use readiness to choose the stretch

During coached work, look for all three children being able to predict the next action, make or explain one change, and reset with help. Offer one stretch to a team that has completed its core test. If only the most confident child understands, rotate the driver and ask another child to explain before adding complexity. Students may type more of their recipe, but the complete starter and tested support functions remain available. No opening ability quiz or public ranking of programming skill is needed.

The existing progression already grows from a named value to loops, conditions, sensor feedback and a function. Four to eight meaningful lines can be appropriate when children understand them; copying more lines is not an extra learning objective. Keep mentors' explanations inside the 10–14 minute code/prediction slot and coach further at the stations.

## Preserve the hour

For sessions 2–7: 0–5 welcome and retrieval; 5–10 demonstration; 10–14 code and prediction; 14–26 T1/T3 at robots and T2/T4 building; 26–38 switch; 38–44 T1/T3 retest; 44–50 T2/T4 retest; 50–54 reflection; 54–60 save and reset. The transitions are inside those blocks. Rotate three jobs every four minutes in the first turns and every two minutes in retests. Every team has 18 robot minutes. Every build uses a footprint/mounting proxy so it works while the shared robot is occupied.

Week 8 keeps its separate schedule: 0–7 individual final check; 7–12 briefing; 12–24 two rehearsal turns; 24–28 setup; 28–44 four four-minute demonstrations; 44–50 celebration; 50–54 reflection; 54–60 packing. Retain the final check on concepts taught in Weeks 1–6. There was no opening concept baseline, so it cannot establish pre/post learning gains.

## Instructor practice before each session

1. The lead opens that week's checklist and assigns two robot mentors, two build mentors and any floaters. Each mentor reads the separate notes; robot mentors practice using Presenter View or read the Markdown alongside the PDF slides.
2. Rehearse the complete program on **both actual bases** with that week's floor, attachments and sensor positions. Check the correct hub and A/B motor wiring. Record outcomes in [SESSION_PREP.md](../SESSION_PREP.md). First-session success is not evidence that later sensors or speed settings have passed.
3. Build two mentor samples and four equal team packs. Complete the build card with the allocated parts, then hand-test the sample and check a quick swap onto the stopped base. Use card/tape if spare LEGO is insufficient; never borrow structural parts from a teaching base.
4. Do a 15-minute teach-back after hardware preparation: 4 minutes for the demo/code explanation, 6 for one mini robot/build rotation, 3 for a likely failure and recovery, 2 for saving and resetting. A second mentor acts as a learner and asks a question. This supplements, rather than replaces, the physical rehearsal.
5. Practice one misconception: wheel degrees versus centimeters (2), indentation (3), invalid distance (4), marker versus line following (5), function name versus actual payload success (6), speed versus reliability (7), or explaining a failed demo honestly (8).
6. Download the slides, complete program and references; print the checklist quantities. Save four separate team programs. Use team IDs and keep completed child records outside the public repository.

## Timed delivery materials and rules

Use the [speed checklist](Class_Preparation/W07_speed_trial_Checklist.md), [slides](../03_Presentations/W07_speed_trial.pptx), [slide PDF](../03_Presentations/W07_speed_trial.pdf), [speaker notes](Speaker_Notes/W07_speed_trial_Speaker_Notes.md), [build card](../02_Student/Printouts/W07_speed_trial_Build_Card.md), [trial sheet](../02_Student/Printouts/W07_speed_trial_Team_Sheet.md) and [full program](../04_Python/W07_speed_trial.py). Use these in place of the original Week 7 student materials. The workbook's original mission page is for the original route.

This is the fastest **reliable delivery within the classroom rules**, not a test of the motor's maximum possible speed. Keep the chassis, motors and wheels assembled. Children improve a removable cradle and select an approved speed. The cargo is one lightweight cube. Do not add gearing or extra motors during this hour.

Use a 60 cm measured course and an additional clear stopping area on the floor. Time from the robot's first movement until a fixed mark on its chassis crosses the finish line. The mark must not be on the changing attachment. The program runs a fixed, mentor-calibrated wheel rotation and stops beyond the finish; it does not detect the line or measure the crossing time. A successful trial crosses the finish, keeps its cargo and stays in its lane until it stops in the runout.

Start with the same mentor tray for each team's first robot turn. Record three runs at 200, then three at an approved 300 if time permits. Keep everything but speed unchanged. At the build table, each team makes its own cradle. In the retest, compare that cradle with the mentor tray at the same chosen speed using three trials. Both station orders therefore allow a fair comparison. If time is tight, skip the higher-speed block and compare the two trays at 200.

Keep failed attempts visible. A setting is ready for the showcase only after three successful trials out of three. Compare mean time only for a complete successful set at one unchanged setting; close stopwatch times are a tie worth retesting. Favor within-team improvement on the same kit. Different batteries, motors, floors and human timing make cross-kit hundredths-of-a-second rankings unjustified.

For Week 8, reload the actual saved speed project rather than the marker fallback. Use the speed lesson's lane, stop check and cargo setup. Each team presents its user/job, one code choice, one build change and its actual results within the existing four minutes. The showcase build table repairs the saved cradle and adds a results sign. If the run fails, use the trial sheet to explain what happened. The original Week 8 sensor example applies only to teams demonstrating a sensor mission.

## What is prepared and what still needs rehearsal

The repository has complete material sets for sessions 2–8, plus the optional speed set. Their presence and embedded-note agreement can be checked with `python scripts/check_lesson_materials.py`. Document and PDF synchronization use the existing checkers. These checks do not establish physical readiness. Keep actual dates, later sensor results, speed approvals and room fit open until confirmed.
