#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re
from subprocess import Popen, PIPE
import sys

from col import red, green, yellow
from voices import get_message

def concat(list, sep=' '):
    return reduce(lambda x, y: x + sep + y, list)

def exec_push(command):
    proc = Popen(command, shell=True)
    proc.wait()
    print green('execute: ' + command)

def main():
    pattern = re.compile('nothing to commit, working directory clean')
    command = concat(['git', 'push'] + sys.argv[1:])

    proc = Popen('git status', stdout=PIPE, shell=True)
    out = proc.stdout.readlines()

    if len(out) == 2 and pattern.match(out[1].rstrip()):
        exec_push(command)
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
            exec_push(command)
            exit()
        else:
            print "please input 'y' or 'n'!!!"
            print u'git pushしますか？[yn] > ',

if __name__ == '__main__':
    main()

