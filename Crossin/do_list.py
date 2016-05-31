#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: do_list.py

l = [365,'everyone',0.618,True]

print l
print l[0]
print l[1]
print l[2]
print l[3]

l[0] = 123
print l

l.append(1024)
print l
print l[4]

del l[0]
print l
print l[0]