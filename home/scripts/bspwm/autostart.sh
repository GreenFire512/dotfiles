#!/bin/sh

config=~/.config/sxhkd/bspwm
pgrep -f "sxhkd -c $config" > /dev/null || sxhkd -c $config &

~/.config/scripts/polybar/launch.sh &

exec dbus-launch bspwm