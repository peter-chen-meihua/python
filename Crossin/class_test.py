#!usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: class_test.py

class MyClass:
        name = 'Sam'

        def sayHi(self):
            print 'Hello %s' % self.name

mc = MyClass()
print mc.name
mc.name = 'Lily'
mc.sayHi()