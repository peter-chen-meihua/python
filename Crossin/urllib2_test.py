#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: urllib2_test.py

import urllib2
web = urllib2.urlopen('http://www.baidu.com')
content = web.read()
print content
data = open('baidu.html','w')
data.write(content)
data.close()