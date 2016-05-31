#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: write_file_test.py

# 1.
f = open('data.txt','r')
data = f.read()
print data
w = open('data2.txt','w')
w.write(data)
f.close()
w.close()

# 2.
indata = input()
w = open('input.txt','w')
w.write(indata)
w.close()