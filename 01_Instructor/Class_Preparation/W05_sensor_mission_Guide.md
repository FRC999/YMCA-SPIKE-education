# Week 5 | Stop at the delivery strip

The robot has to stop at a marked delivery bay. Start with a short distance-sensor demonstration and let all teams build and test the floor-marker mission. Both activities use the same pattern. Read the sensor, compare the reading with a number in the code, then stop or take another short step. The distance sensor reports the gap. The program commands the stop.

## Print and prepare

- [Team mission card](../../02_Student/Printouts/W05_Sensor_Mission.pdf), four copies plus one spare. Use it for prediction, build and trials. Bring one attendance sheet and the [reusable supplies](Reusable_Kit.md).
- For the opening, connect the forward distance sensor to **C** on one robot and set a broad, upright wall square to the sensor. Mark a repeatable start about **30 cm from the sensor face to the wall**. Load [parking](../../04_Python/W04_parking.py) in a separate instructor project. Rehearse `stop_mm = 150` and `stop_mm = 200` from the same start. At 200 mm the robot should stop farther from the wall. Measure and show the actual results. If the drive demo cannot be rehearsed, show live readings with the wheels still and ask for a prediction.
- Put a downward-facing color sensor on **D** on both kits. Start about **1–2 cm above** a light matte floor or flat light card. Tape a **6 cm wide matte dark strip** flat across the sensor's path. Set its leading edge about **25 cm ahead of the sensor** at START. Leave clear runout beyond the strip for the helper's full 24 short moves. Confirm tape, seams and platforms stay flat and wheels and sensor clear the lane.
- Under classroom lighting, take two readings over each surface on each kit. Dark readings should be consistently lower than light readings. Set a whole-number threshold between the highest dark and lowest light reading. If there is no whole number between them, adjust sensor height, shield glare or change the surface before running. Increase strip width if necessary so a reading is taken while the sensor is above it.
- Load the [complete marker project](../../04_Python/W05_marker.py) on both control laptops. Verify that the robot stops with `M` and its **sensor** above the strip. `L` means it used up the move limit. Practice switching the opening demo robot back to the marker project before the first rotation. Have four build packs with light card, dark tape, a footprint proxy and a side delivery platform. [Floor-marker slides, 2–6](../../03_Presentations/W05_marker.pdf) can support the live lesson.

## Teach the hour

| Minutes | What to do |
|---|---|
| 0–5 | Introduce the delivery bay. Ask how the robot could tell when it arrived if you moved the bay. |
| 5–10 | Run the distance demo. Ask whether 200 or 150 stops it farther away. Show a reading and point to the rule `gap <= stop_mm` for a valid reading. |
| 10–14 | Show one light and one dark reading. Ask what the robot will do just below, and exactly at, the chosen threshold. The marker rule is `reading < threshold`. |
| 14–26 / 26–38 | T1/T3 start at robots and T2/T4 start at build tables, then swap. At robots, every team measures both surfaces, chooses a threshold and attempts a delivery. At build, teams make a flat road and a side bay with their own dark strip, then hand-check clearance. |
| 38–44 / 44–50 | T1/T3 retest, then T2/T4. Test the approved team strip. If time permits, move the strip to another reachable spot and predict where the robot will stop. Keep the threshold fixed if the strip and surface are the same. |
| 50–54 / 54–60 | Ask each child what the sensor read and what made the motors stop. Record the result and measured threshold for Week 6. Save and reset. |

Rotate all three jobs every four minutes in the first turn and every two minutes in retests. At the robot, driver runs the trial, navigator checks the start and predicts, observer measures and records. At build, rotate builder, parts manager and tester.

## What counts

A successful delivery stops with the sensor over the dark strip and displays `M`. Film or observe the sensor position if the robot body obscures it. If the reading is **equal** to the reflection threshold, the robot takes another step if any remain. During parking, an invalid reading is handled separately from a genuine near-wall result. A robot that stops at its movement limit has not located the target. In Week 6, reuse the measured marker threshold as a starting point and recheck it after fitting the rescue attachment.
