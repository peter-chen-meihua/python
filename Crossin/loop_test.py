#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: loop_test.py

# 1.
for i in range(0,5):
    for j in range(0,5):
        print i,j
print

# 2.
for i in range(0,5):
    for j in range(0,5):
        print '*',
    print
print
    
# 3. 
for i in range(0,5):
    for j in range(0,i+1):
        print '*',
    print