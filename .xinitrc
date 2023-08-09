#!/bin/sh

export XDG_SESSION_TYPE=x11
export GDK_BACKEND=x11

# keybind
sxhkd &

# application
lxqt-session &
dunst & # notification manager
copyq & # clipboard manager
picom &
# conky &
# volumeicon &
# nm-applet &

google-chrome-stable &
code &
#betterlockscreen -l &

#bg
~/.config/scripts/wallpapers.sh &

#~/.config/scripts/bspwm/autostart.sh
exec i3
#exec dwm
#exec gnome-session
#exec startlxqt
#export DESKTOP_SESSION=plasma
#exec starplasma-x11
