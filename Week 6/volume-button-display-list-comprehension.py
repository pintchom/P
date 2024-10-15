import board, neopixel, time, digitalio
from adafruit_led_animation.color import RED, YELLOW, ORANGE, GREEN, TEAL, \
    CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE, WHITE, BLACK

colors = [RED, YELLOW, ORANGE, GREEN, TEAL, 
    CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE, WHITE, BLACK]

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5)

button_A = digitalio.DigitalInOut(board.BUTTON_A)
button_A.switch_to_input(pull=digitalio.Pull.UP)
button_B = digitalio.DigitalInOut(board.BUTTON_A)
button_B.switch_to_input(pull=digitalio.Pull.UP)
# for i in range(len(pixels)):
#     pixels[i] = colors[i]

volume = 0

move = 0
while True:
    if button_A.value:
        if volume < len(pixels):
            volume += 1
            pixels[0:volume] = RED * volume
            pixels[volume:] = BLACK * (len(pixels) - volume)
        time.sleep(0.2)
    if button_B.value:
        if volume > 0:
            volume -= 1
            pixels[:] = [RED if i < volume else BLACK for i in range(len(pixels))]
        time.sleep(0.2)