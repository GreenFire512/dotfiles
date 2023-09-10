#!/bin/sh

case $BLOCK_BUTTON in
    1) st -e htop;;
esac

ramp-0=" "
ramp-1="▁"
ramp-2="▂"
ramp-3="▃"
ramp-4="▄"
ramp-5="▅"
ramp-6="▆"
ramp-7="▇"

cpu_freq () {
    c=0;t=0
    CPUFREQ=$(awk '/MHz/ {print $4}' < /proc/cpuinfo | (while read -r i
    do
        t=$( echo "$t + $i" | bc )
        c=$((c+1))
    done
    echo "scale=2; $t / $c / 1000" | bc | awk '{printf "%1.1f", $1}'))
}

cpu () {
    CPU=$(top -bn1 | awk '/Cpu/ { print $2}')
}

cpu_freq
cpu

printf "󰓅  %2.1f%%   %s" $CPU $CPUFREQ