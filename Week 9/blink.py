#blink.py
import board, time, digitalio, neopixel

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
# led = digitalio.DigitalInOut(board.LED)
# led.direction = digitalio.Direction.OUTPUT

while True:
    # led.value = True
    # time.sleep(0.25)
    # led.value = False
    # time.sleep(0.25)
    pixel.fill((255, 0, 0))
    time.sleep(0.25)
    pixel.fill((0, 0, 255))
    time.sleep(0.25)