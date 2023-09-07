#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias sudo='doas'
alias sudoedit='doas rnano'
PS1='\u\e@\h \W > '
PS2='>>>'

complete -cf sudo
complete -cf doas

#auto CD
shopt -s autocd
