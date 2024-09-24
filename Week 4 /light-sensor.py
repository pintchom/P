#light-sensor.py
import board, time, analogio

# setup light sensor 
light_sensor = analogio.AnalogIn(board.LIGHT)
while True:
    print((light_sensor.value, ))
    time.sleep(0.2)