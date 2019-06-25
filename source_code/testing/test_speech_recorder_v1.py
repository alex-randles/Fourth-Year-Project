## System freezes when recording audio directly from microphone using pythons speech recognition 
## Recording a fixed length audio file will not be sufficent enough as recording length should be variable length
## This is a test to use sox to record audio while the user is speaking then convert it using the python speech recognition package
## V1 testing sensitivty for silenece 
import os, speech_recognition as SR

os.system("sox -d recording.wav silence 1 5 8% 1 0:00:01 8%")  


# record audio from the microphone
speechRecognizer = SR.Recognizer()
with SR.AudioFile("recording.wav") as source:
     audio = speechRecognizer.record(source)
     #try:
     text = speechRecognizer.recognize_google(audio)
     print(text) 
     #except:
      # print("Unable to translate") 
