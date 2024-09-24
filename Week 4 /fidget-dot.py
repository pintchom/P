#fidget-dot.py
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
splat = "splat.wav"
light_position = -1

def play_sound(filename):
    with open(path + filename,"rb") as wave_file:
        wave = WaveFile(wave_file)
        audio.play(wave)
        while audio.playing:
            pass
def move_dot(position: int, direction: int, color):
    play_sound(splat)
    pixels[position] = BLACK
    position += direction
    if position > 9:
        position = 0
    elif position < 0:
        position = 9

    pixels[position] = color
    return position


while True:
    button_A.update()
    button_B.update()
    if button_B.pressed:
        light_position = move_dot(light_position, -1, BLUE)
    if button_A.pressed:
        light_position = move_dot(light_position, 1, RED)
