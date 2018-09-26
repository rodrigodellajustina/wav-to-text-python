import speech_recognition as sr
print(sr.__version__)

r = sr.Recognizer()

ccp  = sr.AudioFile('audio.wav')

with ccp as source:
    audio = r.record(source)

s = r.recognize_google(audio)
print(s)

