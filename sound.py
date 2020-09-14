import time
import multiprocessing
import board
import neopixel
import sounddevice as sd
import librosa
import librosa.display
import numpy as np

y, sr = librosa.load("Demo.wav",sr=None)    # sr = none damit die sample rate des Songs übernommen wird

pixels = neopixel.NeoPixel(board.D18, 12, brightness=0.1, auto_write=True) # D18 ist der Pin des Raspberry, 12 die Anzahl der LED´s

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)        # Librosa funktion zum feststellen des Tempos

#print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

def Ringlicht():                                                   #Funktion für das LED Ringlicht zur visualisierung der BPM
        while True:                                             #While True damit das Ringlucht nicht nach einer Umdrehung stoppt. Noch keine                                                      #
                for i in range(11):                             #bessere Lösung gefunden
                        pixels[i] = (100, 100, 100)
                        pixels.show()
                        time.sleep(60 / 12 / 150)  # Drehgeschwindigkeit Proberechnung um die BPM (in diesem Fall 150) über das Ringlicht darzustellen
                        pixels[i] = (0, 0, 0)


def musik_abspielen():                                    # Funktion zum Abspielen des Songs
        sd.play(y, sr, blocking=True)



p1 = multiprocessing.Process(target=musik_abspielen,args=[])
p2 = multiprocessing.Process(target=ringlicht,args=[])

if __name__ == '__main__':
    p1.start()
    p2.start()
    p1.join()
    p2.join()


print("Fertig mit durchlauf nach")