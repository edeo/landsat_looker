# -*- coding: utf-8 -*-
"""
lists
@author: 563572
"""

def adj_list(lis):
	output_list = []
	output_list.append(lis[0])
	for x in range(len(lis)-1):
		if lis[x]!=lis[x+1]:
			output_list.append(lis[x+1])
	return output_list
