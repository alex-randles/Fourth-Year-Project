#!/bin/bash
clear 

## show CPU frequency and temperature
cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq
vcgencmd measure_temp 

## system bench to force CPU to turbo speed 
sysbench --test=cpu --cpu-max-prime=1000 --num-threads=4 >/dev/null 2>&1

## show CPU frequency again 
cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq

## longer system bench to measure stability and temperature
sysbench --test=cpu --cpu-max-prime=50000 --num-threads=4 run 

# show CPU frequency and temperature 
cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq
vcgencmd measure_temp 
