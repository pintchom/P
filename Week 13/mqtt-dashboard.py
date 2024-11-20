import board, time, neopixel, pwmio
import os, ssl, socketpool, wifi
import adafruit_minimqtt.adafruit_minimqtt as MQTT
from adafruit_motor import servo

pwm = pwmio.PWMOut(board.GP14, frequency = 50)
servo_1 = servo.Servo(pwm, min_pulse=650, max_pulse=2400)
servo_1.angle = 0

from audiopwmio import PWMAudioOut as AudioOut
from audiomp3 import MP3Decoder

audio = AudioOut(board.GP16)
path = "/sounds/"
filename = "encouragement1.mp3"
mp3_file = open(path + filename, "rb")
decoder = MP3Decoder(mp3_file)

def play_mp3(filename):
    decoder.file = open(path + filename, "rb")
    audio.play(decoder)

strip = neopixel.NeoPixel(board.GP15, 30)
RED = (255,0,0)
BLACK = (0,0,0)
strip.fill(BLACK)
strip_color = RED

aio_username = os.getenv("AIO_USERNAME")
aio_key = os.getenv("AIO_KEY")

strip_on_off_feed = aio_username + "/feeds/strip_on_off"
color_feed = aio_username + "/feeds/color_feed"
sounds_feed = aio_username + "/feeds/sounds_feed"
servo_feed = aio_username + "/feeds/servo_feed"

def connected(client, userdata, flags, rc):
    print("Connected!")
    client.subscribe(strip_on_off_feed)
    client.subscribe(color_feed)
    client.subscribe(sounds_feed)
    client.subscribe(servo_feed)

def disconnected(client, userdata, rc):
    print("Disconnected!")

def message(client, topic, message):
    global strip_color
    print(f"topic: {topic}, message: {message}")
    if topic == strip_on_off_feed: # on/off toggled
        if message == "ON":
            strip.fill(strip_color)
            strip.brightness = 1.0
        elif message == "OFF":
            strip.fill(BLACK)
            strip.brightness = 0.0
    elif topic == color_feed:
        if message[0] == "#":
            message = message[1:]
            strip_color = int(message, 16)
            strip.fill(strip_color)
    elif topic == sounds_feed:
        if message != "0":
            play_mp3(message)
    elif topic == servo_feed:
        servo_1.angle = int(message)


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

mqtt_client.publish(strip_on_off_feed + "/get", "")
mqtt_client.publish(color_feed + "/get", "")
mqtt_client.publish(servo_feed + "/get", "")

while True:
    mqtt_client.loop()
