import board, neopixel, time, digitalio, touchio, audiomixer
from audiomp3 import MP3Decoder
from audiocore import WaveFile
try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        print("THIS BOARD DOES NOT SUPPORT AUDIO")
from adafruit_led_animation.color import RED, YELLOW, ORANGE, GREEN, TEAL, \
    CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE, WHITE, BLACK

colors = [RED, YELLOW, ORANGE, GREEN, TEAL, 
    CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE, WHITE, BLACK]

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5)

button_A = digitalio.DigitalInOut(board.BUTTON_A)
button_A.switch_to_input(pull=digitalio.Pull.UP)
button_B = digitalio.DigitalInOut(board.BUTTON_A)
button_B.switch_to_input(pull=digitalio.Pull.UP)

pads = [board.A1, board.A2, board.A3, board.A4, board.A5, board.A6, board.TX]
touchpads = []
for pad in pads:
    touchpads.append(touchio.TouchIn(pad))

speaker = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker.direction = digitalio.Direction.OUTPUT
speaker.value = True

audio = AudioOut(board.SPEAKER)
path = "sounds/"

mixer = audiomixer.Mixer(voice_count=1, sample_rate=22050, channel_count=1, bits_per_sample=16, samples_signed=True)
audio.play(mixer)

filename = "encouragement1.mp3"
mp3_file = open(path + filename, "rb")
decoder = MP3Decoder(mp3_file)

volume = 0

def play_mp3_voice(filename):
    decoder.file = open(path + filename, "rb")
    mixer.voice[0].play(decoder)
    while mixer.voice[0].playing:
        pass

while True:
    if button_A.value:
        if volume < len(pixels):
            volume += 1
            pixels[0:volume] = RED * volume
            pixels[volume:] = BLACK * (len(pixels) - volume)
        time.sleep(0.2)
    if button_B.value:
        if volume > 0:
            volume -= 1
            pixels[:] = [RED if i < volume else BLACK for i in range(len(pixels))]
        time.sleep(0.2)
    
    for i in range(len(touchpads)):
        if touchpads[i].value:
            print(f"Pad {i + 1} is touched")
            mixer.voice[0].level = volume / 10
            if volume > 0:
                play_mp3_voice("encouragement2.mp3")