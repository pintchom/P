import board, neopixel, time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
GREEN = (0, 255, 0)
WHITE = (255,255,255)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
RED = (255,0,0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (75,0,130)
VIOLET = (143, 0, 255)

while True:
    pixels[0] = RED
    pixels[1] = RED
    pixels[2] = RED
    pixels[3] = RED
    pixels[4] = RED
    pixels[5] = BLUE
    pixels[6] = BLUE
    pixels[7] = BLUE
    pixels[8] = BLUE
    pixels[9] = BLUE