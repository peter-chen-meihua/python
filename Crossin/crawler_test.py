#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: crawler_test.py

import urllib,time

time_start = time.time()
data = []
for i in range(30):
    print 'request movice:',i
    id = 1764796 + i
    url = 'https://api.douban.com/v2/movie/subject/%d' % id
    d = urllib.urlopen(url).read()
    data.append(d)
    print i , time.time() - time_start
print 'data:',len(data)