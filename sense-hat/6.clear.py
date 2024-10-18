from sense_hat import SenseHat
from colors import Colors
import time

sense = SenseHat()
c = Colors()

i = 0
while i < 10:
    hue = c.random_rgb()
    print(f"Clearing display to {hue}")
    sense.clear(hue)
    i += 1
    time.sleep(0.5)
