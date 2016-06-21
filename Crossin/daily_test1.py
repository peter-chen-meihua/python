#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: daily_test1.py

import random

x = 0
y = 1
while y > x or y < 1:
    x = input('取1到多少：')
    y = input('几个数：')
'''
while y >= 1:
    i = random.randint(1,x+1)
    print i,
    y -= 1
'''
j = random.sample(range(1, x + 1), y)
print j


