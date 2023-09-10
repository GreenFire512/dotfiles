# #!/bin/sh

case $BLOCK_BUTTON in
    1)st -e doas wg-quick up w0;;
    2)st -e doas wg-quick down w0;;
esac

dwm_vpn () {
    VPN=$(nmcli -a | grep 'wireguard')
    
    if [ "$VPN" = "" ]; then
        VPN=$(nmcli connection | grep 'wireguard' | sed 's/\s.*$//')
    fi

    if [ "$VPN" != "" ]; then
        printf ""
    else
        printf "󰫝"
    fi
}


dwm_vpn