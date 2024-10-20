from sense_hat import SenseHat
from colors import Colors
import time

sense = SenseHat()
iterations = 10
c = Colors()

print("Compass orientation")
i = 0
while i < iterations:
    direction = sense.get_compass()
    print("North: %s" % direction)
    match direction:
      case 0:
        sense.show_letter('N')
      case 90:
        sense.show_letter('E')
      case 180:
        sense.show_letter('S')
      case 270:
        sense.show_letter('W')
      case _:
        sense.show_message(f"{round(direction,0)}")
    i += 1
