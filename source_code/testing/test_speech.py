import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
  audio = r.listen(source)
  test = r.recognize_google(audio)
  print(test)
