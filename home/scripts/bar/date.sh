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

# . sb-theme
printf "  $(date '+%I:%M%p')"