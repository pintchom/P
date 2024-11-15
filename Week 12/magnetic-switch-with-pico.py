#magnetic-switch-with-pico.py
import board, time, digitalio

door_sensor = digitalio.DigitalInOut(board.GP14)
door_sensor.switch_to_input(pull=digitalio.Pull.UP)

while True:
    if door_sensor.value:
        print("DOOR OPEN")
    else:
        print("DOOR CLOSED")
    time.sleep(0.25)
