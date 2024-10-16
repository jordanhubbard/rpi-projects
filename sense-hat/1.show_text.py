from sense_hat import SenseHat
from colors import Colors
import random

sense = SenseHat()
c = Colors()
while True:
    sense.show_message("I love Lamp!", text_colour=c.random_rgb(), back_colour=c.random_rgb(), scroll_speed=random.uniform(0.01, 0.10))
