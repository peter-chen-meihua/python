#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: if_elif_else.py

from random import randint

def isEqual(num1,num2):
    if num1 < num2:
        print 'too small!'
        return False
    elif num1 > num2:
        print 'too big!'
        return False
    else:
        print 'bingo'
        return True
        
num = randint(1,100)
print 'Guess what I think?'
bingo = False
while bingo == False:
    answer = input()
    bingo = isEqual(answer,num)