#!/bin/python

import os
import subprocess
import sys

HOME_DIR = '~/'
HOME_DIR_LOCAL = './home'
ETC_DIR = '/etc/'
ETC_DIR_LOCAL = './etc/'

UNLINK = len(sys.argv) > 1 and sys.argv[1]


def link_or_unlink(source, destination, count=0, is_print=True):
    """ link or unlink files """
    destination = os.path.expanduser(destination)
    cmd_line = []

    files = ['']
    if os.path.isdir(source):
        files = os.listdir(source)
        destination_dir = destination
    else:
        destination_dir = os.path.dirname(destination)

    if not os.path.isdir(destination_dir):
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
        elif not UNLINK:
            cmd_line = [f"ln -nf {source_file} {destination_file}"]
        if cmd_line:
            print(subprocess.run(cmd_line, shell=True, capture_output=True, check=False))
        else:
            print('skip link: ', source_file)

    if is_print:
        print('Total: ', count)
    return count

# home dir
link_or_unlink(HOME_DIR_LOCAL, HOME_DIR)

# etc dir
# link_or_unlink(ETC_DIR_LOCAL, ETC_DIR)
