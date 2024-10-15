#Accelerometer.py
import board, time, busio, adafruit_lis3dh

i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
int1 = digitalio.DigitalInOut(board.ACCELEROMETER_INTERRUPT)
motion = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19, int1 = int1)
motion.range = adafruit_lis3dh.RANGE_8_G

motion.range = adafruit_lis3dh.RANGE_2_G
while True:
   x, y, z = motion.acceleration
   print(f"X: {x:.2f}, Y: {y:.2f}, Z: {z:.2f}")
   time.sleep(0.1)