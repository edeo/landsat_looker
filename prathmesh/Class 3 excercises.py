# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 13:32:22 2014

@author: Prathmesh
"""

# EXERCISE #1 
# Create a function that acts as a simple calulator
# If the operation is not specified, default to addition
# If the operation is misspecified, return an prompt message
# Ex: my_calc(4,5,"multiply") returns 20
# Ex: my_calc(3,5) returns 8
# Ex: my_calc(1, 2, "something") returns error message

#Solution: 
def my_calc(x,y,z="add"):
    if z=="add":
        return x+y
    elif z=="subtract":
        return x-y
    elif z=="multiply":
        return x*y
    elif z=="divide":
        return x/y
    else:
        print "Invalid Operation"
        
# EXERCISE #2
# Given a list of numbers, return a list where
# all adjacent duplicate elements have been reduced to a single element.
# Ex: [1, 2, 2, 3, 2] returns [1, 2, 3, 2]. 
# You may create a new list or modify the passed in list.

# Bonus: Remove all duplicate values (adjacent or not)
# Ex: [1, 2, 2, 3, 2] returns [1, 2, 3]

#Solution:
lis1 = []
for x in lis:
    if len(lis1):
      if lis1[-1] != x:
        lis1.append(x)
    else: lis1.append(x)

# EXERCISE #3
# Take a string, change it into a list and capitalize all words 
# that are more than 3 characters long using list comprehension
# Ex: "Strange women lying in ponds is no basis for government"
# Returns: ['Strange', 'Women', 'Lying', 'Ponds', 'Basis', 'Government'] 

# Bonus: Same as before, but output should include all words
# Ex: "Strange women lying in ponds is no basis for government"
# Returns: ['Strange', 'Women', 'Lying', 'in', 'Ponds', 'is', 
#                                       'no', 'Basis', 'for', 'Government']

#Solution:
s="Strange women lying in ponds is no basis for government"

lis=s.split()
lis1 = []
for x in lis:
    if len(x)>3:
        lis1.append(x.capitalize())

lis1

#Bonus Solution:

lis=s.split()
lis1 = []
for x in lis:
    if len(x)>3:
        lis1.append(x.capitalize())
    else: lis1.append(x)

lis1

