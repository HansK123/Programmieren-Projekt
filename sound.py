# Beat tracking example
from __future__ import print_function
import librosa
import sounddevice as sd

# 1. Get the file path to the included audio example
filename = "Beispiel2.wav"

# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load(filename)

# 3. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

# 4. Convert the frame indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

sd.play(y,sr,blocking=FALSE)
