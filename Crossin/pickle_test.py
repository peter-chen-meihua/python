#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: pickle_test.py

import pickle

test_data = ['Save me!',123.456,True]

f = file('test.data','w')
pickle.dump(test_data,f)
f.close()

f = file('test.data')
test_data = pickle.load(f)
f.close()

print test_data