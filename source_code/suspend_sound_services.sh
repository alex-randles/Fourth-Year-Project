#!/bin/bash


# stop speaking
if pgrep -x "aplay" > /dev/null
then
    killall aplay
fi

# pause playing music
if pgrep -x "mplayer" > /dev/null
then
   kill -STOP $(pgrep mplayer)
fi