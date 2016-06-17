#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: reduce_test.py

sum = 0
for i in xrange(1,101):
    sum += i
print sum

lst = xrange(1,101)
def add(x,y):
    return x + y
print reduce(add,lst)