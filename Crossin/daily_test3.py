#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: daily_test3.py

import re

text = "aAsmr3idd4bgs7Dlsf9eAF"
print ''.join(re.findall(r'[\d|.]+',text))