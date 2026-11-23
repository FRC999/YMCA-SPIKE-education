# MechaRAMS YMCA | SPIKE App 3 Python
# Paste this entire file into a new project. Week 3 drive and turn helpers.
from hub import port, light_matrix
import motor_pair
import runloop

# Mentor setup: left drive motor A, right drive motor B.
SPEED = 200  # wheel degrees per second
PAIR = motor_pair.PAIR_1


async def student_recipe():
    # STUDENT RECIPE START
    # Each row is (forward wheel degrees, right turn wheel degrees).
    # These are starter values. Predict and test one change at a time.
    route = [
        (245, 107),  # Cone 1, then point toward Cone 2
        (327, 139),  # Cone 2, then point toward Cone 3
        (286, 96),   # Cone 3, then make the final turn
    ]
    for forward_deg, right_deg in route:
        await drive(forward_deg)
        await turn(right_deg)
    await signal("D")
    # STUDENT RECIPE END


async def signal(letter):
    await light_matrix.write(letter)


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


async def main():
    motor_pair.pair(PAIR, port.A, port.B)
    try:
        await student_recipe()
    finally:
        motor_pair.stop(PAIR)


runloop.run(main())
