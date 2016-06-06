#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: regular_test1.py

# 1.
import re
text = 'Hi,I am Shirley Hilton. I am his wife.'
m = re.findall(r"hi",text)
if m:
    print m
else:
    print 'not match'

# 2.
text = 'Hi,I am Shirley Hilton. I am his wife.'
m = re.findall(r'\bHi\b',text)
if m:
    print m
else:
    print 'not match'

# 3.
text = 'Hi,I am Shirley Hilton. I am his wife.'
m = re.findall(r'[Hh]i',text)
if m:
    print m
else:
    print 'not match'