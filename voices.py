#-*- coding: utf-8 -*-

from random import choice
import platform

voices = (u'進むと言うのか？修羅の道を...ッ！！！',
          u'おにいちゃん？あんとらっくとふぁいるってなあに？ぷっしゅしちゃうの？',
          u'まーたお前はuntracked fileを残しているぞ？しょうがないやつだなあ',
          u'ちくわ大明神',
          u'untracked fileが残っています。ただちにgit addし直して下さい。それでもgit pushしますか？')

def get_message():
    return choice(voices)

def say_message(msg):
    if platform.system() == 'Darwin':
        from subprocess import Popen, PIPE
        Popen('say ' + msg, shell=True, stdout=PIPE, stderr=PIPE)

