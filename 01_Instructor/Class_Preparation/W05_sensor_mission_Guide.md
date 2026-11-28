# Week 5 | Stop at the delivery strip

Can the robot carry a supply cube to a marked bay and unload it? Start with the short distance-sensor demo. Teams then calibrate the floor sensor and build a removable tipping tray. The robot uses the strip to stop. With the robot fully stopped, a student lifts the back of the tray to deliver the cube into the bay.

## Print and prepare

- Print the [16-page class packet](../../02_Student/Printouts/W05_Class_Print_Packet.pdf) once on US Letter, Actual Size, single-sided. It includes both lanes with movable strips, all five mission cards and attendance.
- [Sensor mission slides](../../03_Presentations/W05_marker.pptx) · [Slide PDF](../../03_Presentations/W05_marker.pdf) · [Speaker notes](../Speaker_Notes/W05_marker_Speaker_Notes.md). Slide 4 shows the swap and baseline. Slide 5 shows the tray and delivery retest.
- [Team mission card](../../02_Student/Printouts/W05_Sensor_Mission.pdf), four copies plus one spare when printing individually. Use it for prediction, build and trials. Bring the [reusable supplies](Reusable_Kit.md).
- [Full-size delivery lane and movable strip](../../02_Student/Printouts/W05_Delivery_Strip_Full_Size_Field.pdf). Print pages 2–5 at Actual Size on landscape US Letter for each lane. Assemble the three tiles, tape the seams from behind and align the strip's near edge with the 25 cm marks. Use that position for the baseline and cargo trials. The lane has 52 cm ahead of the sensor start. Rehearse the full run with the strip removed and leave clear floor beyond the lane.
- For the opening, connect the forward distance sensor to **C** on one robot and set a broad, upright wall square to the sensor. Mark a repeatable start about **30 cm from the sensor face to the wall**. Load the [distance demo](../../04_Python/W05_distance_demo.py) in a separate instructor project. Rehearse `stop_mm = 150` and `stop_mm = 200` from the same start. At 200 mm the robot should stop farther from the wall. Measure and show the actual results. If the drive demo cannot be rehearsed, show live readings with the wheels still and ask for a prediction.
- Put a downward-facing color sensor on **D** on both kits. Start about **1–2 cm above** a light matte floor or flat light card. Tape a **6 cm wide matte dark strip** flat across the sensor's path. Set its leading edge about **25 cm ahead of the sensor** at START. Leave clear runout beyond the strip for the helper's full 24 short moves. Confirm tape, seams and platforms stay flat and wheels and sensor clear the lane.
- Under classroom lighting, take two readings over each surface on each kit. Dark readings should be consistently lower than light readings. Set a whole-number threshold between the highest dark and lowest light reading. If there is no whole number between them, adjust sensor height, shield glare or change the surface before running. Increase strip width if necessary so a reading is taken while the sensor is above it.
- Assemble and tape both lanes before class. Load the [complete marker project](../../04_Python/W05_marker.py) on both control laptops. Verify `M` with the sensor over the strip at 25 cm and check the full strip-removed run through `L`. Switch the demo robot back to the marker project before the first rotation.
- Bring two tested sample trays, four checked mounting bases or matching proxies, stiff card or spare LEGO, short rails, tape and six lightweight foam or paper cubes. Fit a sample tray on each kit, check wheel and sensor clearance, and run it loaded at 25 cm. Wait for a full stop and tip the cube. Mark a landing bay around the cube’s resting place with flat, light-colored tape tabs outside the sensor path. Bring thin stiff card for teams that reach the automatic unload stretch.

## Build a tipping delivery tray

1. Fit a small tray to the mounting proxy. Hinge the front edge with tape or a LEGO pivot. Make the front edge project just beyond the chassis so the cube can fall clear.
2. Add short side rails, leave the front open, and rest the back of the tray on a support so it rides level. Add a tab or handle so a student can lift the back without touching the cube.
3. Hand-test both parts of the delivery. Move the proxy gently with the tray level. The cube should stay aboard. Lift the handle and check that the cube slides out into a paper target. Improve one thing before the robot test.

If the cube slips during travel, test a thin tape ridge on the tray while keeping the front open. If it hangs on the way out, check the hinge travel and front clearance. Retest both carrying and tipping after a change.

## Stretch challenge Automatic unloading

After a successful manual delivery, use the same tray hinge and add a side lever that lifts the back of the tray. Set a low, shallow cardboard ramp beside the dark strip where only the lever can touch it. Slide the loaded proxy along the route by hand. Move the ramp along the side of the lane until the cube releases into the bay near the measured stop position. The ramp must stay clear of the chassis, wheels, sensor and runout. Tape it down and have a mentor approve a powered run. Use the same strip and program. Record whether the hub showed `M` over the strip and whether the cube landed in the bay without anyone touching the moving robot.

## Teach the hour

| Minutes | What to do |
|---|---|
| 0–5 | Show the cube on a level tray and tip it into a sample bay. Ask how the robot will know when it has arrived. |
| 5–10 | Run the distance demo. Ask whether 200 or 150 stops it farther away. Show a reading and point to the rule `gap <= stop_mm` for a valid reading. |
| 10–14 | Show one light and one dark reading. Ask what the robot will do just below, and exactly at, the chosen threshold. The marker rule is `reading < threshold`. |
| 14–26 | T1/T3 calibrate and run the 25 cm baseline. T2/T4 build and hand-test their tipping trays. |
| 26–38 | Swap. T2/T4 get the same 25 cm baseline. T1/T3 build and hand-test their trays. Label each tray and stage it for the retest. |
| 38–44 / 44–50 | T1/T3 retest, then T2/T4. A mentor checks the team tray and fits it to the stopped robot. Run loaded at the same 25 cm setting. With M showing and the robot fully stopped, lift the handle and check where the cube lands. A team that finishes early may try the side-ramp trigger after a hand test and mentor approval. |
| 50–54 / 54–60 | Ask each child what the sensor read and what made the motors stop. Record the result and measured threshold for Week 6. Save and reset. |

Rotate all three jobs every four minutes in the first turn and every two minutes in retests. At the robot, the driver runs the trial, the navigator checks the start and tips the tray after the full stop, and the observer records both results. At build, rotate builder, parts manager and tester. If a tray needs more work, let the team explain the fault, use the mentor tray to practice unloading, and record which tray ran.

## What counts

Score two results separately. The robot finds the strip when it shows `M` with the sensor over the dark strip. The delivery succeeds when the cube stayed aboard during travel and ends fully inside the bay after tipping. `L` reports the movement limit. If the reading equals the threshold, the robot takes another step if any remain. In Week 6, reuse the measured marker threshold as a starting point and recheck it after fitting the rescue attachment.
