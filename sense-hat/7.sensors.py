from sense_hat import SenseHat
from colors import Colors
import time

sense = SenseHat()

i = 0
c = Colors()
while i < 10:
    sense.show_message(f"{round(sense.temp, 1)}C", text_colour=c.get_rgb("red"))
    time.sleep(0.5)
    sense.show_message(f"{round(sense.pressure, 2)}P", text_colour=c.get_rgb("blue"))
    time.sleep(0.5)
    sense.show_message(f"{round(sense.humidity, 2)}H", text_colour=c.get_rgb("yellow"))
    i += 1
    time.sleep(0.5)
