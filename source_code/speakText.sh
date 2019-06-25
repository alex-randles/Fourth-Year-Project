#!/bin/bash
# bash script to change leds color and run pico2wave voice synthesizer

pico2wave -w=speakText.wav "$*"
aplay speakText.wav
rm speakText.wav
