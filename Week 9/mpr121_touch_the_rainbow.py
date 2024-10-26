# mpr121_touch_the_rainbow.py

import board, adafruit_mpr121, neopixel
from adafruit_debouncer import Button
from adafruit_led_animation.color import RED, YELLOW, ORANGE, GREEN, TEAL, \
    CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE, WHITE, BLACK

colors = [RED, YELLOW, ORANGE, GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE, WHITE, BLACK]
strip = neopixel.NeoPixel(board.GP16, 30)
i2c = board.STEMMA_I2C()
touch_pad = adafruit_mpr121.MPR121(i2c)

pads = []
for t_pad in touch_pad:
    pads.append(Button(t_pad, value_when_pressed=True))

while True:
    for i in range(len(pads)):
        pads[i].update()
        if pads[i].pressed:
            print(f"You touched pad {i}!")
            strip.fill(colors[i])
        if pads[i].released:
            strip.fill(BLACK)
    time.sleep(0.1)


# while True:
#     touched = False
#     for i in range(12):
#         if touch_pad[i].value:
#             print(f"You touched pad #{i}!")
#             strip.fill(colors[i])
#             touched = True
#     if not touched:
#         strip.fill(BLACK)




