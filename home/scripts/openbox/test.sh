#!/usr/bin/env bash

HERE=$(dirname $(readlink -f $0))
SCREEN_SIZE=${SCREEN_SIZE:-1600x900}
XDISPLAY=${XDISPLAY:-:1}
LOG_LEVEL=${LOG_LEVEL:-INFO}

Xephyr +extension RANDR -screen ${SCREEN_SIZE} ${XDISPLAY} -ac &
XEPHYR_PID=$!
(
  sleep 1
  env DISPLAY=${XDISPLAY} openbox-session &
  QTILE_PID=$!
  env DISPLAY=${XDISPLAY} ${APP} &
  wait $QTILE_PID
  kill $XEPHYR_PID
)