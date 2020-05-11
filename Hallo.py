import board
import neopixel


import sounddevice as sd
import librosa
import librosa.display
import numpy as np

#pixels = neopixel.NeoPixel(board.D18, 12)

audio_path = librosa.util.example_audio_file()

y, sr = librosa.load("Demo.wav")



# 3. Run the default beat tracker
#tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

#print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

# 4. Convert the frame indices of beat events into timestamps
#beat_times = librosa.frames_to_time(beat_frames, sr=sr)

#print('Saving output to beat_times.csv')
#librosa.output.times_csv('beat_times.csv', beat_times)

sd.play(y,sr*2,blocking=True)
print(sr)

#pixels[0]=((245,255,0))
#time.sleep(5)
#pixels.fill((0,0,0))



