#three-press-servo-moves.py
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
   if button_A.value and button_B.value:
      print("180°")
      servo_1.angle = 180
   elif button_A.value:
      print("0°")
      servo_1.angle = 0
   elif button_B.value:
      print("90°")
      servo_1.angle = 90
   time.sleep(0.2)

   