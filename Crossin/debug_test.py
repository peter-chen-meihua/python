#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: debug_test.py

import random
a = 0
for i in range(5):
    b = random.choice(range(5))
    a += i / b
print a