# MechaRAMS YMCA pilot | SPIKE App 3 Python
# Original teaching scaffold, October 2026. Bench-test on both actual kits.
# Paste this ENTIRE file into one SPIKE Prime Python project.
# This is not desktop Python, SPIKE Legacy, or Pybricks.
from hub import port, light_matrix
import motor_pair
import runloop
import distance_sensor
import color_sensor

# MENTOR SETTINGS: trace the physical wheel-motor cables before pairing.
# Left wheel motor A, right wheel motor B, distance C, color D.
SPEED = 200  # wheel degrees per second, not percent
PAIR = motor_pair.PAIR_1

async def student_recipe():
    # STUDENT RECIPE START
    threshold = 40  # Replace with YOUR measured threshold.
    result = await seek_marker(threshold)
    print("Stop reason:", result)
    # STUDENT RECIPE END

# MENTOR SUPPORT FUNCTIONS BELOW
async def signal(letter):
    await light_matrix.write(letter)

async def pause(milliseconds):
    await runloop.sleep_ms(milliseconds)

async def drive(wheel_degrees):
    if not 0 <= wheel_degrees <= 1080:
        raise ValueError("drive needs 0 to 1080 wheel degrees")
    await motor_pair.move_for_degrees(
        PAIR, int(wheel_degrees), 0, velocity=SPEED)

async def turn(wheel_degrees):
    # A pivot based on WHEEL rotation. This is not a robot heading angle.
    if not -360 <= wheel_degrees <= 360:
        raise ValueError("turn needs -360 to 360 wheel degrees")
    await motor_pair.move_for_degrees(
        PAIR, int(wheel_degrees), 100, velocity=SPEED)

async def park(stop_mm):
    # Bounded, slow approach. Every command finishes before the next reading.
    # It is a classroom prototype, not a certified collision-prevention system.
    if not 100 <= stop_mm <= 250:
        raise ValueError("parking threshold needs 100 to 250 mm")
    for step in range(12):
        gap = distance_sensor.distance(port.C)
        print("gap mm:", gap)
        if gap < 0:
            motor_pair.stop(PAIR)
            await signal("?")
            return "invalid"
        if gap <= stop_mm:
            motor_pair.stop(PAIR)
            await signal("P")
            return "near"
        await drive(30)
        await pause(50)
    # Read once more after the final allowed movement.
    gap = distance_sensor.distance(port.C)
    motor_pair.stop(PAIR)
    if gap < 0:
        await signal("?")
        return "invalid"
    if gap <= stop_mm:
        await signal("P")
        return "near"
    await signal("L")
    return "limit"

async def seek_marker(threshold):
    if not 1 <= threshold <= 99:
        raise ValueError("reflection threshold needs 1 to 99")
    for step in range(24):
        reading = color_sensor.reflection(port.D)
        print("reflection:", reading)
        if reading < threshold:
            motor_pair.stop(PAIR)
            await signal("M")
            return "marker"
        await drive(30)
        await pause(50)
    reading = color_sensor.reflection(port.D)
    motor_pair.stop(PAIR)
    if reading < threshold:
        await signal("M")
        return "marker"
    await signal("L")
    return "limit"

async def main():
    motor_pair.pair(PAIR, port.A, port.B)
    try:
        await student_recipe()
    finally:
        motor_pair.stop(PAIR)

runloop.run(main())
