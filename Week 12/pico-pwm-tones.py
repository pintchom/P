#pico-pwm-tones.py
import board, time, pwmio

tone = pwmio.PWMOut(board.GP15, variable_frequency = True)
volume = 25
tone.duty_cycle = volume

notes = [262, 277, 294, 311, 330, 349, 370, 392, 410, 440, 466, 494]

tone_duration = 0.2
rest_duration = 0.01

def play_a_tone(freq, duration):
    tone.duty_cycle = volume
    tone.frequency = freq
    time.sleep(duration)

def play_a_rest(duration):
    tone.duty_cycle = 0
    time.sleep(duration)

for note in notes:
    play_a_tone(note, tone_duration)
    play_a_rest(rest_duration)
