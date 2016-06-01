#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: dictionary_test.py

score = {
    'peter': 85,
    'jacky': 95,
    'waiber': 74
}
print score['peter']

for name in score:
    print score[name]
    
score['waiber'] = 88
score['charlie'] = 98
del score['peter']

for name in score:
    print name,score[name]