#!/bin/bash

alacritty -e cd $HOME/jonalm/docs/Labbar 
alacritty -e git add --all
alacritty -e git commit -m "upload"
alacritty -e git push -u -f origin master
