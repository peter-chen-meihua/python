#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: string_format_test.py

from random import randint

print 'Guess what I think?'
answer = randint(1,100)
bingo = False

while bingo == False:
    result = input()
    
    if result < answer:
        print '%d is too small.' % result
        
    if result > answer:
        print '%d is too big.' % result
        
    if result == answer:
        print 'BINGO, %d is the right answer!' % answer
        bingo = True