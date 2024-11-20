import board, time, busio, sdcardio, storage

sck = board.GP10
si = board.GP11
so = board.GP12
cs = board.GP13

spi = busio.SPI(sck, si, so)
sdcard = sdcardio.SDCard(spi,cs)

vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

from audiomp3 import MP3Decoder
from audiopwmio import PWMAudioOut as AudioOut
audio = AudioOut(board.GP15)


path = "/sd/robot_sounds/"

filename = "0.mp3"
mp3_file = open(path + filename, "rb")
decoder = MP3Decoder(mp3_file)

def play_mp3(filename):
    decoder.file = open(path + filename, "rb")
    audio.play(decoder)
    while audio.playing:
        pass

for i in range(13):
    filename = f"{i}.mp3"
    print(f"playing {filename}")
    play_mp3(filename)
