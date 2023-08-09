#!/usr/bin/env bash

HERE=$(dirname $(readlink -f $0))
SCREEN_SIZE=${SCREEN_SIZE:-1600x900}
XDISPLAY=${XDISPLAY:-:1}
LOG_LEVEL=${LOG_LEVEL:-INFO}
APP=${APP:-$(python -c "from libqtile.utils import guess_terminal; print(guess_terminal())")}
if [[ -z $PYTHON ]]; then
    PYTHON=python3
fi

Xephyr +extension RANDR -screen ${SCREEN_SIZE} ${XDISPLAY} -ac &
XEPHYR_PID=$!
(
  sleep 1
  env DISPLAY=${XDISPLAY} i3 &
  QTILE_PID=$!
  env DISPLAY=${XDISPLAY} ${APP} &
  wait $QTILE_PID
  kill $XEPHYR_PID
)