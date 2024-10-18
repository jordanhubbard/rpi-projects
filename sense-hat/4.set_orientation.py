from sense_hat import SenseHat
from colors import Colors
import time

sense = SenseHat()
c = Colors()

X = c.get_rgb("red")
O = c.get_rgb("white")

question_mark = [
O, O, O, X, X, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, O, O, X, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O
]

sense.set_pixels(question_mark)


# Twirl 5 times
i = 0
while i < 5:
    for rot in [0, 90, 180, 270]:
        print(f"Set orientation to {rot} degrees")
        sense.set_rotation(rot)
        time.sleep(0.5)
    i += 1
    sense.set_rotation(0)
