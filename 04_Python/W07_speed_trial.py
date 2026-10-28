# MechaRAMS / Cheshire YMCA | optional Week 7 | SPIKE App 3 Python
# Paste this ENTIRE file into one SPIKE Prime Python project.
# One supervised run per start. Stopwatch timing is separate from this program.
from hub import port, light_matrix
import motor_pair
import runloop

PAIR = motor_pair.PAIR_1
# MENTOR: calibrate on this kit before class, then keep fixed for all trials.
# 0 deliberately prevents driving until the route has been rehearsed.
# Pick 1..1440 wheel degrees to cross the 60 cm line and stop in the runout.
TRAVEL_DEGREES = 0
# Classroom choices, not the motor's maximum capability. Test each on the floor.
APPROVED_SPEEDS = (200,)  # Add 300, then optionally 400 only after rehearsal.

async def student_recipe():
    # STUDENT RECIPE START
    speed = 200  # wheel degrees per second, not percent or cm/s
    await signal("R")
    await pause(1000)
    await sprint(speed)
    await signal("D")
    # STUDENT RECIPE END

async def signal(letter):
    await light_matrix.write(letter)

async def pause(milliseconds):
    await runloop.sleep_ms(milliseconds)

def check_settings(speed):
    if type(TRAVEL_DEGREES) is not int or not 1 <= TRAVEL_DEGREES <= 1440:
        raise ValueError("Mentor must calibrate TRAVEL_DEGREES: 1 to 1440")
    if (not APPROVED_SPEEDS or
            any(type(s) is not int or s not in (200, 300, 400)
                for s in APPROVED_SPEEDS)):
        raise ValueError("Approved speeds must be selected from 200, 300, 400")
    if type(speed) is not int or speed not in APPROVED_SPEEDS:
        raise ValueError("Choose a speed rehearsed and approved by the mentor")

async def sprint(speed):
    check_settings(speed)
    try:
        await motor_pair.move_for_degrees(
            PAIR, TRAVEL_DEGREES, 0, velocity=speed)
    finally:
        motor_pair.stop(PAIR)

async def main():
    motor_pair.pair(PAIR, port.A, port.B)
    try:
        await student_recipe()
    finally:
        motor_pair.stop(PAIR)

# D means the commanded movement ended, not that a delivery was successful.
# This program does not detect the finish line, time it, or sense lane edges.
# The observer times and judges the run. Reset by hand only after full stop.
runloop.run(main())
