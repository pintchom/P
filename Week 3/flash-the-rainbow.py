import board, neopixel, time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

RED = (255, 0, 0)
ORANGE = (255, 40, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
INDIGO = (75, 0, 130)
VIOLET = (180, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

time_interval = 0.5

rainbow_colors = [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET]
rainbow_colors.append(CYAN)

while True:
    for color in rainbow_colors:
        pixels.fill(color)
        time.sleep(time_interval)
    
