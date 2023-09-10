#!/bin/sh

MEM=$(free -m | awk '/Mem/{print $3}')

case $BLOCK_BUTTON in
    1) alacritty -s htop;;
esac

printf "󰌢  %2.1fG" $(($MEM/1000))