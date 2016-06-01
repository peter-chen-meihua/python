#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: unusual_test.py

try:
    f = file('non-exist.txt')
    print 'File not exists.'
    f.close()
except:
    print 'File not exists.'
print 'Done'