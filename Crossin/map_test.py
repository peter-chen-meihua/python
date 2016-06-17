#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: map_test.py

list_1 = [1,2,3,4,5]
list_2 = []
for item in list_1:
    list_2.append(item * 2)
print list_2

list_1 = [1,2,3,4,5]
list_2 = [i * 2 for i in list_1]
print list_2

list_1 = [1,2,3,4,5]
def double_func(x):
    return x * 2
list_2 = map(double_func,list_1)
print list_2

list_1 = (1,2,3,4,5)
list_2 = map(lambda x: x * 2,list_1)
print list_2

list_1 = [1,2,3,4,5,6]
list_2 = [1,3,5,7,9,11]
list_3 = map(lambda x,y: x + y,list_1,list_2)
print list_3

list_1 = [1,2,3,4,5]
list_2 = [1,3,5,7,9]
list_3 = map(None,list_1)
print list_3
list_4 = map(None,list_1,list_2)
print list_4