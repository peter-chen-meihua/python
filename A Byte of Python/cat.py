#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: cat.py

import sys

def readfile(filename):
    '''Print a file to the standard output.'''
    f = open(filename,'r')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line,end='')  # notice comma
    f.close()
    
# Script starts from here
if len(sys.argv) < 2:
    print('No action specified.')
    sys.exit()
    
if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    # fetch sys.argv[1] but without the first two characters
    if option == 'version':
        print('Version 1.2')
    elif option == 'help':
        print('''\
This program prints files to the standard output.
Any number of files can be specified.
Options in cnclude:
    --version : Prints the version number
    --help    : Dispaly this help''')
    else:
        print('Unknown option.')
    sys.exit()
else:
    for filename in sys.argv[1:]:
        readfile(filename)