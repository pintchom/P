#non-repeating-random-sparkly.py
import board, time, neopixel, random

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.4)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
last_light = -1

while True:
    random_light = random.randrange(len(pixels))
    while random_light == last_light:
        random_light = random.randrange(len(pixels))
    last_light = random_light
    print(last_light)
    pixels[last_light] = WHITE
    time.sleep(0.1)
    pixels[last_light] = BLACK
    time.sleep(0.1)

