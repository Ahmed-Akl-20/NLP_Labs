import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.AudioFile() as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio)

    print("You said:", text)

except sr.UnknownValueError:
    print("Could not understand audio")