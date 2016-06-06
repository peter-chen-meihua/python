#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: class_car_test2.py

# 1.
speed1 = 60.0
distance1 = 100.0
distance2 = 200.0
time1 = distance1 / speed1
print time1
time2 = distance2 / speed1
print time2

speed2 = 150.0
time3 = distance1 / speed2
print time3
time4 = distance2 / speed2
print time4

# 2.
class Car:
    speed = 0
    def drive(self,distance):
        time = distance / self.speed
        print time

car1 = Car()
car1.speed = 60.0
car1.drive(100.0)
car1.drive(200.0)

car2 = Car()
car2.speed = 150.0
car2.drive(100.0)
car2.drive(200.0)