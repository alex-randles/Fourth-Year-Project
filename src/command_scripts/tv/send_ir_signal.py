import time
import os
import pigpio
import sys
import json
import difflib

#custom modules
import hotword

# json file containing all ir codes
code_file = "/home/pi/2019-ca400-randlea2/src/command_scripts/tv/ir_codes.json"

# the gpio pin for matrix creator ir transmitter
ir_emitter_gpio = 13
pigpio.exceptions = True


def generate_wave(code):
    pigpio_connection.set_mode(ir_emitter_gpio, pigpio.OUTPUT)
    pigpio_connection.wave_add_new()
    start_time = time.time()
    wave = [0 for i in range(0,len(code))]
    for i in range(0, len(code)):
        current_code = code[i]
        # check if a space, led off
        if i % 2 != 0:
            # delay for current code time
            pigpio_connection.wave_add_generic([pigpio.pulse(0, 0, current_code)])
            wave[i] = pigpio_connection.wave_create()
        # else marks, led on
        else:
            mark_signal = generate_mark(current_code)
            pigpio_connection.wave_add_generic(mark_signal)
            wave[i] = pigpio_connection.wave_create()
    # allow waveforms to be generated correctly
    time_difference = start_time - time.time()
    if time_difference > 0.0:
        time.sleep(time_difference)
    return wave

def generate_mark(code_length):
   # generate the mark waveform
   frequency = 26.4
   wave_length = round(code_length/frequency)
   led_on_time = round(frequency / 2.0)
   generated = 0
   mark_wave = []
   for i in range(wave_length):
      # find out how long we should turn turn led on and off
      expected_time = round((i+1)*frequency)
      generated += led_on_time
      led_off_time = expected_time - generated
      generated +=led_off_time
      #                                  ( on       ,  off    ,   delay)
      mark_wave.append(pigpio.pulse(1<<ir_emitter_gpio, 0, led_on_time))
      mark_wave.append(pigpio.pulse(0, 1<<ir_emitter_gpio, led_off_time))
   return mark_wave


def stop_pigpio_signal(code_length):
    # wait till finished sending signal
    while pigpio_connection.wave_tx_busy() is True:
       time.sleep(0.001)
    # delete all waveforms
    for num in range(0 ,code_length):
        pigpio_connection.wave_delete(num)
    # stop connection
    pigpio_connection.wave_clear()
    pigpio_connection.stop()
    return None


def send_wave(wave):
    pigpio_connection.wave_chain(wave)
    return None


def get_code(code_name):
    # find the code user wants to send
    with open(code_file, "r") as json_file:
        codes = json.load(json_file)
        code_keys = codes.keys()
        for word in code_name:
            print(word)
            print(code_keys)
            if word in code_keys:
                return codes[word]
        else:
            code_name = " ".join(code_name)
            key = difflib.get_close_matches(code_name, code_keys, cutoff=0.1)[0]
            print(code_name,key)
            return codes[key]


def main(code_name):
    # need to use global pigpio as we may create multiple instances in one session
    # pigpio prevents this
    global pigpio_connection
    code = get_code(code_name)
    pigpio_connection = pigpio.pi()
    wave = generate_wave(code)
    send_wave(wave)
    stop_pigpio_signal(len(code))
    hotword.detect_hotword()

if __name__ == "__main__":
    main(sys.argv[1:])
