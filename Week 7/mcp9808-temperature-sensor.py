#mcp9808-temperature-sensor.py
import time, board, adafruit_mcp9808

i2c = board.I2C()
temp_sensor = adafruit_mcp9808.MCP9808(i2c)

print("Sensing Temperature")
while True:
   tempC = temp_sensor.temperature
   tempF = tempC * 9/5 + 32
   print(f"Temperature: {tempF:.2f}°F, {tempC:.2f}°C")
   time.sleep(1)