#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: function_transfer_test2.py

def calcSum(*args):
    sum = 0
    for i in args:
        sum += i
    print sum

calcSum(1,2,3)
calcSum(123,456)
calcSum()

def printAll(*args):
    for i in args:
        print i,
    print

printAll(1,2,3)
printAll(3,2,1)