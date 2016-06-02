#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: weather.py

from city import city
import urllib2

cityname = raw_input('Which city do you want to know?\n')
citycode = city.get(cityname)
print citycode
if citycode:
    url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
    content = urllib2.urlopen(url).read()
    print content