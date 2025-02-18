# VOSK + Whisper speech recognition system
'''This module utilizes vosk as user feedback as wel as VAD solution
    While it uses OpenAI whisper for actual transcription.'''

import os, pyaudio, whisper
from vosper import recorder
from vosk import SetLogLevel, Model, KaldiRecognizer
SetLogLevel(-1)
import time
import datetime

whisp = whisper.load_model("small", "cuda")

recording_whisper = False
readytts = True
timecheck = datetime.datetime.now()


def load (model):
    # load vosk model
    model_voice = Model("./vosper/models/vosk/"+model)
    recognizer = KaldiRecognizer(model_voice, 16000)
    
    return recognizer

def Stream(listening=True):
    mic = pyaudio.PyAudio()
    # microphone streaming
    stream = mic.open(
        channels=1, 
        rate=16000, 
        input=True,
        format=pyaudio.paInt16,
        frames_per_buffer=4096,
        input_device_index=4
    )
    stream.start_stream()
    
    return stream

def listen (data, recognizer, listenCD):
    global recording_whisper
    global readytts
    global timecheck

    data = data.read(4096)
    if recognizer.AcceptWaveform(data):
        #print(f"{readytts}")
        recorder.stop()
        text = recognizer.Result()[14:-3]
        #teststr = time.strftime("%H:%M:%S", time.localtime())
        #print(text + f"{teststr}")
        whipsrtext = ""
        delta = datetime.datetime.now() - timecheck
        

        if (len(text) > 3) and readytts:
            print("Transcribing...\n")
            whipsrtext = whisp.transcribe('speaker.wav')['text'].strip()
            if whipsrtext.isspace(): return None
            recording_whisper = False
            readytts = False
            timecheck = datetime.datetime.now()
            listenCD.clear()
            return whipsrtext
        recording_whisper = False

        if (delta.total_seconds() > 6) and (readytts == False): 
            #print(delta.total_seconds())
            readytts=True
            listenCD.set()
            #print(f"{readytts}")

    else:
        if (recording_whisper == False):
            recorder.stop()
            recording_whisper = True
            recorder.record(5)
    
