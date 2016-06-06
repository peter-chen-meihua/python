#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: weather2.py

import urllib2
import json
from city import city

cityname = raw_input('你想查看哪个城市的天气？\n')
citycode = city.get(cityname)
#print citycode
if citycode:
    try:
        url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
        content = urllib2.urlopen(url).read()
        #print content
        data = json.loads(content)
        #print data
        result = data['weatherinfo']
        #print result
        str_temp = ('%s\n%s ~ %s') % (
            result['weather'],
            result['temp1'],
            result['temp2']
        )
        print str_temp
    except:
        print '查询失败！'
else:
    print '没有找到这个城市！'