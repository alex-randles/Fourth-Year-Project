import time
import subprocess

#custom modules
import hotword

def main(spoken_words):
    # i have omitted this script as it was written by the matrix creator team
    # i have been granted permission by them to use it
    if "on" in spoken_words:
        subprocess.Popen(["node /home/pi/zigbee_on.js &"], shell=True)
    else:
        subprocess.Popen(["node /home/pi/zigbee_off.js &"], shell=True)
    hotword.detect_hotword()


if __name__ == "__main__":
    main()