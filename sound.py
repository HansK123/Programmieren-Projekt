"""PyAudio Example: Play a wave file (callback version)"""
import pyaudio
import wave
import time
#import syshaw

#if len(sys.argv) < 2:                                                          #Auskommentiert um kein Argument zu benötigen
#    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
#    sys.exit(-1)

wf = wave.open("Demo.wav", 'rb')
p = pyaudio.PyAudio()
def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=callback)
stream.start_stream()
while stream.is_active():
    time.sleep(0.1)
stream.stop_stream()
stream.close()
wf.close()

p.terminate()