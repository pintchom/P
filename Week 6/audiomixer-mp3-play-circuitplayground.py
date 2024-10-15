import board, digitalio, audiomixer
from audiomp3 import MP3Decoder
from audiocore import WaveFile
try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        print("THIS BOARD DOES NOT SUPPORT AUDIO")


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

button_A = digitalio.DigitalInOut(board.BUTTON_A)
button_A.switch_to_input(pull=digitalio.Pull.UP)
button_B = digitalio.DigitalInOut(board.BUTTON_B)
button_B.switch_to_input(pull=digitalio.Pull.UP)

def play_mp3_voice(filename):
    decoder.file = open(path + filename, "rb")
    mixer.voice[0].play(decoder)
    while mixer.voice[0].playing:
        pass

play_mp3_voice("encouragement1.wav")
mixer.voice[0].level = 0.25
play_mp3_voice("encouragement2.wav")

while True:
    if button_A.value:
        play_mp3_voice("encouragement1.mp3")
    if button_B.value:
        play_mp3_voice("encouragement2.mp3")
