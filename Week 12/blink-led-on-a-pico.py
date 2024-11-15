#blink-led-on-a-pico.py
import board, time, digitalio

led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.25)
    led.value = False
    time.sleep(0.25)
