#wav-play.py
import board, neopixel, time, digitalio
import adafruit_led_animation.color
from adafruit_led_animation.color import RED, YELLOW, ORANGE, GREEN, TEAL, \
    CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE, WHITE, BLACK
from audiocore import WaveFile
try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        print("No audioIO")

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
colors = [RED, YELLOW, ORANGE, GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE, WHITE, BLACK]

#Audio setup
speaker = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker.direction = digitalio.Direction.OUTPUT
speaker.value = True

audio = AudioOut(board.SPEAKER)

#Setup path 
path = "drumSounds/"
filename = "drum_cowbell.wav"

with open(path + filename,"rb") as wave_file:
    wave = WaveFile(wave_file)
    audio.play(wave)
    while audio.playing:
        pass
