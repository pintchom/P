#VL53L1X-time-of-flight-distnace-sensor.py
import time, board, adafruit_vl53l1x

i2c = board.I2C()
distance_sensor = adafruit_vl53l1x.VL53L1X(i2c)
distance_sensor.start_ranging()
print("Sensing Distance")
while True:
   if distance_sensor.data_ready:
      distance = distance_sensor.distance
      if distance != None:
         inches = distance * 0.394
         print(f"{distance: .1f}cm, {inches: .1f}in, {inches/12:.1f}ft")
      else:
         print("****** NONE/INFINITY ******")
   distance_sensor.clear_interrupt()
   time.sleep(0.2)