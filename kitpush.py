#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re
from subprocess import Popen, PIPE
import sys

from col import red, green
from voices import get_message

def concat(list, sep=' '):
    return reduce(lambda x, y: x + sep + y, list)

def main():
    pattern = re.compile('nothing to commit, working directory clean')
    command = concat(['git', 'push'] + sys.argv[1:])

    proc = Popen('git status', stdout=PIPE, shell=True)
    out = proc.stdout.readlines()

    if len(out) == 2 and pattern.match(out[1].rstrip()):
        print green('execute: ' + command)
        proc = Popen(command, shell=True)
        exit()

    print
    print red(get_message())
    print u'git pushしますか？[yn] > ',
    while True:
        desire = raw_input()
        if desire == 'n':
            exit()
        elif desire == 'y':
            print green('execute: ' + command)
            proc = Popen(command, shell=True)
            exit()
        else:
            print "please input 'y' or 'n'!!!"

if __name__ == '__main__':
    main()

