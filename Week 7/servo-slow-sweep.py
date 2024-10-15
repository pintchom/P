#servo-slow-sweep.py
import time, board, pwmio, digitalio
from adafruit_motor import servo
from adafruit_led_animation.color import RED, YELLOW, ORANGE, GREEN, TEAL, \
    CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE, WHITE, BLACK

pwm = pwmio.PWMOut(board.A2, frequency=50)
servo_1 = servo.Servo(pwm, max_pulse=2500)
servo_1.angle = 0

button_A = digitalio.DigitalInOut(board.BUTTON_A)
button_A.switch_to_input(digitalio.Pull.DOWN)

button_B = digitalio.DigitalInOut(board.BUTTON_B)
button_B.switch_to_input(digitalio.Pull.DOWN)

while True:
   for angle in range(0, 181, 5):
      servo_1.angle = angle
      time.sleep(0.05)
   time.sleep(0.5)
   for angle in range(180, -1, -5):
      servo_1.angle = angle
      time.sleep(0.05)
   time.sleep(0.5)
   
         
   