import pyaudio
import wave

FORMAT = pyaudio.paInt16

CHANNELS = 1
RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 3

audio = pyaudio.PyAudio()

# start Recording
stream = audio.open(format=FORMAT, channels=CHaANNELS,
            rate=RATE, input=True,
            frames_per_buffer=CHUNK)
print "recording..."
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print "finished recording"


# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

file = open("classtest.raw", "wb")
file.write(b''.join(frames))
file.close()