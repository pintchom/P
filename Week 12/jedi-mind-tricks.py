#jedi-mind-tricks.py
import board, time
from adafruit_apds9960.apds9960 import APDS9960
from audiocore import WaveFile

i2c = board.STEMMA_I2C()
multi_sensor = APDS9960(i2c)
multi_sensor.enable_proximity = True
multi_sensor.enable_gesture =  True

from audiopwmio import PWMAudioOut as AudioOut

audio = AudioOut(board.GP15)

def playSound(filename):
    with open(filename, 'rb') as wave_file:
        wave = WaveFile(wave_file)
        audio.play(wave)
        while audio.playing:
            pass


while True:
    gesture = multi_sensor.gesture()
    if gesture == 3:
        print("left")
        playSound("not-the-droids.wav")
    elif gesture == 4:
        print("right")
        playSound("no-id.wav")
    time.sleep(0.1)
