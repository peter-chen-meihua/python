#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: crawler_test2.py

import urllib, time, thread

def get_content(i):
    id = 1764796 + i
    url = 'https://api.douban.com/v2/movie/subject/%d' % id
    d = urllib.urlopen(url).read()
    data.append(d)
    print i, time.time() - time_start
    print 'data:', len(data)

time_start = time.time()

data = []

for i in range(30):
    print 'request movie:', i
    thread.start_new_thread(get_content, (i,))
raw_input('press ENTER to exit...\n')