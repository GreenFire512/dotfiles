#!/bin/sh

export XDG_SESSION_TYPE=x11

# keybind
sxhkd &

# application
lxsession &
dunst & # notification manager
parcellite & # clipboard manager
picom &
conky &
# volumeicon &
nm-applet &

google-chrome-stable &
code &
#betterlockscreen -l &

#bg
feh --bg-fill --randomize ~/Pictures/wallpapers/backgroud/*

#~/.config/scripts/bspwm/autostart.sh
exec i3
