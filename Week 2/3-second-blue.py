import board, neopixel, time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
BLUE = (0, 0, 255)
print("Making lights blue")
pixels.fill(BLUE)
time.sleep(5.0)