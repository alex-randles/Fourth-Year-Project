# will time and record false detections within 10 minutes
# played this: https://www.youtube.com/watch?v=DQqETh7E0LM
# on volume 50% to simulate people speaking
import sys
import os
import snowboydecoder_arecord
import signal
import os
import sqlite3
import subprocess
import time
import multiprocessing
import datetime
import threading

# count of false detections
false_detections = 0

interrupted = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted


def detected():
    print("hotword detected at {}".format(time.time()))
    global false_detections
    false_detections  += 1
    false_detections_info = "There were {} false detections\n".format(false_detections)
    print(false_detections_info)
    detect_hotword()





def detect_hotword():
    # capture SIGINT signal, e.g., Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    print('Listening... Press Ctrl+C to exit')
    # kill all recording before hotword detection starts
    subprocess.call(["killall arecord"], shell = True)
    global detector
    detector.start(detected_callback=detected,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)


def record_result(info):
    # record the results
    result_file = open("/home/pi/2019-ca400-randlea2/src/testing/unit_testing/test_hotword/test_results.txt", "w" )
    result_file.write(info)

def main(sensitivty_level):
    header = "*******TEST WITH {} SENSITIVITY*******\n".format(sensitivty_level)
    record_result(header)
    print(header)
    start_info = "Test starts at {}\n".format(datetime.datetime.now().time())
    print(start_info)
    record_result(start_info)
    global detector
    detector = snowboydecoder_arecord.HotwordDetector("snowboy.pmdl", sensitivity=sensitivty_level)
    detect_hotword()
    end_info = "Test finishes at {}\n".format(datetime.datetime.now().time())
    print(end_info)
    record_result(end_info)
    false_detections_info = "There were {} false detections\n".format(false_detections)
    print(false_detections_info)
    record_result(false_detections_info)


if __name__ == '__main__':
    main(sys.argv[1])


