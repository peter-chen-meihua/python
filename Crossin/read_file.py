#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: read_file.py

f = file('data.txt')
data = f.read()
print data
f.close()
print

f = file('data.txt')
data = f.readline()
print data
f.close()
print

f = file('data.txt')
data = f.readlines()
print data
f.close()