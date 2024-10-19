from sense_hat import SenseHat
from colors import Colors
import time

sense = SenseHat()
iterations = 50
c = Colors()

print("Orientation in degrees")
i = 0
while i < iterations:
    orientation_deg = sense.get_orientation_degrees()
    print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation_deg))
    i += 1
    time.sleep(0.1)

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

print("Accelerometer test")
i = 0
while i < iterations:
    accel_only = sense.get_accelerometer()
    print("p: {pitch}, r: {roll}, y: {yaw}".format(**accel_only))
    i += 1
    time.sleep(0.1)
