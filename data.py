# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 22:24:29 2017

@author: steve
"""

def get_data(file_name):
    with open (file_name, 'r') as f:
       data = f.read().splitlines()
    return data