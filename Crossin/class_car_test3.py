#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: class_car_test3.py

class Vehicle:
    def __init__(self,speed):
        self.speed = speed

    def drive(self,distnace):
        print 'need %f hour(s)' % (distnace / self.speed)

class Bike(Vehicle):
    pass

class Car(Vehicle):
    def __init__(self,speed,fuel):
        Vehicle.__init__(self,speed)
        self.fuel = fuel

    def drive(self,distance):
        Vehicle.drive(self,distance)
        print 'need %f fuels' % (distance * self.fuel)

b = Bike(15.0)
c = Car(80.0,0.012)
b.drive(100.0)
c.drive(100.0)