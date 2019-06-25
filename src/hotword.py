import sys
import snowboydecoder_arecord
import signal
import os
import sqlite3
import subprocess
import time

# custom modules
import command_recogniser
import listening_leds
import speak
import translate_speech

interrupted = False
security_db = "/home/pi/2019-ca400-randlea2/src/security.db"

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted


# return the current hotword settings e.g snowboy.pmdl or snowboy.udml
def create_security_table():
    # create the security table if not already
    with sqlite3.connect(security_db) as connection:
        cursor = connection.cursor()
        cursor.execute(""" CREATE TABLE if NOT EXISTS security(
		security_lock text primary key,
		hotword_file  text
          )""")
        # set initial security level
        cursor.execute("INSERT or IGNORE INTO security(security_lock,hotword_file)values(?,?) ",("true", "snowboy.pmdl",))
        cursor.execute("SELECT * FROM security")
        results = cursor.fetchone()
        print(results)
    return results[1]



# return the hotword for current security setting
def get_hotword_set():
    # connection to database which stores all security information
    with sqlite3.connect(security_db) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM security")
        # return the universal or personal model depending on settings
        hotword_file = cursor.fetchall()[0][1]
        print(hotword_file)
        return "/home/pi/2019-ca400-randlea2/src/" + hotword_file


# get current hotword set from security table
detector = snowboydecoder_arecord.HotwordDetector(get_hotword_set(), sensitivity=0.45)


def detected():
    #  hotword has been detected, start recording command keywords
    detector.terminate()
    subprocess.call(["/home/pi/2019-ca400-randlea2/src/suspend_sound_services.sh"])
    snowboydecoder_arecord.play_audio_file()
    command_recogniser.query_user()
    print("hotword detected")


def detect_hotword():
    global detector
    signal.signal(signal.SIGINT, signal_handler)
    # kill all recording before hotword detection starts
    print('Listening... Press Ctrl+C to exit')
    listening_leds.listening_leds()
    # need to stop arecord to prevent chunk overflow when recording
    subprocess.call(["/home/pi/2019-ca400-randlea2/src/stop_arecord.sh"])
    detector.start(detected_callback=detected,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)


def main():
    create_security_table()
    detect_hotword()


if __name__ == "__main__":
    main()
