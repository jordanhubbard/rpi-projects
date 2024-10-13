from sense_hat import SenseHat

sense = SenseHat()

red = [255, 0, 0]
blue = [0, 0, 255]
green = [0, 255, 0]
black = [0, 0, 0]
white = [255, 255, 255]

X = red
O = white

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
