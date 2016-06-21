#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: daily_test4.py

import os
import fnmatch

for root,dirs,files in os.walk('.'):
    for file in files:
        if fnmatch.fnmatch(file,"*.txt"):
            print file