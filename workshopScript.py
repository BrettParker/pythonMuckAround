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


# if statements
mass = 15.02

if mass > 3.0 and mass <= 10.0:
    print(mass, 'is large')
elif mass > 10.0:
    print(mass, 'reduclously is large')
else:
    print(mass, 'is not large')


masses = [2.4, 7.4, 1.1, 52.3]

for i in masses:
    if i > 3.0 or i <= 10.0:
        print(i, 'is large')
    elif i > 10.0:
        print(i, 'reduclously is large')
    else:
        print(i, 'is not large')


masses = [2.4, 7.4, 1.1, 52.3]
velocity = [53.6, 100.44, 7.2, 10000.5]


if masses[1] > 3.0 and masses[2] <= 10.0 or velocity[0] = 54:
    print('all good')

velocity[0] = 54




import glob
import pandas as pd

for filename in glob.glob('/Users/s5001793/Downloads/data 2/*.csv'):
    contents = pd.read_csv(filename)
    #print(filename, len(contents))

contents.shape[0]

len(contents)

def print_greeting():
    print("hello!!!")


print_greeting()

def print_date(year, month, day):
    joined = str(year) + '-' + str(month) + '-' + str(day)
    print(joined)
    return(joined)

Date = print_date(1999, 12, 29)


def average(values):
    if len(values) == 0:
        print("You must provide some values")
        return None
    return sum(values) / len(values)

def report(pressure):
    #print('pressure is', pressure)
    return(pressure)

print('calling', report(22.5))

report(22.5)

r = report(22.5)












