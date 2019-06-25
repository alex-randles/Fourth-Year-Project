#!/bin/bash


# if arecord is running stop it
# prevents chunk error from previous arecord input when detecting hotword
if pgrep -x "arecord" > /dev/null
then
    sudo killall arecord
    echo "arecord stopped"
fi
