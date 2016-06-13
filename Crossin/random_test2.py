#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: random_test2.py

from random import randint
import random
x = randint(1,10)
print x
y = random.random()
print y
z = random.choice('hello')
print z
a = random.choice(['hello','world'])
print a
b = random.randrange(1, 9, 2)
print b