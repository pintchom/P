#pico-w-api-call.py
import os, time, ssl, wifi, socketpool, adafruit_requests
import board

wifi.radio.connect(os.getenv("WIFI_SSID"), os.getenv("WIFI_PASSWORD"))
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

url = "https://worldtimeapi.org/api/timezone/"
timezone = "America/New_York"
url = url+timezone

print(f"Accessing url: {url}")
response = requests.get(url)

print(f"The API returned the text: \n{response.text}")
