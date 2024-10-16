# hid-press-and-layoutwrite-demo.py
import usb_hid, board, time, digitalio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

kbd.release_all()

button_A = digitalio.DigitalInOut(board.BUTTON_A)
button_A.switch_to_input(digitalio.Pull.DOWN)
button_B = digitalio.DigitalInOut(board.BUTTON_B)
button_B.switch_to_input(digitalio.Pull.DOWN)

while True:
    if button_A.value and button_B.value:
        kbd.press(Keycode.RETURN)
        kbd.release_all()
    elif button_A.value:
        layout.write("You are awesome!")
    elif button_B.value:
        layout.write("Fabulous? thats you!")
    time.sleep(0.2)