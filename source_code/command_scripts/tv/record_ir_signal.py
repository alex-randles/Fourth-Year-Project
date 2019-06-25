import RPi.GPIO
import os
import datetime
import time
import json

#custom modules
import speak
import hotword
import translate_speech

code_file = "/home/pi/2019-ca400-randlea2/src/command_scripts/tv/ir_codes.json"

# start connection with GPIO pin
ir_receiver_gpio = 36
RPi.GPIO.setmode(RPi.GPIO.BOARD)
RPi.GPIO.setup(ir_receiver_gpio, RPi.GPIO.IN)

def save_code(name, code):
    with open(code_file ,"r") as json_file:
        data = json.load(json_file)
    with open(code_file, "w") as json_file:
        data[name] = code
        json.dump(data, json_file)
        print("code added to {}".format(code_file))
    return None


def get_code():
    current_pulse = None
    timer = datetime.datetime.now()
    while current_pulse != 0:
        current_pulse = RPi.GPIO.input(ir_receiver_gpio)
        timer_left = (datetime.datetime.now() - timer).total_seconds()
        # timer if they dont press button
        if timer_left > 30:
            return None
    start_time = datetime.datetime.now()
    pulses = []
    # count for number of 1's
    count = 0
    # check if previous pulse its 1 (mark) or 0 (space) 
    previous_pulse = 0
    while count < 10000:
        if current_pulse != previous_pulse:
            now = datetime.datetime.now()
            pulse_time = now - start_time
            start_time = datetime.datetime.now()
            pulses.append(pulse_time.microseconds)
        if current_pulse == 1:
            count = count + 1
        else:
            count = 0
        previous_pulse = current_pulse
        current_pulse = RPi.GPIO.input(ir_receiver_gpio)
    print("code received")
    RPi.GPIO.cleanup()
    return pulses

def record_code():
    speak.speak_to_user("Please press the button ")
    code  = get_code()
    # if no button pressed
    if code is None:
        speak.speak_to_user("Unable to save, please try again ")
    else:
        speak.speak_to_user("What is the name of the button ")
        name = translate_speech.start_translator()
        save_code(name, code)
        speak.speak_to_user("Button saved")


def main():
    record_code()
    hotword.detect_hotword()


if __name__ == "__main__":
    main()