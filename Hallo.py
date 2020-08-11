import board
import time
import neopixel
import sounddevice as sd
import librosa
import librosa.display
import numpy as np

y, sr = librosa.load("Demo.wav",sr=None)    # sr = none damit die sample rate des Songs übernommen wird

pixels = neopixel.NeoPixel(board.D18, 12, brightness=0.1, auto_write=True) # D18 ist der Pin des Raspberry, 12 die Anzahl der LED´s

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)        # Librosa funktion zum feststellen des Tempos

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

def Licht():                                                   #Funktion für das LED Ringlicht zur visualisierung der BPM
        while True:                                             #While True damit das Ringlucht nicht nach einer Umdrehung stoppt. Noch keine                                                      #
                for i in range(11):                             #bessere Lösung gefunden
                        pixels[i] = (100, 100, 100)
                        pixels.show()
                        time.sleep(60 / 12 / 150)  # Drehgeschwindigkeit Proberechnung um die BPM (in diesem Fall 150) über das Ringlicht darzustellen
                        pixels[i] = (0, 0, 0)


def Musik():                                    # Funktion zum Abspielen des Songs
        sd.play(y, sr, blocking=True)


Musik()
Licht()








# 4. Convert the frame indices of beat events into timestamps
#beat_times = librosa.frames_to_time(beat_frames, sr=sr)
#print('Saving output to beat_times.csv')
#librosa.output.times_csv('beat_times.csv', beat_times)













