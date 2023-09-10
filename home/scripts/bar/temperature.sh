#!/bin/sh

TEMP1=/sys/devices/platform/coretemp.0/hwmon/hwmon5/temp1_input
TEMP2=/sys/devices/platform/coretemp.0/hwmon/hwmon6/temp1_input
TEMP3=/sys/devices/platform/coretemp.0/hwmon/hwmon7/temp1_input

case $BLOCK_BUTTON in
    1) st -e 'sensors';;
esac

if [ -f "$TEMP1" ]; then
    TEXT=$((`cat $TEMP1`/1000))
elif [ -f "$TEMP2" ]; then
    TEXT=$((`cat $TEMP2`/1000))
elif [ -f "$TEMP3" ]; then
    TEXT=$((`cat $TEMP3`/1000))
else
    TEXT=
fi

printf " %s" $TEXT