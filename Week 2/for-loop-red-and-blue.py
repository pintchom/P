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

for i in range(5):
    pixels[i] = RED
for i in range(5,10):
    pixels[i] = BLUE
while True:
    pass