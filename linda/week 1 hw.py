# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 21:09:38 2014

@author: lindaxie
"""

# EXERCISE #1: 
# Create a function that acts as a simple calulator
# So my_calc(1,2,"add") returns 3, and my_calc(4,5,"multiply) returns 20
# If the operation is not specified, default to addition
# If the operation is misspecified, return an error
from __future__ import division 
# to import the float function

def my_calc(x, y, oper = 'add'):
    if oper=='subtract':
        return x-y
    elif oper=='multiply':
        return x*y
    elif oper=='divide':
        # return a/float(b)
        return x/y
    elif oper=='add':
        return x + y
    else:
        return 'error: oper type must be add, subtract, multiply or divide'

# EXERCISE #2
# Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
# BONUS: remove all duplicate values (adjcent or not)

numbers = [1,2,2,3] #[1,2,3]
numbers = [1,2,3,2] #[1,2,3,2]
numbers = [1,2,2,2] #[1,2]
numbers = [1,2,2,3,2]
numbers = [1,2,5,3,3,6,2,3,4,7,7,7,3]

def uniqueExer(numList, exerType = 'default'):
    newList = [numList[0]]
    for i in range(1,len(numList)):
        if exerType == 'bonus':
            iAdd = 1
            for j in range(i):
                if numList[j] == numList[i]:
                    iAdd = 0
            if iAdd == 1: 
                newList.append(numList[i])
        else:
            if numList[i] != numList[i-1]:
                newList.append(numList[i])
    return newList
 
def unique(numList):
    newList = []
    for num in numList:
        if num not in newList:
            newList.append(num)
    return newList
    
def uniqueV2(numList):
    return(list(set(numList)))

# EXERCISE #3
# Take a string, change it into a list and capitalize all words 
# that are more than 3 characters long using list comprehension
# Ex: "Strange women lying in ponds is no basis for government"
# Returns: ['Strange', 'Women', 'Lying', 'Ponds', 'Basis', 'Government'] 

string = 'Strange women lying in ponds is no basis for government'
[word.capitalize() for word in string.split() if len(word)>3]

def cap(string, exerType = 'default'):
    string = string.split()
    if exerType=='bonus':
        string = [x.capitalize() if len(x)>3 else x for x in string]
    else:
        string = [x.capitalize() for x in string if len(x)>3]
    return string

# Bonus: Same as before, but output should include all words
# Ex: "Strange women lying in ponds is no basis for government"
# Returns: ['Strange', 'Women', 'Lying', 'in', 'Ponds', 'is', 
# 'no', 'Basis', 'for', 'Government']