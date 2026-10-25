# Stationary diagnostic. Select ONLY the sensor actually attached.
from hub import port
import runloop
import distance_sensor
import color_sensor

MODE = "distance"  # "distance" on C or "reflection" on D

async def main():
    for sample in range(10):
        if MODE == "distance":
            print("mm:", distance_sensor.distance(port.C))
        elif MODE == "reflection":
            print("reflection:", color_sensor.reflection(port.D))
        else:
            raise ValueError("Choose distance or reflection")
        await runloop.sleep_ms(500)

runloop.run(main())
