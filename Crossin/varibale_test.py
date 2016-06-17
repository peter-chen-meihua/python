#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: varibale_test.py

def func(x):
    print 'X in the beginning of func(x):',x
    x = 2
    print 'X in the end of func(x):',x

x = 50
func(x)
print 'X after calling func(x):',x

def func():
    global x
    print 'X in the beginning of func(x):',x
    x = 2
    print 'X in the end of func(x):',x

x = 50
func()
print 'X after calling func(x):',x