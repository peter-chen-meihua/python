#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test12.py

import re

f1 = open('from.txt')
data = f1.read()
f1.close()
result = re.findall('[A-z]+',data)
result.sort()
data = '\n'.join(result)
f2 = open('to.txt','w')
f2.write(data)
f2.close()