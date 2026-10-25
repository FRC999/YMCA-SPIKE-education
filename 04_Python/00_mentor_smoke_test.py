# SPIKE App 3 Python. First run with wheels lifted clear of the floor.
# Confirm paired motor direction, then repeat in a clear floor lane.
from hub import port, light_matrix
import motor_pair
import runloop

async def main():
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
    try:
        await light_matrix.write("T")
        await motor_pair.move_for_degrees(
            motor_pair.PAIR_1, 90, 0, velocity=150)
    finally:
        motor_pair.stop(motor_pair.PAIR_1)

runloop.run(main())
