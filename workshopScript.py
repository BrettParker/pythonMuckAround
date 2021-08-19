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


## For loops

"I really like cats"
"I really like dogs"
"I like gold fish"
"I really like Jacob"

subjects = ["cats", "dogs", "gold fish", "Jacob"]

for likeables in subjects:
    print("I really like", likeables) #comments

for number in [2,3,4]:
    print('the value of number * x=', number*2)

print("Brett")

primes = [2,3,5]
squared = []

for p in primes:
    sqr = p ** 2
    squared.append(sqr)


primes = [2,3,5]
for i in range(0,len(primes),1):
    print("the value of i in this loop is:", primes[i])



























