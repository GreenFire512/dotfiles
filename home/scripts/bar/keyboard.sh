#!/bin/sh

LANG_CODE=$(xset -q|grep LED| awk '{ print $10 }')

# case $BLOCK_BUTTON in
#     1) alacritty -s htop;;
# esac

if [ "$LANG_CODE" == "00001000" ]; then
    LANG=ru
else
    LANG=en
fi

printf "󰥻  %s" $LANG