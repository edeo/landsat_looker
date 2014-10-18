# ==================================================================
# Homework 1
# Chad Leonard
# October 10, 2014
# ==================================================================

# ==================================================================
#                           E X E R C I S E S 
# ==================================================================

# EXERCISE #1 
# Create a function that acts as a simple calulator
# If the operation is not specified, default to addition
# If the operation is misspecified, return an prompt message
# Ex: my_calc(4,5,"multiply") returns 20
# Ex: my_calc(3,5) returns 8
# Ex: my_calc(1, 2, "something") returns error message

def my_calc(x,y, op="add"):
    if op == "add":
        ans = x + y
    elif op == "multiply":
        ans = x * y
    else:
        ans = op + " is not a valid method"
    return ans

# EXERCISE #2
# Given a list of numbers, return a list where
# all adjacent duplicate elements have been reduced to a single element.
# Ex: [1, 2, 2, 3, 2] returns [1, 2, 3, 2]. 
# You may create a new list or modify the passed in list.

# Bonus: Remove all duplicate values (adjacent or not)
# Ex: [1, 2, 2, 3, 2] returns [1, 2, 3]

def my_uniq2(lst):
    newlist = []
    for word in lst:
        if word not in newlist:
            newlist.append(word)
    return newlist

def my_uniqlist(lst, all=False):
    newlist = []
    if all:
        newlist = my_uniq2(lst)
    else:
        i=0
        while i < len(lst) - 1:
            if lst[i] != lst[i+1]:
                newlist.append(lst[i])
            i += 1
        newlist.append(lst[-1])
    return newlist

# EXERCISE #3
# Take a string, change it into a list and capitalize all words 
# that are more than 3 characters long using list comprehension
# Ex: "Strange women lying in ponds is no basis for government"
# Returns: ['Strange', 'Women', 'Lying', 'Ponds', 'Basis', 'Government'] 

# Bonus: Same as before, but output should include all words
# Ex: "Strange women lying in ponds is no basis for government"
# Returns: ['Strange', 'Women', 'Lying', 'in', 'Ponds', 'is', 'no', 'Basis', 'for', 'Government']


if __name__ == "__main__":
    # Test Exercise 1:
    print '=' * 10
    x = 4
    y = 3
    print my_calc(x,y)
    for op in ["add","multiply","nada"]:
        print my_calc(x,y,op)
	
    #Test Exercise 2:
    print '=' * 10
    blist = [0,0,5,5,5,1,2,4,4,5,6]
    print blist
    for booly in [True,False]:
        print my_uniqlist(blist, booly)
	
    #Test Exercise 3:
    print '=' * 10
    quote = "Strange women lying in ponds is no basis for government"
    print [word.capitalize() for word in quote.split() if len(word) > 3]
	
    #Test Exercise 3 Bonus:
    print [str.capitalize(word) if len(word) > 3 else word for word in quote.split()]


    print [word.capitalize() if len(word) > 3 else word for word in quote.split()]


