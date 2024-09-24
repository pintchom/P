import board, neopixel, time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
strip = neopixel.NeoPixel(board.A1, 30)

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
    for i in range(0, 30, 2):
        strip[i] = GREEN
        time.sleep(0.1)
        strip[i+1] = ORANGE
        time.sleep(0.1)
    for i in range(29, -1, -1):
        strip[i] = BLACK
        time.sleep(0.1)
        
    time.sleep(0.5)
