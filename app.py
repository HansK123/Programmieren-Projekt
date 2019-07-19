import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 30)

import sounddevice as sd
import librosa
import librosa.display
import numpy as np


import matplotlib.style as ms
ms.use('seaborn-muted')


audio_path = librosa.util.example_audio_file()

y, sr = librosa.load("Beispiel2.wav")



# 3. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

# 4. Convert the frame indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

print('Saving output to beat_times.csv')
librosa.output.times_csv('beat_times.csv', beat_times)

y_speed = librosa.effects.time_stretch(y, 3)
y_pitched = librosa.effects.pitch_shift(y_speed, sr, n_steps=0)
sd.play(y_pitched,sr,blocking=True)

pixels[y_speed]=((255, 0, 0))