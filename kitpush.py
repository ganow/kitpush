#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re
from subprocess import Popen, PIPE
import sys

from col import red, green, yellow
from voices import get_message

def concat(list, sep=' '):
    return reduce(lambda x, y: x + sep + y, list)

def main():
    pattern = re.compile('nothing to commit, working directory clean')
    command = concat(['git', 'push'] + sys.argv[1:])

    proc = Popen('git status', stdout=PIPE, shell=True)
    out = proc.stdout.readlines()

    if len(out) == 2 and pattern.match(out[1].rstrip()):
        proc = Popen(command, shell=True)
        print green('execute: ' + command)
        exit()

    print
    print red(get_message())
    print
    for line in out:
        print yellow(line),
    print
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
            print u'git pushしますか？[yn] > ',

if __name__ == '__main__':
    main()

