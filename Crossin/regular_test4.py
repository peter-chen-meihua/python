#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: regular_test4.py

import re
text = "(021)88776543,010-55667890,02584453362,561512302," \
       "202148541,01025818185,021-84984,0533 51515222,(02151825965"
m = re.findall(r"[(]?0\d{2,3}[)]?[-]?[ ]?\d{8}",text)
if m:
    print m
else:
    print 'not match'

m = re.findall(r"\(?0\d{2,3}[) -]?\d{7,8}",text)
if m:
    print m
else:
    print 'not match'