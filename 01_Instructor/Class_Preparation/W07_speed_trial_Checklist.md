# Week 7 timed delivery print and bring checklist

Optional replacement for the original Week 7 mission. Use for 12 children in four teams of three, with two robot stations and two build tables. Follow the [remaining-sessions plan](../Remaining_Sessions_Plan.md) and [detailed teaching notes](../Speaker_Notes/W07_speed_trial_Speaker_Notes.md).

## Print

- [ ] **5 copies** of [timed delivery team sheet](../../02_Student/Printouts/W07_speed_trial_Team_Sheet.pdf): four teams plus one spare.
- [ ] **4 copies** of [cargo cradle build card](../../02_Student/Printouts/W07_speed_trial_Build_Card.pdf): one per team.
- [ ] **1 copy** of [attendance](../../02_Student/Printouts/Attendance.pdf).
- [ ] Optional: **1 copy** of [this packing checklist](W07_speed_trial_Checklist.pdf) and one lead speaker-note document.

**10 required sheets**, single-sided, actual size. These replace the original Week 7 team sheets and build cards. Reuse role cards and hub guides. Keep completed sheets privately.

## Pack

- [ ] Everything in [Reusable_Kit.md](Reusable_Kit.md): two charged bases, four laptops/chargers, tested cables, four team trays, writing tools, rulers, floor-safe tape and the display setup.
- [ ] Two stopwatch-capable devices, separate from the visible rotation timer. No purchase is implied; use available devices. One mentor times all compared runs on each lane while children observe and record.
- [ ] Two tested removable mentor trays and six similar lightweight cubes: two at the robots and four for hand tests.
- [ ] Four mounting/footprint proxies traced from the real bases. Four equal packs of spare beams/pins or pre-cut card; eight card rail strips, eight brace strips, craft tape, and four labeled storage bags. Have four spare card panels for repairs. Do not take parts from the chassis.
- [ ] Two measuring tapes and small removable chassis-reference markers. Prepare two floor lanes, each at least 150 cm long and 50 cm wide, with a 60 cm timed section and a clear runout. Rehearsal may require more space. Keep people and furniture outside the lanes and runouts.
- [ ] Save [slides](../../03_Presentations/W07_speed_trial.pptx), [slide PDF](../../03_Presentations/W07_speed_trial.pdf), notes and the **complete** [program](../../04_Python/W07_speed_trial.py) offline. Four team saves must retain the correct kit's mentor settings.

## Rehearse and configure both kits before class

1. Trace A left/B right; leave the auxiliary motor unplugged and secure any unused cables. Use the existing smoke test for a short forward check. This lesson needs no sensor. The timing mark goes on the chassis, never the removable tray.
2. At each lane, mark the fixed start and the finish 60 cm away, measured along the travel direction. Start with the chassis mark aligned to the start line. Fit the loaded mentor tray. Keep at least 90 cm of clear floor beyond the finish; verify the full robot stops inside the available area.
3. In the mentor section of the speed program, keep `APPROVED_SPEEDS = (200,)`. The supplied `TRAVEL_DEGREES = 0` deliberately blocks motion. Begin calibration with 180 wheel degrees, reset, then increase in small steps on the clear floor. Choose a value no greater than 1440 that crosses the finish and stops well within the runout. Do not infer centimeters from wheel degrees. Once calibrated, keep that value fixed for the comparison.
4. Repeat three loaded runs at 200. Confirm straight travel, cargo retention, stopping, the app/hub stop controls and a quick attachment swap. Keep hands out until all motion stops. A finite motor command does not detect lane edges, and a stall may require the mentor to stop the program.
5. Only then add 300 to `APPROVED_SPEEDS`, rehearse three loaded runs and check stopping space again. If it fails, remove it and teach at 200. Optionally rehearse 400 the same way; do not exceed 400 in this lesson. These are classroom limits, not claimed motor specifications. Save each kit's approved settings separately.
6. Practice stopwatch timing: start on first physical movement after the ready signal/pause; stop when the same chassis mark crosses the finish. Check validity through the final stop. Record seconds to one decimal place; do not treat the display's extra digits as accuracy. `D` means the move ended, not a successful or timed crossing.
7. Build a sample cradle from one team pack, hand-test it, then confirm mounting and clearance. It may not touch the floor, wheels or cables or obscure controls. Student designs get the same inspection before a powered test.
8. Assign two robot mentors and two build mentors. If two lanes cannot be supervised independently, run them alternately; drop the extra speed block to protect the hour. If course setup or movement cannot be made reliable, use the original rehearsed [Week 7 mission](W07_mission_Checklist.md).

## Record the rehearsal

| Kit | Travel degrees | Approved speeds | 60 cm course and runout checked | Three loaded runs passed | Mentor/date |
|---|---|---|---|---|---|
| A | ____ | ____ | ____ | ____ | ____ |
| B | ____ | ____ | ____ | ____ | ____ |

Transfer actual operational results to [SESSION_PREP.md](../../SESSION_PREP.md). Blank fields are not passed checks.

## Closeout and Week 8

- [ ] Save each team's program and selected setting, label and store four cradles, and collect the nine-row trial sheets privately.
- [ ] A showcase setting requires three successful trials out of three. If a late adjustment has fewer trials, label it unconfirmed and use the earlier reliable setting or a stationary explanation.
- [ ] Record kit problems, charge hubs and retain the floor measurements. In Week 8, reopen the saved speed project and use the same lane rules. Keep the existing four-minute team showcase slots and final concept check.
