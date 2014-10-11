# EXERCISE #1 
# Create a function that acts as a simple calulator
# If the operation is not specified, default to addition
# If the operation is misspecified, return an prompt message
# Ex: my_calc(4,5,"multiply") returns 20
# Ex: my_calc(3,5) returns 8
# Ex: my_calc(1, 2, "something") returns error message

def my_calc(x, y, z):
    if z == "add":
        return x + y
    elif z == "multiply":
        return x*y
    else:
        return "oops! try again, but specify whether to add or multiply."

print my_calc(5,4,'add')

# EXERCISE #2
# Given a list of numbers, return a list where
# all adjacent duplicate elements have been reduced to a single element.
# Ex: [1, 2, 2, 3, 2] returns [1, 2, 3, 2]. 
# You may create a new list or modify the passed in list.

def adj_dup(x):
    new = []
    i = len(x)-1
    while i > 0:
        if x[i] == x[i-1]:
            del x[i]
        i -= 1
    return x

print adj_dup([1,2,2,3])

# Bonus: Remove all duplicate values (adjacent or not)
# Ex: [1, 2, 2, 3, 2] returns [1, 2, 3]

def all_dup(x):
	new = []
	for i in x:
		if i not in new:
			new.append(i)
	return new

print all_dup([1, 2, 2, 3, 2])

# EXERCISE #3
# Take a string, change it into a list and capitalize all words 
# that are more than 3 characters long using list comprehension
# Ex: "Strange women lying in ponds is no basis for government"
# Returns: ['Strange', 'Women', 'Lying', 'Ponds', 'Basis', 'Government'] 

def cap(x):
    new = x.split()
    capitalized = []
    for word in new:
        if len(word) > 3:
            capitalized.append(word[0].upper() + word[1:])  
    return capitalized
    
print cap("Strange women lying in ponds is no basis for government")

# Bonus: Same as before, but output should include all words
# Ex: "Strange women lying in ponds is no basis for government"
# Returns: ['Strange', 'Women', 'Lying', 'in', 'Ponds', 'is', 
# 'no', 'Basis', 'for', 'Government']

def cap_bonus(x):
	new = x.split()
	capitalized = []
	for word in new:
		if len(word) > 3:
			capitalized.append(word[0].upper() + word[1:]) 
		else:
			capitalized.append(word)
	return capitalized

print cap_bonus("Strange women lying in ponds is no basis for government")
