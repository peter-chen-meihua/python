#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test7.py

x = input()
for i in range(1,x+1):
    for j in range(0,x-i):
        print '',
    for j in range(0,i):
        print '*',
    print