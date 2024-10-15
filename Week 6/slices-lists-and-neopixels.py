import board, neopixel, time 
from adafruit_led_animation.color import RED, YELLOW, ORANGE, GREEN, TEAL, \
    CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE, WHITE, BLACK

colors = [RED, YELLOW, ORANGE, GREEN, TEAL, 
    CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE, WHITE, BLACK]

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5)
pixels[0:3] = RED, WHITE, BLUE
pixels[0:3] = BLUE * 3
pixels[7:10] = RED * 3
pixels[:] = GREEN * len(pixels)
pixels[-3:] = RED * 3
pixels[:-3] = BLUE * 7
pixels[:-3] = YELLOW * (len(pixels) - 3) 
pixels.fill(BLACK)
pixels[0:10:2] = MAGENTA * 5
pixels[1::2] = TEAL * (int(len(pixels) / 2))
pixels[1::2] = YELLOW * (len(pixels) // 2)
while True:
    pass
