# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 21:19:35 2014

@author: Christine
"""

'''
Exercise 1:

Part 1:
    Read in drinks.csv
    Store the header in a list called 'header'
    Store the data in a list of lists called 'data'
    
'''
import csv

readdrink = csv.DictReader(open('drinks.csv', 'rb'), delimiter=',')

header = readdrink.fieldnames
type(header) #is a list
data = [row for row in readdrink] #is not a list of lists

''''    
Part 2:
    Isolate the beer_servings column in a list of integers called 'beers'
    Hint: use a list comprehension to do this in one line
'''
beers = [row.get('beer_servings') for row in data]#[row for row in data .get('beer_servings')]
    
'''
Part 3:
    Create separate lists of NA and EU beer servings ('NA_beers', 'EU_beers')
    Hint: use list comprehensions
'''
na_beers = [int(row.get('beer_servings')) for row in data if row.get('continent') == "NA"]
eu_beers = [int(row.get('beer_servings')) for row in data if row.get('continent') == "EU"]
    
'''    
Part 4:
    Calculate the average NA and EU beer servings ('NA_avg', 'EU_avg') to 2 decimals
'''
na_beers_avg = int((sum(na_beers)/float(len(na_beers)))*100)/100.0 #could use round
eu_beers_avg = round(sum(eu_beers)/float(len(eu_beers)),2)