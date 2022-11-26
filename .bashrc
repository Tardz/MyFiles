# ~/.bashrc
### PATHS ###
export PYTHONPATH=$PYTHONPATH:/home/jonalm/docs/tdde25-2022-projekt-sg3-08/lib/python3.10/site-packages

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
alias .='cd ..'
alias l='lsd -all'
alias ll="lsd"
alias pacman='sudo pacman'
alias update='pacman -Syu'
alias pac='pacman -R $(pacman -Qtdq)'
alias rt='systemctl reboot'
alias sd='systemctl poweroff'
alias hb='systemctl hibernate'
alias rm='sudo rm -r'
alias nnn='nnn -d -e -H -r'
alias gg='git status'
alias xt='Xephyr -br -ac -noreset -screen 1440x900 :1 &'
alias x='XephDISPLAY=:1 qtile'
alias n='nvim'
