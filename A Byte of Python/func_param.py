#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: func_param.py

def printMax(a,b):
    if a > b:
        print(a,'is maximum')
    else:
        print(b,'is maximum')

printMax(3,4) # directly give literal values

x = 7
y = 2

printMax(x,y) # give variables as arguments