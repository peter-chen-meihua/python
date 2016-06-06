#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: regular_test3.py

import re
text = '11525566474 15852288741 025115 32584477158 21691155268 121651814 26121546 13549966258'
m = re.findall(r"1[0-9]{10}",text)
if m:
    print m
else:
    print 'not match'