#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: if_nesting.py

x = input()
y = input()
if x >=0:
    if y >= 0:
        print '1'
    else:
        print '4'
else:
    if y >= 0:
        print '2'
    else:
        print '3'