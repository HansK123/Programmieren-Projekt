import pyaudio
p = pyaudio.PyAudio()

print ('\n'.join([y['name'] for y in [p.get_device_info_by_index(x) for x in range(p.get_device_count())]]))