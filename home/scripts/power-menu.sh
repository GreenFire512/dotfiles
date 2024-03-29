#!/bin/bash

# small power menu using rofi, i3, systemd and pm-utils
# (last 3 dependencies are adjustable below)
# tostiheld, 2016

poweroff_command="systemctl poweroff"
reboot_command="systemctl reboot"
logout_command="pkill dwm"
hibernate_command="systemctl hibernate"
suspend_command="systemctl suspend"

# you can customise the rofi command all you want ...
rofi_command="rofi -width 10 -hide-scrollbar"

options=$'poweroff\nreboot\nlogout\nhibernate\nsuspend' 

# ... because the essential options (-dmenu and -p) are added here
eval '$'$(echo "$options" | $rofi_command -dmenu -p "")_command