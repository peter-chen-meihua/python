#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: continue.py

while True:
    s = input('Enter something: ')
    if s == 'quit':
        break
    if len(s) < 3:
        continue
    print('Input is of sufficient length')
    # Do other kinds of processing here...