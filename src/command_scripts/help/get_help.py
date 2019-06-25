# script to tell user commands available to them

import speak
import subprocess
import time

#custom modules
import hotword

def main():
    # dictionary with the command mapped to the keywords needed to activate it
    commands_available = {
                          "to turn off the smart plug" : "turn plug off",
                          "to turn on the smart plug": "turn plug off",
                          "to get the news headlines" : "news",
                          "to get the weather forecast" : "weather",
                          "to send an email to alex" : "send email alex",
                          "to read the email inbox" : "read email",
                          "to play a song": "play and the songs name",
                          "to pause the song" : "hotword",
                          "to play the song" : "play song",
                          "to stop the song" : "stop song",
                          "to shuffle your playlist": "shuffle playlist",
                          "to translate a sentence" : "translate followed by the sentence and then to followed by the destination language",
                          "to search wikipedia": "what is and the search term",
                          "to turn on the candle" : "candle on",
                          "to turn off the candle" :"candle off"
                        }

    help_information = ""
    for (command, key_words) in commands_available.items():
        help_information = help_information + ("{} say a sentence consisting of {}".format(command, key_words))

    # hotword detection in background while speaking
    subprocess.Popen(["python3", "/home/pi/2019-ca400-randlea2/src/hotword.py","&"])
    speak.speak_to_user(help_information)



if __name__== "__main__":
    main()