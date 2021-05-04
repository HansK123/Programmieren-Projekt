from threading import Thread                    # Import der unterschiedlichen Libraries und Module
import board
import time
import neopixel
import sounddevice as sd
import librosa
import librosa.display
import numpy as np

y, sr = librosa.load("Beispiel2.wav",sr=None)    # sr = none damit die sample rate des Songs übernommen wird. y sind die Audiodaten

pixels = neopixel.NeoPixel(board.D18, 12, brightness=0.1, auto_write=True) # D18 ist der Pin des Raspberry, 12 die Anzahl der LED´s

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)        # Librosa Funktion zum erfassen des Tempos

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

def Licht():                                                   # Funktion für das LED Ringlicht zur visualisierung der BPM
        while True:                                            # While True damit das Ringlucht nicht nach einer Umdrehung stoppt
                for i in range(11):                # Ringdurchlauf des LED Rings
                        pixels[i] = (100, 100, 100)# Festlegung der LED Werte (in diesem Fall Weiß in mittlerer Intensität)
                        pixels.show()              # Befehl zum aktivieren der LEDs
                        time.sleep(60 / 12 / 150)  # Drehgeschwindigkeit Proberechnung um die BPM (in diesem Fall 150) darzustellen
                        pixels[i] = (0, 0, 0)      # Ausschalten der LED


def Musik():                                    # Funktion zum Abspielen des Songs
        sd.play(y, sr, blocking=False)          # Song abspielen mit Hilfe des Soundcard Moduls

if __name__ == '__main__':                      # Threading um beide Prozesse gleichzeitig laufen zu lassen
    Thread(target = Musik).start()              # Starten des Musik Threads
    Thread(target = Licht).start()              # Starten des Licht Threads




