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


# flip twice in each direction
i = 0
while i < 4:
    print("two horizontal flips")
    sense.flip_h()
    time.sleep(0.5)
    sense.flip_h()
    time.sleep(0.5)
    print("two vertical flips")
    sense.flip_v()
    time.sleep(0.5)
    sense.flip_v()
    time.sleep(0.5)
    i += 1
