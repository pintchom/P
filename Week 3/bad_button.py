import board, neopixel, time, digitalio
import adafruit_led_animation.color
from adafruit_led_animation.color import RED, YELLOW, ORANGE, GREEN, TEAL, \
    CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE, WHITE, BLACK
from adafruit_debouncer import Button

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
colors = [RED, YELLOW, ORANGE, GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE, WHITE, BLACK]

button_A = digitalio.DigitalInOut(board.BUTTON_A)
button_A.switch_to_input(digitalio.Pull.DOWN)

button_B = digitalio.DigitalInOut(board.BUTTON_B)
button_B.switch_to_input(digitalio.Pull.DOWN)

press_count_A = 0
while_count = 0
press_count_B = 0

while True:
    if button_B.value:
        press_count_A += 1
        pixels.fill(RED)
        print(f"Press Count A: {press_count_A}")
    elif button_A.value:
        press_count_B += 1
        pixels.fill(BLUE)
        print(f"Press Count B: {press_count_B}")
    else:
        pixels.fill(BLACK)
    # while_count += 1
    # print(f"While count: {while_count}")