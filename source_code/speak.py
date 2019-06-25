# module for speaking to user with speakText.sh
import subprocess
import sys
import speaking_leds


def speak_to_user(sentence, background=None):
    speaking_leds.speaking_leds()
    if background is True:
        subprocess.Popen(["/home/pi/2019-ca400-randlea2/src/speakText.sh", sentence])
    else:
        subprocess.call(["/home/pi/2019-ca400-randlea2/src/speakText.sh", sentence])


if __name__ == "__main__":
    sentece = " ".join(sys.argv[1:])
    speak_to_user(sentece)