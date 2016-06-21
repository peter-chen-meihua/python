#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test11.py

for i in range(1,201):
    sq = i ** 2
    str_sq = str(sq)
    qtr_sq = str_sq[::-1]
    if str_sq == qtr_sq:
        print sq