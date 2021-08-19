#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:06:11 2021

@author: s5001793
"""

pressure = [0.27, 0.456, 0.33333, 0.7, 1.4]

print('pressure:', pressure)

print(len(pressure))

print(pressure[1])

#add single value to the end of my list
pressure.append(0.543333333)

#add another list (list within list)
pressure.append([0.43,2.7,0.665])
print(pressure)

pressure1 = [0.27, 0.456, 0.33333, 0.7, 1.4]
#extend to the list
pressure1.extend([0.43,2.7,0.665])
print(pressure1)

#delete

del pressure1[0]
print(pressure1)

empty = [1, "rrrrrr", 1.2345]

del empty[1]













