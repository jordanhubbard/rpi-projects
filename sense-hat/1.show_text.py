from sense_hat import SenseHat
from colors import Colors

sense = SenseHat()
c = Colors()
sense.show_message("I love the Astro Pi!", text_colour=c.get_rgb("yellow"), back_colour=c.get_rgb("blue"))
