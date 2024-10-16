# hid-glove-mouse.py
import board, time, touchio, digitalio, busio, adafruit_lis3dh, analogio, math
import usb_hid
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)

i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
int1 = digitalio.DigitalInOut(board.ACCELEROMETER_INTERRUPT)
accelerometer = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19, int1=int1)
accelerometer.range = adafruit_lis3dh.RANGE_8_G

touchpad_A1 = touchio.TouchIn(board.A1)
touchpad_A2 = touchio.TouchIn(board.A2)

while True:
    x, y, z = accelerometer.acceleration
    x_move = int(math.pow(abs(x), 2.5))
    x_move = -x_move if x > 0 else x_move
    y_move = int(math.pow(abs(y), 3))
    y_move = -y_move if y < 0 else y_move
    
    mouse.move(x_move, y_move)

    if touchpad_A1.value:
        mouse.press(Mouse.LEFT_BUTTON)
    else:
        mouse.release(Mouse.LEFT_BUTTON)
    
    if touchpad_A2.value:
        mouse.press(Mouse.RIGHT_BUTTON)
    else:
        mouse.release(Mouse.RIGHT_BUTTON)

    time.sleep(0.05)