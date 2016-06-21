#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test8.py

for i in range(1,10):
    for j in range(1,i + 1):
        print '%d * %d = %d' % (j,i,i * j)