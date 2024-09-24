#Max Pintchouk

import board, neopixel, time
import digitalio
from adafruit_debouncer import Button
from adafruit_led_animation.color import (
    AMBER, #(255, 100, 0)
    AQUA, # (50, 255, 255)
    BLACK, #OFF (0, 0, 0)
    BLUE, # (0, 0, 255)
    CYAN, # (0, 255, 255)
    GOLD, # (255, 222, 30)
    GREEN, # (0, 255, 0)
    JADE, # (0, 255, 40)
    MAGENTA, #(255, 0, 20)
    OLD_LACE, # (253, 245, 230)
    ORANGE, # (255, 40, 0)
    PINK, # (242, 90, 255)
    PURPLE, # (180, 0, 255)
    RED, # (255, 0, 0)
    TEAL, # (0, 255, 120)
    WHITE, # (255, 255, 255)
    YELLOW, # (255, 150, 0)
    RAINBOW # a list of colors to cycle through
)

INDIGO = (63, 0, 255)
VIOLET = (127, 0, 255)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

button_A_input = digitalio.DigitalInOut(board.BUTTON_A)
button_A_input.switch_to_input(digitalio.Pull.DOWN) # Note: Pull.UP for external buttons
button_A = Button(button_A_input, value_when_pressed = True) # NOTE: False for external buttons

button_B_input = digitalio.DigitalInOut(board.BUTTON_B)
button_B_input.switch_to_input(digitalio.Pull.DOWN) # Note: Pull.UP for external buttons
button_B = Button(button_B_input, value_when_pressed = True) # NOTE: False for external buttons



def flash(color):
    pixels.brightness = 0
    pixels.fill(color)

    while True:
        button_A.update()
        button_B.update()
        for i in range(51):
            pixels.brightness = i/100
        for i in range(50, -1, -1):
            pixels.brightness = i/100
        if button_A.pressed or button_B.pressed:
            break
    pixels.fill(BLACK)
    pixels.brightness = 1

redCounter = -1
blueCounter = 10
while True:
    button_A.update()
    button_B.update()
    if button_A.pressed:
        redCounter += 1
        pixels[redCounter] = RED
    if button_B.pressed:
        blueCounter -= 1
        pixels[blueCounter] = BLUE
    if redCounter == 5:
        flash(RED)
        blueCounter, redCounter = 10, -1
    if blueCounter == 4:
        flash(BLUE)
        blueCounter, redCounter = 10, -1
    

