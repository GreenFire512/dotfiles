#!/bin/sh

case $BLOCK_BUTTON in
    1) st -e doas yay -Syu;;
esac
check_updates() {
    # if ! updates_arch=$(checkupdates 2> /dev/null | wc -l); then
    #     updates_arch=0
    # fi

    # if ! updates_aur=$(yay -Qum 2> /dev/null | wc -l); then
    #     updates_aur=0
    # fi

    if ! UPDATES=$(yay -Qu 2> /dev/null | wc -l); then
        UPDATES=0
    fi
}

check_updates

if [ "$UPDATES" -gt 0 ]; then
    TEXT=$UPDATES
else
    TEXT=󰡕
fi

printf "󰮯  %s" $TEXT