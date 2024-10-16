# hid-circuitplayground-touchpad-keyboard.py
import usb_hid, board, time, digitalio, touchio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

kbd.release_all()

keys = [Keycode.UP_ARROW, Keycode.DOWN_ARROW, Keycode.RETURN, Keycode.SPACE, "A", "b", "This is cool"]
pads = [board.A1, board.A2, board.A3, board.A4, board.A5, board.A6, board.TX]
touchpads = [touchio.TouchIn(pad) for pad in pads]

while True:
    for i in range(len(touchpads)):
        if touchpads[i].value:
            if isinstance(keys[i], str):
                layout.write(keys[i])
            else:
                kbd.press(keys[i])
                kbd.release_all()
            while touchpads[i].value:
                pass
            
