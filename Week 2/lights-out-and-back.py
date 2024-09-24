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
    green = True
    for i in range(0, len(pixels), 2):
        pixels[i] = GREEN
        time.sleep(0.2)
        pixels[i+1] = ORANGE
        time.sleep(0.2)
    for i in range(len(pixels)-1, -1, -1):
        pixels[i] = BLACK
        time.sleep(0.2)
    time.sleep(0.2)