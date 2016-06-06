#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: class_car_test.py

# 1.
speed = 60.0
distance = 100.0
time = distance / speed
print time

# 2.
class Car:
    speed = 0
    def drive(self,distnace):
        time = distance / self.speed
        print time

car = Car()
car.speed = 60.0
car.drive(100.0)