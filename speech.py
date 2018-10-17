import speech_recognition as sr
import sounddevice as sd
print(sr.__version__)

r = sr.Recognizer()

ccp  = sr.AudioFile('audiodecifrar.wav')

with ccp as source:
    audio = r.record(source)

s = r.recognize_google(audio)
print(s)

