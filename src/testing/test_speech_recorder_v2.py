## System freezes when recording audio directly from microphone using pythons speech recognition 
## Recording a fixed length audio file will not be sufficent enough as recording length should be variable length
## This is a test to use sox to record audio while the user is speaking then convert it using the python speech recognition package
## V1 testing sensitivty for silenece 
import os, speech_recognition as SR

os.system("sox -t alsa default ./record.wav silence 3 0 3% 1 1.0 1%") # first 3 are input when to start recording when sound is 5% and stop recording when sound less then 5% and 1 second gap   
## After adjusting the settings, this is the most optium solution 

# record audio from the microphone
speechRecognizer = SR.Recognizer()
with SR.AudioFile("record.wav") as source:
     audio = speechRecognizer.record(source)
     #try:
     text = speechRecognizer.recognize_google(audio)
     print(text) 
     #except:
      # print("Unable to translate") 
