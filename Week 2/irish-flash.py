import board, neopixel, time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
GREEN = (0, 255, 0)
WHITE = (255,255,255)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
print("Making Irish lights")
for _ in range(2):
    pixels.fill(GREEN)
    time.sleep(2.0)
    pixels.fill(WHITE)
    time.sleep(2.0)
    pixels.fill(ORANGE)
    time.sleep(2.0)
    pixels.fill(BLACK)
    time.sleep(2.0)