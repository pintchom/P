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

move = 0
while True:
    if button_A.value:
        move = 1
    if button_B.value:
        move = -1
    if move == 1:
        temp = pixels[9]
        pixels[1:10] = pixels[0:9]
        pixels[0] = temp
        time.sleep(0.1)
    elif move == -1:
        temp = pixels[0]
        pixels[0:9] = pixels[1:10]
        pixels[9] = temp
        time.sleep(0.1)