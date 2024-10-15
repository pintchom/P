#random-sparkly.py
import board, time, neopixel, random

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

while True:
    random_light = random.randrange(len(pixels))
    print(random_light)
    pixels[random_light] = WHITE
    time.sleep(0.1)
    pixels[random_light] = BLACK
    time.sleep(0.1)

