#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test6.py
'''
x = input()
num = {}
for i in range(1,x+1):
    if i == 1 or i == 2:
        num[i] = 1
        print num[i]
        continue
    num[i] = num[i-2] + num[i-1]
    print num[i]
    print num
'''

x = input()
a1 = 1
a2 = 1
i = 3
print a1
print a2
while i <= x:
    a3 = a1 + a2
    print a3
    a1 = a2
    a2 = a3
    i += 1