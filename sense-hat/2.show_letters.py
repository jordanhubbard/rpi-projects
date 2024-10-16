from sense_hat import SenseHat
from colors import Colors
import time

sense = SenseHat()
c = Colors()

ch = 65
while ch < (65 + 26):
    hue = c.random_rgb()
    # Eliminate black as a choice
    while hue == (0, 0, 0):
        hue = c.random_rgb()
    sense.show_letter(f"{chr(ch)}", hue)
    ch += 1
    time.sleep(1)
