#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: game_save.py

from random import randint

f = open('C:\Users\user\python\Crossin\game.txt')
score = f.read().split()
f.close()
game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])

if game_times > 0:
    avg_times = float(total_times) / game_times
else:
    avg_times = 0
    
print 'You play %d times,least spend %d round to guess the result,average is %.2f round' % (game_times,min_times,avg_times)

num = randint(1,100)
print 'Guess what I think?'
bingo = False
while bingo == False:
    answer = input()
    if answer < num:
        print 'too small!'
    if answer > num:
        print 'too big!'
    if answer == num:
        print 'BINGO!'
        bingo = True