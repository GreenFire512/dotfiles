#!/bin/sh


VPN=$(eval "~/scripts/bar/vpn-wireguard.sh")
MAIL=$(eval "~/scripts/bar/mail.sh")

echo -e "\x06$VPN\x07$MAIL"