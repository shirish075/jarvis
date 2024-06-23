import pyttsx3
import speech_recognition as sr
from playsound import playsound
from vosk import Model, KaldiRecognizer

try:
    import requests
except:
    print("no internet cannot work properly")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 1.0)
engine.setProperty('rate', 140)

r = sr.Recognizer()


# ---configured speech recognition-------

def speak(tex: object) -> object:
    engine.say(tex)
    print(tex)
    engine.runAndWait()


import pyaudio

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()
text = ''
model = Model(r'E:\project\vosk-model-en-us-0.22-lgraph')
rec = KaldiRecognizer(model, 16000)


def listen_offline():
    print("listening...at offline")
    playsound(r'E:\project\listening.wav')
    while True:
        data = stream.read(4090, exception_on_overflow=False)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            results = rec.Result()
            text = results[14:-3]
            print(f"you said {text}")
            if len(text) > 0:
                return str(text).lower().replace("jarvis", "")
            else:
                return (str(" "))


def listen_online():
    playsound(r'E:\project\listening.wav')
    with sr.Microphone() as source:
        print("listening... at onlinee")
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 0, 4)
    try:
        print("recognising...")
        query = r.recognize_google(audio, language='en-in')
        query = str(query.lower()).replace("jarvis", "")
        print(f"query is {query}")
        return str(query)
    except Exception as err:
        print(f"error is at take command exception {err}")
        return str(" ")


def test_recogniser():
    c = internet_test()
    if c is not None:
        return listen_online()
    else:
        return listen_offline()


def internet_test():
    try:
        ok = requests.get(url="http://www.google.com")

        return (ok)
    except:
        ok = None

        return ok
