# Beat tracking example
#import playsound
import librosa
import sounddevice as sd

# 1. Get the file path to the included audio example
filename = librosa.util.example_audio_file()

# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load("Demo.wav",sr=None)    # sr = none damit die sample rate des Songs übernommen wird

# 3. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))


# 4. Convert the frame indices of beat events into timestamps
sd.play(y,sr,blocking=True)
