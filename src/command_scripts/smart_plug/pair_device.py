# script for pair zigbee smart device
import subprocess
import json
import time

# custom modules
import speak
import hotword

device_json_file = "/home/pi/devices.json"


def get_num_devices(file_name):
    # check how many currently paired devices
    read_file = open(file_name,"r")
    load_json = json.load(read_file)
    num_devices = len(load_json)
    print(num_devices)
    return num_devices


def start_pair():
    speak.speak_to_user("Waiting 60 seconds for you to reset your zig bee device")
    # start pairing script
    subprocess.Popen(["node", "/home/pi/register_zigbee.js", "&"])


def finish_pair(num_devices):
    # wait 65 seconds for them to reset zigbee device
    time.sleep(65)
    new_num_devices = get_num_devices(device_json_file)
    # check if theirs a new device in file
    if new_num_devices > num_devices:
        speak.speak_to_user("Device paired successfully")
    else:
        speak.speak_to_user("Unable to pair device please try again")


def main():
    num_devices = get_num_devices(device_json_file)
    start_pair()
    finish_pair(num_devices)
    hotword.detect_hotword()



if __name__ == "__main__":
    main()