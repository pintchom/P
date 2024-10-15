import board, neopixel, time 
from adafruit_led_animation.color import RED, YELLOW, ORANGE, GREEN, TEAL, \
    CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE, WHITE, BLACK

colors = [RED, YELLOW, ORANGE, GREEN, TEAL, 
    CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE, WHITE, BLACK]

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5)

# for i in range(len(pixels)):
#     pixels[i] = colors[i]

pixels[:] = [colors[i] for i in range(len(pixels))]

while True:
    temp = pixels[9]
    pixels[1:10] = pixels[0:9]
    pixels[0] = temp
    time.sleep(0.1)