#magnetic-switch-door-alarm-with-pico.py
import board, time, digitalio
from audiomp3 import MP3Decoder
import audiopwmio import PWMAudioOut as AudioOut

audio = AudioOut(board.GP16)
path = "alarm/"
filename = "siren.mp3"
mp3_file = open(path + filename, "rb")
decoder = MP3Decoder(mp3_file)

def play_mp3(filename):
    decoder.file = open(path + filename, "rb")
    audio.play(decoder)
    while audio.playing:
        pass

door_sensor = digitalio.DigitalInOut(board.GP14)
door_sensor.switch_to_input(pull=digitalio.Pull.UP)

led = digitalio.DigitalInOut(board.GP15)
led.switch_to_output()

while True:
    if door_sensor.value:
        print("DOOR OPEN")
        led.value = True
        play_mp3("siren.mp3")
    else:
        print("DOOR CLOSED")
        led.value = False
    time.sleep(0.25)
