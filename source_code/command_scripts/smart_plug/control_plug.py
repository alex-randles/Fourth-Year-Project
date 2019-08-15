import time
import subprocess

#custom modules
import hotword

def main(spoken_words):
    if "on" in spoken_words:
        subprocess.Popen(["node /home/pi/zigbee_on.js &"], shell=True)
    else:
        subprocess.Popen(["node /home/pi/zigbee_off.js &"], shell=True)
    hotword.detect_hotword()


if __name__ == "__main__":
    main()
