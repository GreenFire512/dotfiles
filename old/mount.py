#!/bin/python

import subprocess

cmd = 'bindfs --resolve-symlinks ~/dotfiles/dotfiles ~/dotfiles/workdir'
print(subprocess.run([cmd], shell=True, capture_output=True))
