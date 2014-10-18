# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 17:31:12 2014

@author: danielmatthews
"""
# EXERCISE #1 
# Create a function that acts as a simple calulator
# If the operation is not specified, default to addition
# If the operation is misspecified, return an prompt message
# Ex: my_calc(4,5,"multiply") returns 20
# Ex: my_calc(3,5) returns 8
# Ex: my_calc(1, 2, "something") returns error message


from __future__ import division

def my_calc(a, b, operation='add'):
    if operation == 'add':
        return a+b
    elif operation == 'subtract':
        return a-b
    elif operation == 'multiply':
        return a*b
    elif operation == 'divide':
        return a/b
    else:
        print: 'please assign a valid operation- add, subtract, multiply, divide'

my_calc(4,5, 'multiply')
my_calc(3,5)
my_calc(1,2, 'something')

# EXERCISE #2
# Given a list of numbers, return a list where
# all adjacent duplicate elements have been reduced to a single element.
# Ex: [1, 2, 2, 3, 2] returns [1, 2, 3, 2]. 
# You may create a new list or modify the passed in list.

# Bonus: Remove all duplicate values (adjacent or not)
# Ex: [1, 2, 2, 3, 2] returns [1, 2, 3]

def remove_duplicates(base_list):
    new_list = []
    for num in base_list:
        if len(new_list) == 0 or num != new_list[-1]:
            new_list.append(num)
    return new_list

remove_duplicates([1, 2, 2, 3, 2])

# EXERCISE #3
# Take a string, change it into a list and capitalize all words 
# that are more than 3 characters long using list comprehension
# Ex: "Strange women lying in ponds is no basis for government"
# Returns: ['Strange', 'Women', 'Lying', 'Ponds', 'Basis', 'Government'] 

# Bonus: Same as before, but output should include all words
# Ex: "Strange women lying in ponds is no basis for government"
# Returns: ['Strange', 'Women', 'Lying', 'in', 'Ponds', 'is', 
#                                       'no', 'Basis', 'for', 'Government']

quote = "Strange women lying in ponds is no basis for government"
[word.capitalize() for word in quote.split() if len(word) > 3]
