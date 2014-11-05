# EXERCISE #1 
# Create a function that acts as a simple calulator
# If the operation is not specified, default to addition
# If the operation is misspecified, return an prompt message
# Ex: my_calc(4,5,"multiply") returns 20
# Ex: my_calc(3,5) returns 8
# Ex: my_calc(1, 2, "something") returns error message

def my_calc(x, y, operation = 'add'):
	if operation == 'add':
		return x + y
	elif operation == 'multiply':
		return x * y
	elif operation == 'substract':
		return x - y
	elif 'divide':
		return x/y
	else:
		return "Error, invalid option. Please enter 'add', 'substract', 'multiple' or 'divide'"

# EXERCISE #2
# Given a list of numbers, return a list where
# all adjacent duplicate elements have been reduced to a single element.
# Ex: [1, 2, 2, 3, 2] returns [1, 2, 3, 2]. 
# You may create a new list or modify the passed in list.

# Bonus: Remove all duplicate values (adjacent or not)
# Ex: [1, 2, 2, 3, 2] returns [1, 2, 3]

def remove_adj_num(ls):
    i = 1
    while i < len(ls):
        if ls[i] == ls[i-1]:
            ls.pop(i)
        i += 1
    return ls

def flatten(ls):
	return list(set(ls))


# EXERCISE #3
# Take a string, change it into a list and capitalize all words 
# that are more than 3 characters long using list comprehension
# Ex: "Strange women lying in ponds is no basis for government"
# Returns: ['Strange', 'Women', 'Lying', 'Ponds', 'Basis', 'Government'] 

# Bonus: Same as before, but output should include all words
# Ex: "Strange women lying in ponds is no basis for government"
# Returns: ['Strange', 'Women', 'Lying', 'in', 'Ponds', 'is', 'no', 'Basis', 'for', 'Government']



