# pulse-up-and-down.py
import board, neopixel, time
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
RED = (255,0,0)
BLACK = (0,0,0)
pixels.fill(RED)
print("RUNNING")
def pulse():
    for i in range(0, 101):
        pixels.brightness = i/100
        time.sleep(0.01)
    for i in range(100, -1, -1):
        pixels.brightness = i/100
        time.sleep(0.01)

while True:
    pulse()