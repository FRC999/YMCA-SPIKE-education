# Week 4 | Cone challenge rematch

Alex reported that the students enjoyed testing in Week 3 and had difficulty completing the cone challenge. This session gives them another run with what they learned. One cone upright in its matching home is the first milestone. The stretch is two or three cones on a course with a diagonal approach to Cone 2. After the final turn, count each upright cone whose entire base is inside its matching home.

## Print and prepare

- [Field map, team card and floor markers](../../02_Student/Printouts/W04_Cone_Rematch.pdf). Print page 1 for each robot lane and page 2 for each of the four teams, plus one spare. Print page 3 at actual size for each lane if using the cutouts. Display page 1 and the student recipe during the opening.
- For a printed field, use the [full-size Letter tiles](../../02_Student/Printouts/W04_Cone_Rematch_Full_Size_Field.pdf). Print pages 2–10 at Actual Size for each lane, join in a 3 × 3 grid and tape it flat. The tiles include the starts and homes. Use the team card from the first packet.
- Two smooth 60 × 60 cm marked fields plus about 20 cm of clear floor around each as a starting layout. Increase clearance if either robot, pusher or displaced cone can sweep beyond it. Pack painter's tape, rulers, six matching cones plus spares, two mentor pushers, team pushers or four equal build packs, four mounting proxies, and the [reusable supplies](Reusable_Kit.md). [Paper cone template](../../02_Student/Printouts/W03_Paper_Cone_Template.pdf) · [Pusher mount picture](../../02_Student/Printouts/W03_Centered_LEGO_Pusher.png) · [Rounded tip sketch on page 2](../../02_Student/Printouts/W03_Dance_Three_Cone_Field.pdf).
- Lay out starts and homes from the lower-left corner using the map. Mark the start axle center and heading. Place each cone so its center meets its own approach line. Cone 2 is diagonal **relative to the field edge**. The robot turns to face it head-on. Use a low rounded center tip that projects beyond the beam so the cone can stay in its home when the robot turns.
- Open the complete [Week 4 SPIKE project source](../../04_Python/W04_cone_rematch.py) on both control laptops. Left motor A, right motor B, speed 200. The recipe reuses Week 3's `drive()`, `turn()` and final `D`. Each row gives one forward distance and one turn in **wheel degrees**. Sensor ports are not needed. Save a baseline and four separately named team copies.
- On each kit, dry-run the marked course without cones. Check where the axle stops and which way the tip points after each turn. Run with only Cone 1, then with Cones 1 and 2, then all three if the next approach clears the earlier home. The printed coordinates assume roughly 17.6 cm wheel circumference, 12 cm wheel track and 10 cm axle-to-tip distance. Adapt the baseline or tape marks for the actual kit before students begin. Keep the field and start pose fixed once teams start comparisons. If the full route is unreliable, teach the one-cone version on that kit and record the limit.
- Use one attendance sheet. Assign two robot mentors and two build mentors. Fit or change attachments only when the robot has stopped.

## Teach the hour

| Minutes | What to do |
|---|---|
| 0–5 | Ask what students saw in Week 3. Have them name a particular miss, tip or turn. Introduce the first home and the two- and three-cone stretches. |
| 5–10 | Show one upright cone delivery and release with a tested mentor tip. Trace the diagonal second approach on the map. |
| 10–14 | Read one row of the recipe aloud. Ask which value to change if the robot stops short and which to change if it points past Cone 2. Show why a turn before a cone is written in the previous row. |
| 14–26 / 26–38 | T1/T3 start at robots and T2/T4 start at build tables, then swap. At robots, run the one-cone baseline with the rehearsed mentor pusher or a tested team pusher. At build, use the proxy and hand-test how the pusher meets and releases the cone. |
| 38–44 / 44–50 | T1/T3 retest, then T2/T4. Fit the approved team pusher or use the team's one-number edit. Compare against the baseline. Give a team its next cone after a reliable delivery. |
| 50–54 / 54–60 | Each child names a prediction or observation. Save the team's tested code and result, then reset and pack. |

Robot jobs are driver, navigator and observer. Build jobs are builder, parts manager and tester. Rotate every four minutes in the first station turns and every two minutes in retests. Each child predicts or explains a change before running it.

## Coach with the result

- **Axle stops short or goes long.** Adjust the forward value on that leg in small mentor-approved steps. A first experiment might be 10 wheel degrees. Keep the pusher, cone, start and speed fixed for that comparison.
- **Pusher points left or right of the next cone.** Adjust the turn at the end of the previous leg. Change one number and retest before tuning later legs because a turn changes the rest of the path.
- **The tip reaches the cone and it tips or follows the beam.** Hand-test a low rounded tip and check clearance as the beam swings. Compare that hardware change using the same recipe. Recheck that the cone base stands flat and that its seam slides smoothly.
- Score upright cones in their matching homes, then record one predicted change and one observed result. A team that gets one cone home and explains its improvement has finished the core rematch.
