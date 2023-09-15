#!/bin/sh

case $BLOCK_BUTTON in
    1) st -e htop;;
esac

ramp0=" "
ramp1="▁"
ramp2="▂"
ramp3="▃"
ramp4="▄"
ramp5="▅"
ramp6="▆"
ramp7="▇"

cpu_freq () {
    c=0;t=0
    CPUFREQ=$(awk '/MHz/ {print $4}' < /proc/cpuinfo | (while read -r i
    do
        t=$( echo "$t + $i" | bc )
        c=$((c+1))
    done
    echo "scale=2; $t / $c / 1000" | bc | awk '{printf "%1.1f", $1}'))
}

cpu () {
    # CPU=$(top -bn1 | awk '/Cpu/ { print $2}')
    CPU=$(uptime | awk '{print substr($8, 1, length($8)-1)}')
}

cpu_freq
cpu

printf "󰓅  %2.1f    %s" $CPU $CPUFREQ

# # Module showing CPU load as a changing bars.
# # Just like in polybar.
# # Each bar represents amount of load on one core since
# # last run.

# # Cache in tmpfs to improve speed and reduce SSD load
# cache=/tmp/cpubarscache

# case $BLOCK_BUTTON in
# 	2) setsid -f "$TERMINAL" -e htop ;;
# 	3) notify-send "🪨 CPU load module" "Each bar represents
# one CPU core";;
# 	6) "$TERMINAL" -e "$EDITOR" "$0" ;;
# esac

# # id total idle
# stats=$(awk '/cpu[0-9]+/ {printf "%d %d %d\n", substr($1,4), ($2 + $3 + $4 + $5), $5 }' /proc/stat)
# [ ! -f $cache ] && echo "$stats" > "$cache"
# old=$(cat "$cache")
# printf "🪨"
# echo "$stats" | while read -r row; do
# 	id=${row%% *}
# 	rest=${row#* }
# 	total=${rest%% *}
# 	idle=${rest##* }

# 	case "$(echo "$old" | awk '{if ($1 == id)
# 		printf "%d\n", (1 - (idle - $3)  / (total - $2))*100 /12.5}' \
# 		id="$id" total="$total" idle="$idle")" in

# 		"0") printf "▁";;
# 		"1") printf "▂";;
# 		"2") printf "▃";;
# 		"3") printf "▄";;
# 		"4") printf "▅";;
# 		"5") printf "▆";;
# 		"6") printf "▇";;
# 		"7") printf "█";;
# 		"8") printf "█";;
# 	esac
# done; printf "\\n"
# echo "$stats" > "$cache"