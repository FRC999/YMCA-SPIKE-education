# Wheel turns and distance

Team ____   Kit ____   Our measured circumference C = ____ cm

## Around the wheel

Diameter d goes across the center. Radius r is half the diameter. Circumference C goes all the way around the tire.

C = pi × d = 2 × pi × r. Pi is about 3.14.

With the robot off, wrap a string or paper strip once around the tire. Straighten it and measure the length. Ask the mentor for help.

## Part of a turn

90 degrees = quarter turn. 180 degrees = half turn. 360 degrees = one full turn. 720 degrees = two full turns.

One full wheel turn predicts one circumference of forward travel when the wheel rolls straight without slipping.

## Code to distance

Predicted distance = (wheel degrees / 360) × C

Example only, C = 17.6 cm: 180 degrees predicts 8.8 cm; 360 predicts 17.6 cm; 720 predicts 35.2 cm.

For OUR kit, 180 degrees predicts ____ cm and 360 predicts ____ cm.

## Distance to code

Wheel degrees = (target distance / C) × 360

Example only: for 40 cm with C = 17.6 cm, (40 / 17.6) × 360 is about 818 degrees. Round only at the end.

For OUR kit, (40 / ____) × 360 = ____ wheel degrees.

Use centimeters for both target and C. One meter = 100 cm. The 1 meter question is a paper calculation today.

## Our test

Change wheel_degrees in the supplied program. Keep speed, floor, tray, cube and start direction the same. Measure movement of the same chassis mark. Test 180, then 360, then your calculated 40 cm value. Stay within 0–1080 degrees and ask the mentor before running.

The motor counts turns. It does not measure distance across the floor. Measure the real travel and explain any difference.
