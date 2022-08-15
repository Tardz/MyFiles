#!/bin/bash

### DISPLAY CONF ###
xrandr --output DVI-D-1  --mode 1920x1080 --rate 144 --pos 0x495 --output HDMI-1 --rotate right --mode 1920x1080 --rate 144

### KEYBOARD CONF ###
setxkbmap se

### TIME ###
#alacritty -e ntpd -qg

### APPS ###
nitrogen --restore &
picom &
emacs --daemon &
openrazer-daemon
imwheel -b 45 &
nm-applet &
polychromatic-tray-applet &
blueman-applet &
#discord --start-minimized
#alacritty -e alttab
