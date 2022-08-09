# ~/.bashrc

### DEFAULT ###
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

### synth-shell-prompt.sh ###
if [ -f /home/jonalm/.config/synth-shell/synth-shell-prompt.sh ] && [ -n "$( echo $- | grep i )" ]; then
	source /home/jonalm/.config/synth-shell/synth-shell-prompt.sh
fi

### START NEOFETCH IN TERM ###
neofetch

### ALIAS ###
alias ll='ls -alF'
alias pacman='sudo pacman'
alias reboot='sudo reboot'
alias shutdown='sudo shutdown now'
alias rm='sudo rm -r'
alias nnn='nnn -d -e -H -r'
alias gg="git status"
