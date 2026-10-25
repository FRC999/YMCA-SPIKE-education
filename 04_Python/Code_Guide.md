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
travel = 180
await drive(travel)
await signal("D")
```

If 180 wheel degrees travels about 9 cm on our floor, what might 360 do? Mark this as a prediction, not a promise.

### Week 3: Robot dance studio

```python
for beat in range(3):
    await drive(90)
    await turn(90)
await signal("D")
```

How many drives? How many turns? Does the final D repeat? Which indentation tells you?

### Week 4: Parking assistant

```python
stop_mm = 150
gap = distance_sensor.distance(port.C)
if 0 <= gap <= stop_mm:
    await signal("P")
```

At a 150 mm threshold, classify 220, 150, 90, and -1. Which readings mean near? Which means check the sensor?

### Week 5: The floor tells the robot

```python
threshold = 40
reading = color_sensor.reflection(port.D)
if reading < threshold:
    await signal("M")
```

If dark reads 12 and light reads 76, is 44 a useful threshold? What happens if the threshold is below both readings?

### Week 6: A rescue attachment

```python
async def deliver():
    await signal("R")
    result = await seek_marker(threshold)
    print(result)

# inside student_recipe
await deliver()
```

Why might two short side guides keep a cube in front better than one flat beam? How could too much contact slow the robot?

### Week 7: Community robot mission

```python
mission = "marker"
if mission == "marker":
    result = await seek_marker(threshold)
else:
    result = await park(stop_mm)
print(result)
```

Which part of your mission is most likely to fail? What small test could answer that before you run everything?

### Week 8: Robot showcase

```python
await signal("Y")
result = await seek_marker(threshold)
print("Our result:", result)
```

Before the demo, predict the stop reason. What will you explain if the robot stops for a limit instead of detecting its target?

Sources: official SPIKE App Python help, LEGO Cart Control, and the Tufts CEEO SPIKE 3 documentation archive. See the research source list for links. The short programs and helper layer are original teaching materials.
