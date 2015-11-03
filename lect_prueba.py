# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 11:44:50 2015

@author: wbarrios
"""

#Used libs python
import json 
import numpy as np
import collections

#load all arrays names per video in JSON file.
names=np.load('data/array_list_names.npy')

#Determinate freq of names.
names_counter=collections.Counter(names)
#Create a name list (203 classes from activity-net.org)
real_namelist=list(names_counter)
print real_namelist
print len (real_namelist)