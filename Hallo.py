import board
import time
import neopixel


import sounddevice as sd
import librosa
import librosa.display
import numpy as np

pixels = neopixel.NeoPixel(board.D18, 12, brightness=0.1, auto_write=True)

audio_path = librosa.util.example_audio_file()

y, sr = librosa.load("Demo.wav",sr=None)    #sr = none damit die sample rate des Songs übernommen wird



tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

# 4. Convert the frame indices of beat events into timestamps
#beat_times = librosa.frames_to_time(beat_frames, sr=sr)
xyz = (60/12/150)
#print('Saving output to beat_times.csv')
#librosa.output.times_csv('beat_times.csv', beat_times)
pixels[0] = (100,100,100)
pixels[12] = (100,100,100)

#for i in range(12):
 #       pixels[i] = (100,100,100)
   #     time.sleep(xyz)     #Drehgeschwindigkeit
  #      pixels.show()
    #    pixels[i] = (0,0,0)



#sd.play(y,sr,blocking=True)







