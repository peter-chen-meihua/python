#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: string_index_split.py

# 1.
word = 'helloworld'
for c in word:
    print c

# 2.    
print word[0]
print word[-2]

# 3.
print word[5:7]
print word[:-5]
print word[:]

# 4.
newword = ','.join(word)
print newword