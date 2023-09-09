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

brave &
code &
#betterlockscreen -l &

#bg
~/scripts/wallpapers.sh &

#~/.config/scripts/bspwm/autostart.sh
# exec i3
exec dwm 2> ~/.dwm.log
#exec gnome-session
#exec startlxqt
#export DESKTOP_SESSION=plasma
#exec starplasma-x11
