#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: regular_test2.py

# 1.
import re
text = 'Hi,I am Shirley Hilton. I am his wife.'
m = re.findall(r"i.",text)
if m:
    print m
else:
    print 'not match'

# 2.
text = 'Hi,I am Shirley Hilton. I am his wife.'
m = re.findall(r"I.*e",text)
if m:
    print m
else:
    print 'not match'

# 3.
text = 'Hi,I am Shirley Hilton. I am his wife.'
m = re.findall(r"I.*?e",text)
if m:
    print m
else:
    print 'not match'


# 4.
text = 'site sea sue sweet see case sse ssee loses'
m = re.findall(r"\bs\S*?e\b",text)
if m:
    print m
else:
    print 'not match'