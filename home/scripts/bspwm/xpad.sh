#!/bin/bash

xpad_index=7
xpad_name=Xpad

desk=$(wmctrl -lx | grep $1 | awk '{print $2;}')
node_id=$(wmctrl -lx | grep $1 | awk '{print $1;}')

wm=$(wmctrl -d | grep Xpad | awk '{print $1}')

if ! [ $wm -eq xpad_index ]; then
    bspc wm -a PAD 1920x1080+3840+0
fi

if ! [ pgrep -f $1 ]; then
  $1
fi

if [ ! $desk -eq $xpad_index ] ; then
	bspc node $node_id -d $xpad_name
else
	bspc node $node_id -d focused
fi