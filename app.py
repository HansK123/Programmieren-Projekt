

import sounddevice as sd
import librosa
import librosa.display
import numpy as np

import matplotlib.pyplot as plt
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

y_speed = librosa.effects.time_stretch(y, 0.9)
y_pitched = librosa.effects.pitch_shift(y_speed, sr, n_steps=0)
sd.play(y_pitched,sr,blocking=True)
beat_frames lösen licht aus

#LED RING
	
sudo apt-get update
sudo apt-get install build-essential python-dev git scons swig  
  
git clone https://github.com/jgarff/rpi_ws281x.git
cd rpi_ws281x
scons

cd python
sudo python setup.py install

# LED strip configuration:
LED_COUNT = 12 # Number of LED pixels.
LED_PIN = 18 # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000 # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5 # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 100 # Set to 0 for darkest and 255 for brightest
LED_INVERT = False # True to invert the signal (when using NPN transistor level shift)
