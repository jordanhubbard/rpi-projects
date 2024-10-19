from sense_hat import SenseHat
from colors import Colors
import time

sense = SenseHat()

i = 0
c = Colors()
while i < 10:
    temp = sense.get_temperature()
    pressure = sense.get_pressure()
    humidity = sense.get_humidity()

    print(f"Temperature: {round(temp, 1)}C ({round(temp * (9 / 5) + 32, 1)}F)")
    print(f"Pressure: {round(pressure, 2)} Mbar ({round(pressure * 0.02953, 2)} in)")
    print("Humidity: %s" % round(humidity, 2))

    sense.show_message(f"{round(temp, 1)}C", text_colour=c.get_rgb("red"))
    sense.show_message(f"{round(pressure, 2)}Mbar", text_colour=c.get_rgb("blue"))
    sense.show_message(f"{round(humidity, 2)}H", text_colour=c.get_rgb("yellow"))
    i += 1
    time.sleep(0.5)
