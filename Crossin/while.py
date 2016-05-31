#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: while.py

num = 10
print 'Guess what I think?'
bingo = False

while bingo == False:
    answer = input()
    
    if answer < num:
        print 'too smaill!'
    
    if answer > num:
        print 'too big!'
        
    if answer == num:
        print 'BINGO'
        bingo = True
        
print 'The End'