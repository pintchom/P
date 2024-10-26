#
import board, time, adafruit_mcp9808
i2c = board.STEMMA_I2C()
temp_sensor = adafruit_mcp9808.MCP9808(i2c)

while True:
    tempC = temp_sensor.temperature
    tempF = tempC * 9/5 + 32
    print(f"Temperature: {tempC:.2f}°C, {tempF:.2f}°F")
    time.sleep(0.5)