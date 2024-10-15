#Potentiometer.py
import time, board
from analogio import AnalogIn
potentiometer = AnalogIn(board.A3)

print("Potentiometer Code Running!")
while True:
   print(potentiometer.value)
   time.sleep(0.25)