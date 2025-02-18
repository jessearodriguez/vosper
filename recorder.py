# import required libraries
import sounddevice as sd
import os
from scipy.io.wavfile import write
sd.default.device = "Line 2 (Virtual Audio Cable), Windows WASAPI"
import time

recording = sd.rec(int(0 * 44100), samplerate=44100, channels=2)
def record (secs):
    global recording
    recording = sd.rec(int(secs * 44100), samplerate=44100, channels=2)

def stop():
    global recording
    sd.stop()
    if os.path.exists("./vosper/speaker.wav"):
        os.remove("./vosper/speaker.wav")
    if os.path.exists("speaker.wav"):
        os.remove("speaker.wav")
    time.sleep(.5)
    write('speaker.wav',44100,recording)

