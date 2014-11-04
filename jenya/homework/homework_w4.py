# -*- coding: utf-8 -*-

# completed by @jenyazueva

'''
Exercise 2 (homework):
Learn csv.DictReader() and redo all of Exercise 1 using csv.DictReader()

Part 1:
    Read in drinks.csv
    Store the header in a list called 'header'
    Store the data in a list of lists called 'data'
Part 2:
    Isolate the beer_servings column in a list of integers called 'beers'
    Hint: use a list comprehension to do this in one line
Part 3:
    Create separate lists of NA and EU beer servings ('NA_beers', 'EU_beers')
    Hint: use list comprehensions
Part 4:
    Calculate the average NA and EU beer servings ('NA_avg', 'EU_avg') to 2 decimals
'''
import csv

# part 1
with open('data/drinks.csv', 'rU') as drinks_csv_2:
    data = [row for row in csv.DictReader(drinks_csv_2)]
header = data[0].keys()

# part 2
beers = [int(row['beer_servings']) for row in data]

# part 3
NA_beers = [int(row['beer_servings']) for row in data if row['continent'] == 'NA']
EU_beers = [int(row['beer_servings']) for row in data if row['continent'] == 'EU']

# part 4
NA_avg = round(sum(NA_beers) / float(len(NA_beers)), 2)
EU_avg = round(sum(EU_beers) / float(len(EU_beers)), 2)