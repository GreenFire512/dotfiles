#!/bin/sh

~/.xinitrc &
pgrep -x sxhkd > /dev/null || sxhkd -c ~/.config/sxhkd/qtile &
