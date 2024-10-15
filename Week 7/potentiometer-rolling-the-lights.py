#potentiometer-rolling-the-lights.py
import time, board, neopixel
from analogio import AnalogIn
from adafruit_led_animation.color import RED, YELLOW, ORANGE, GREEN, TEAL, \
    CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE, WHITE, BLACK


potentiometer = AnalogIn(board.A3)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
number_of_options = 11
max_reading = 65535

while True:
   val = potentiometer.value
   lights_on = int(val * (number_of_options / max_reading))
   print(f"Number of lights to turn on: {lights_on}, reading: {val}")
   
   pixels[0:lights_on] = BLUE * lights_on
   pixels[lights_on:] = BLACK * (10 - lights_on)
   time.sleep(0.1)