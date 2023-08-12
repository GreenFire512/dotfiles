#!/bin/python

import os
import subprocess
import sys

CONFIG_DIR = '~/.config/'
CONFIG_DIR_LOCAL = './.config/'
HOME_DIR = '~/'
HOME_DIR_LOCAL = './'
ETC_DIR = '/etc/'
ETC_DIR_LOCAL = './etc/'

CONFIG_APPS = [
    'alacritty',
    'bspwm',
    # 'cava',
    'conky',
    'dunst',
    # 'dwm',
    'eww',
    # 'htop',
    'hypr',
    'i3',
    'i3blocks',
    'i3status',
    'kitty',
    # 'ncspot',
    'neofetch',
    'openbox',
    'picom',
    'polybar',
    'qtile',
    'ranger',
    'rofi',
    'scripts',
    'sxhkd',
    # 'mpv',
]

HOME_FILES = [
    '.bash_prompt',
    '.bashrc',
    '.gitconfig',
    '.xinitrc',
    # '.zshrc',
]

FILES = [
    '/etc/X11/xorg.conf.d/00-keyboard.conf',
]

UNLINK = len(sys.argv) > 1 and sys.argv[1]


def link_or_unlink(source, destination, count, is_print=True):
    """ link or unlink files """
    destination = os.path.expanduser(destination)
    cmd_line = []

    files = ['']
    if os.path.isdir(source):
        files = os.listdir(source)

    if not os.path.isdir(destination):
        print('create dir:', destination)
        os.makedirs(destination)

    for file_name in files:
        source_file = source + '/' + file_name
        destination_file = destination + '/' + file_name
        if os.path.isdir(source_file):
            count = link_or_unlink(source_file, destination_file, count, False)
            continue

        count += 1
        if UNLINK and os.path.exists(destination_file):
            cmd_line = ["unlink", destination_file]
        elif not UNLINK and not os.path.exists(destination_file):
            cmd_line = [f"ln -nf {source_file} {destination_file}"]
        if cmd_line:
            print(subprocess.run(cmd_line, shell=True, capture_output=True, check=False))
        else:
            print('skip link: ', source_file)

    if is_print:
        print('Total: ', count)
    return count



# .config dir
for file_str in CONFIG_APPS:
    SOURCE_PATH = CONFIG_DIR_LOCAL + file_str
    DEST_PATH = CONFIG_DIR + file_str
    link_or_unlink(SOURCE_PATH, DEST_PATH, 0)

# home dir
# for file_str in HOME_FILES:
#     SOURCE_PATH = HOME_DIR_LOCAL + file_str
#     DEST_PATH = HOME_DIR + file_str
#     link_or_unlink(SOURCE_PATH, DEST_PATH)

# etc dir
# for file_name in HOME_FILES:
#     source = HOME_DIR + file_name
#     dest = HOME_DIR_WORK + file_name
#     print(link_or_unlink(source, dest, unlink))
