#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename; pickle_test2.py

import pickle
a = 123
b = "hello"
c = 0.618
d = "world"
f = file('test.data','w')
pickle.dump(a,f)
pickle.dump(b,f)
pickle.dump(c,f)
pickle.dump(d,f)
f.close()

f = file('test.data')
x = pickle.load(f)
y = pickle.load(f)
z = pickle.load(f)
o = pickle.load(f)
f.close()

print x,y,z,o