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
alias ..='cd ..'
alias l='lsd -all'
alias ll="lsd"
alias pacman='sudo pacman'
alias update='pacman -Syu'
alias pac='pacman -R $(pacman -Qtdq)'
alias rt='sudo reboot'
alias sd='sudo shutdown now'
alias rm='sudo rm -r'
alias nnn='nnn -d -e -H -r'
alias gg='git status'
alias xt='Xephyr -br -ac -noreset -screen 1440x900 :1 &'
alias x='XephDISPLAY=:1 qtile'
