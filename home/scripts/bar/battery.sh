#!/bin/sh

LOW=15
BATTERY=BAT0

BAT_ICON0="󰂃"
BAT_ICON1="󰁺"
BAT_ICON2="󰁻"
BAT_ICON3="󰁼"
BAT_ICON4="󰁽"
BAT_ICON5="󰁾"
BAT_ICON6="󰁿"
BAT_ICON7="󰂀"
BAT_ICON8="󰂁"
BAT_ICON9="󰂂"
BAT_ICON10="󱟢"

CHARGE_ICON0="󰢜"
CHARGE_ICON1="󰢜"
CHARGE_ICON2="󰂆"
CHARGE_ICON3="󰂇"
CHARGE_ICON4="󰂈"
CHARGE_ICON5="󰢝"
CHARGE_ICON6="󰂉"
CHARGE_ICON7="󰢞"
CHARGE_ICON8="󰂊"
CHARGE_ICON9="󰂋"
CHARGE_ICON10="󰂅"

battery () {
    CHARGE=$(cat /sys/class/power_supply/$BATTERY/capacity)
    STATUS=$(cat /sys/class/power_supply/$BATTERY/status)
    STAGE=$(($CHARGE / 10))
    if [ "$STATUS" = "Charging" ]; then
        eval ICON='CHARGE_ICON'$STAGE
    else
        eval ICON='$BAT_ICON'$STAGE
    fi
    if [ "$CHARGE" = "100" ]; then
        TEXT=full
    else
        TEXT="$CHARGE%"
    fi
    printf "%s %s" $ICON $TEXT
}

battery