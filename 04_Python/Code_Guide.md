# Python code guide

Use SPIKE App 3 Python on a SPIKE Prime hub. Paste the entire weekly source file into one new Python project. These are not desktop-Python programs or native SPIKE project bundles. Keep a known-good copy.

Port map: A left wheel motor, B right wheel motor, C distance sensor, D color sensor. Trace cables physically. Any auxiliary attachment motor in the LEGO base remains unplugged for this program. Use the mentor smoke test before movement.

Students edit the `student_recipe` function. Week 6 also has a named `deliver` function and its threshold. The support layer is supplied so beginners can focus on a few readable commands. Show its loops and conditions during the corresponding lesson.

## Teaching commands

```python
await signal("Y")
await pause(500)
await drive(180)
await turn(90)
result = await park(150)
result = await seek_marker(40)
```

drive and turn use wheel degrees. turn(90) does not promise a 90-degree heading change. SPEED is wheel degrees per second. park uses millimeters. seek_marker uses reflected light on a 0–100 scale. Calibrate thresholds on the real surface.

Support code limits drive to 0–1080 wheel degrees, pivots to -360–360 wheel degrees, parking thresholds to 100–250 mm, and reflection thresholds to 1–99. Parking permits 12 short steps, marker seeking 24. Each search takes a final sensor reading after its last allowed move. Keep these bounds.

## Results to interpret

`near` means the parking threshold was reached. `marker` means the dark strip was detected. `invalid` means the distance sensor returned a negative reading and movement stopped. `limit` means the movement budget ended without a target detection. A limit is not mission success.

## Offline checks and local rehearsal

The [Week 7 timed delivery program](W07_speed_trial.py) uses `sprint(speed)`. Its mentor-calibrated travel accepts 1–1440 wheel degrees. The supplied zero blocks movement until configured. Approve speeds from 200, 300 and 400 wheel degrees/s after physical rehearsal. Each start makes one finite move. Use the [speed checklist](../01_Instructor/Class_Preparation/W07_speed_trial_Checklist.md) for calibration and manual stopwatch timing. Reopen each team's saved project in Week 8.

The package checks Python syntax, loop counts, sensor threshold boundaries, invalid distance readings, movement limits, and stopping on a simulated sensor exception with mock modules. These checks do not emulate motors, sensor noise, battery state, firmware, mounting, geometry, or real floor behavior. Complete the hardware acceptance record in the instructor guide.

## Recipe reading cards

### Week 1: Meet your robot

```python
await signal("Y")
await pause(500)
await drive(90)
```

Number these actions in run order: drive, show Y, wait. What changes if the first and last lines trade places?

### Week 2: Delivery to a target

```python
wheel_degrees = 180
await drive(wheel_degrees)
await signal("D")
```

Measure wheel circumference C in centimeters. Predict the centimeters traveled for 180 and 360 wheel degrees using (degrees / 360) × C. For the 40 cm target, calculate (40 / C) × 360 and round at the end. Keep SPEED = 200 and the 0–1080-degree limit. Test the prediction on the real floor.

### Week 3: Robot dance studio

```python
for beat in range(3):
    await drive(90)
    await turn(90)
await signal("D")
```

How many drives? How many turns? Does the final D repeat? Which indentation tells you?

#### Week 3 build and dance test

Attach the team's pusher to the stopped robot and put the cone inside its guide. Run the SAME dance recipe above, including `turn(90)`, with the pusher attached. Predict three drives, three turns and one D. The pusher must keep the cone upright within the guide through the turns; the cone slides on the floor, not fastened or carried.

Record complete drive-and-turn repeats before a tip, escape or loose mount (0–3). Stop for a failure and reset only once stopped. Keep SPEED = 200. Mentors rehearse the swept area and may approve a smaller positive turn on both kits; a wheel turn value is not a heading angle. Preserve turns. Compare one build change with the same cone, start, surface, speed and approved recipe. A hand test alone does not complete the task: each team must fit and test its attachment on the robot.

### Week 4: Cone challenge rematch

```python
for forward_deg, right_deg in route:
    await drive(forward_deg)
    await turn(right_deg)
await signal("D")
```

In [W04_cone_rematch.py](W04_cone_rematch.py), each route row supplies the forward move and the following turn in wheel degrees. Start with Cone 1. Which number changes how far the pusher reaches? Which earlier turn changes the heading toward Cone 2?

### Week 5: Stop at the delivery strip

For the short wall demonstration, use [W05_distance_demo.py](W05_distance_demo.py). Compare 150 and 200 mm from the same start. The floor-marker activity uses [W05_marker.py](W05_marker.py) and a separate reflection threshold.

```python
threshold = 40
reading = color_sensor.reflection(port.D)
if reading < threshold:
    await signal("M")
```

If dark reads 12 and light reads 76, is 44 a useful threshold? What happens if the threshold is below both readings?

### Week 6: Rescue the supply cube

```python
async def deliver():
    await signal("R")
    result = await seek_marker(threshold)
    print(result)

# inside student_recipe
await deliver()
```

Reuse the measured Week 5 threshold and recheck it with the guide attached. The marker result tells you what the sensor found. Observe separately whether the whole cube base reached the rescue bay.

### Week 7: Timed delivery

```python
speed = 200
await sprint(speed)
```

Choose an approved speed and keep the kit's calibrated travel fixed. Compare the same tray at different speeds, or compare two trays at the same speed.

### Week 8: Robot showcase

Open each team's saved Week 7 timed delivery project on the same kit and course. Ask one student to point to a choice in their actual code. Time the demo from first movement to the chassis mark crossing FINISH. If the robot cannot run, use the saved code, cradle and trial record.

Sources: official SPIKE App Python help, LEGO Cart Control, and the Tufts CEEO SPIKE 3 documentation archive. See the research source list for links. The short programs and helper layer are original teaching materials.
