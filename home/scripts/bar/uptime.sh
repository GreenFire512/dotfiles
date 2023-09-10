#!/bin/sh

NOW=`date +%s -d $(date '+%H:%M:%S')`
START=`date +%s -d $(uptime -s | awk '{print $2}')`
DIFFSEC=`expr ${NOW} - ${START}`
UPTIME=$(date +%H:%M -ud @${DIFFSEC})

printf "󰜸 %s" $UPTIME