import board
import time
import neopixel
from threading import Thread

import sounddevice as sd
import librosa
import librosa.display
import numpy as np

y, sr = librosa.load("Demo.wav",sr=None)    #sr = none damit die sample rate des Songs übernommen wird

pixels = neopixel.NeoPixel(board.D18, 12, brightness=0.1, auto_write=True)

audio_path = librosa.util.example_audio_file()

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))


def Licht():
        while True:
                for i in range(11):
                        pixels[i] = (100, 100, 100)
                        pixels.show()
                        time.sleep(60 / 12 / 150)  # Drehgeschwindigkeit
                        pixels[i] = (0, 0, 0)


def Musik():
        sd.play(y, sr, blocking=True)



#Licht()
#Musik()

#if __name__ == '__main__':

Thread(target = Musik()).start()
Thread(target = Licht()).start()



# 4. Convert the frame indices of beat events into timestamps
#beat_times = librosa.frames_to_time(beat_frames, sr=sr)
#print('Saving output to beat_times.csv')
#librosa.output.times_csv('beat_times.csv', beat_times)













