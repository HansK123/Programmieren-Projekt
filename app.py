

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

y_speed = librosa.effects.time_stretch(y, 0.9)
y_pitched = librosa.effects.pitch_shift(y_speed, sr, n_steps=0)
sd.play(y_pitched,sr,blocking=True)

# LED strip configuration:
LED_COUNT      = 12      # Number of LED pixels.
LED_PIN        = 13      # GPIO pin connected to the pixels (must support PWM!).
LED_CHANNEL    = 1       # PWM Channel must correspond to chosen LED_PIN PWM!
LED_FREQ_HZ    = 800000  #  LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 50     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

...

# Main program logic follows:
if __name__ == '__main__':
        # Create NeoPixel object with appropriate configuration.
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        # Intialize the library (must be called once before other functions).
        strip.begin()