import board, time, neopixel
import os, ssl, socketpool, wifi
import adafruit_minimqtt.adafruit_minimqtt as MQTT

strip = neopixel.NeoPixel(board.GP15, 30)
RED = (255,0,0)
BLACK = (0,0,0)
strip.fill(BLACK)

aio_username = os.getenv("AIO_USERNAME")
aio_key = os.getenv("AIO_KEY")

strip_on_off_feed = aio_username + "/feeds/strip_on_off"

def connected(client, userdata, flags, rc):
    print("Connected!")
    client.subscribe(strip_on_off_feed)

def disconnected(client, userdata, rc):
    print("Disconnected!")

def message(client, topic, message):
    print(f"topic: {topic}, message: {message}")
    if message == "ON":
        strip.fill(RED)
    elif message == "OFF":
        strip.fill(BLACK)

print("Connected to WIFI...")
wifi.radio.connect(os.getenv("WIFI_SSID"), os.getenv("WIFI_PASSWORD"))
print("CONNCETED to WIFI!")
pool = socketpool.SocketPool(wifi.radio)

mqtt_client = MQTT.MQTT(
    broker = os.getenv("BROKER"),
    port = os.getenv("PORT"),
    username = aio_username,
    socket_pool = pool,
    ssl_context = ssl.create_default_context(),
)

mqtt_client.on_connect = connected
mqtt_client.on_disconnect = disconnected
mqtt_client.on_message = message

print("Connecting to ADAFRUIT IO")
mqtt_client.connect()

while True:
    mqtt_client.loop()
