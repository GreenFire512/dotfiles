#!/bin/sh

case $BLOCK_BUTTON in
    1) st -e btop;;
esac

c=0;t=0

awk '/MHz/ {print $4}' < /proc/cpuinfo | (while read -r i
do
    t=$( echo "$t + $i" | bc )
    c=$((c+1))
done
printf "  %s" $(echo "scale=2; $t / $c / 1000" | bc | awk '{printf "%1.1f", $1}'))