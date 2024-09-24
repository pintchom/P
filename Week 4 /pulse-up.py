# pulse-up.py
import board, neopixel, time
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
RED = (255,0,0)
BLACK = (0,0,0)
pixels.fill(RED)
print("RUNNING")
while True:
    for i in range(0, 101):
        pixels.brightness = i/100