#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: function_transfer_test.py

def func(arg1,arg2):
    print arg1,arg2

func(3,7)
func(arg2=3,arg1=7)

def func(arg1=1,arg2=2,arg3=3):
    print arg1,arg2,arg3
func(2,3,4)
func(5,6)
func(7)