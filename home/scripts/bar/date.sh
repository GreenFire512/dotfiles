#!/bin/sh

YAD_WIDTH=200
YAD_HEIGHT=200

case $BLOCK_BUTTON in
    1)
        eval "$(xdotool getmouselocation --shell)"

        if [ $BOTTOM = true ]; then
            : $(( pos_y = Y - YAD_HEIGHT - 20 ))
            : $(( pos_x = X - (YAD_WIDTH / 2) ))
        else
            : $(( pos_y = Y + 20 ))
            : $(( pos_x = X - (YAD_WIDTH / 2) ))
        fi
        yad --calendar --undecorated --fixed --close-on-unfocus --no-buttons \
            --width=$YAD_WIDTH --height=$YAD_HEIGHT --posx=$pos_x --posy=$pos_y
esac

clock=$(date '+%I')

case "$clock" in
	"00") icon="🕛" ;;
	"01") icon="🕐" ;;
	"02") icon="🕑" ;;
	"03") icon="🕒" ;;
	"04") icon="🕓" ;;
	"05") icon="󱑏" ;;
	"06") icon="🕕" ;;
	"07") icon="🕖" ;;
	"08") icon="🕗" ;;
	"09") icon="🕘" ;;
	"10") icon="🕙" ;;
	"11") icon="🕚" ;;
	"12") icon="🕛" ;;
esac

printf "\x01%s  $(date '+%I:%M%p')" $icon