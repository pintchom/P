#function-with-arguments-and-return-values.py
import board, neopixel, time, digitalio
import adafruit_led_animation.color
from adafruit_debouncer import Button
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

#Button setup
button_A_input = digitalio.DigitalInOut(board.BUTTON_A)
button_A_input.switch_to_input(digitalio.Pull.DOWN)
button_A = Button(button_A_input, value_when_pressed=True)

button_B_input = digitalio.DigitalInOut(board.BUTTON_B)
button_B_input.switch_to_input(digitalio.Pull.DOWN)
button_B = Button(button_B_input, value_when_pressed=True)

#Audio setup
speaker = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker.direction = digitalio.Direction.OUTPUT
speaker.value = True

audio = AudioOut(board.SPEAKER)

#Setup path 
path = "drumSounds/"
cowbell = "drum_cowbell.wav"
scratch = "scratch.wav"
times_pressed = 0

def play_sound(filename, press_count):
    # global times_pressed
    # times_pressed += 1
    # print(f"Times pressed: {times_pressed}")
    press_count += 1
    print(press_count)
    with open(path + filename,"rb") as wave_file:
        wave = WaveFile(wave_file)
        audio.play(wave)
        while audio.playing:
            pass
    return press_count

while True:
    button_A.update()
    button_B.update()
    if button_B.pressed:
        times_pressed = play_sound(cowbell,times_pressed)
    if button_A.pressed:
        times_pressed = play_sound(scratch,times_pressed)
