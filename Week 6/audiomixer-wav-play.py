import board, digitalio, audiomixer

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

def play_voice(filename): 
    wave = WaveFile(open(path + filename, "rb"))
    mixer.voice[0].play(wave, loop=False)
    while mixer.voice[0].playing:
        pass

play_voice("encouragement1.wav")
mixer.voice[0].level = 0.25
play_voice("encouragement2.wav")
