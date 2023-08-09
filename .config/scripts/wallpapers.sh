#!/bin/bash

CURRENT_PROCESS=$$

echo $CURRENT_PROCESS
for PROCESS in $(pgrep -f $(basename $0)); do
    if [ $PROCESS -ne $CURRENT_PROCESS ]; then
        kill -9 $PROCESS
    fi
done

while true
do
    feh --bg-fill --randomize ~/Pictures/wallpapers/backgroud/*
    sleep 1800
done