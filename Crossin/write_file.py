#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: write_file.py

data = 'I will be in a file.\nSo cool!'
out = open('output.txt','w')
out.write(data)
out.close()