# -*- coding: utf-8 -*-
"""
This is a calculator function
"""

def my_calc(x,y, operation='add'):
	if operation == 'add':
		return x+y
	elif operation == 'multiply':
		return x*y
	elif operation=='divide':
		return x/y
	elif operation=='subtract':
		return x-y
	else:
		return 'Error! Not a valid operation!'

