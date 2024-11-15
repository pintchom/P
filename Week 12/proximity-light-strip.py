#proximity-light-strip.py
import board, time, neopixel
from adafruit_apds9960.apds9960 import APDS9960

strip = neopixel.NeoPixel(board.GP16, 30)
i2c = board.STEMMA_I2C()
multi_sensor = APDS9960(i2c)
multi_sensor.enable_proximity = True

RED = (255,0,0)
BLACK = (0,0,0)

while True:
    reading = multi_sensor.proximity
    lights = round(reading * (30/255))
    if lights == 0:
        strip.fill(BLACK)
    else:
        strip[0: lights] = RED * lights
        strip[lights: 30] = BLACK * (30 - lights)
    print(f"Reading: {reading}, lights: {lights}")
    time.sleep(0.1)
