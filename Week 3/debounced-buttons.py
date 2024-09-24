#debounced-buttons.py
import board, neopixel, time, digitalio
import adafruit_led_animation.color
from adafruit_led_animation.color import RED, YELLOW, ORANGE, GREEN, TEAL, \
    CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE, WHITE, BLACK
from adafruit_debouncer import Button

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
colors = [RED, YELLOW, ORANGE, GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE, WHITE, BLACK]

button_A_input = digitalio.DigitalInOut(board.BUTTON_A)
button_A_input.switch_to_input(digitalio.Pull.DOWN)
button_A = Button(button_A_input, value_when_pressed=True)

button_B_input = digitalio.DigitalInOut(board.BUTTON_B)
button_B_input.switch_to_input(digitalio.Pull.DOWN)
button_B = Button(button_B_input, value_when_pressed=True)

press_count_A = 0
press_count_B = 0

while True:
    button_B.update()
    button_A.update()
    if button_B.pressed:
        pixels.fill(RED)
        press_count_B += 1
        print(f"Press Count B: {press_count_B}")
    elif button_A.pressed:
        pixels.fill(BLUE)
        press_count_A += 1
        print(f"Press Count A: {press_count_A}")
    elif button_B.released:
        pixels.fill(BLACK)
    elif button_A.released:
        pixels.fill(BLACK)