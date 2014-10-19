# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 19:15:04 2014

@author: danielmatthews
"""

from __future__ import division
import csv

# Part 1:
with open('../data/drinks.csv', 'rU') as f:
    header = csv.reader(f).next()
    data = [row for row in csv.reader(f)]

# Part 2:
assert(header[1] == 'beer_servings')
beers = [int(row[1]) for row in data]

# Part 3:
assert(header[5] == 'continent')
NA_beers = [int(row[1]) for row in data if row[5]=='NA']
EU_beers = [int(row[1]) for row in data if row[5]=='EU']

# Part 4:
NA_avg = round(sum(NA_beers) / float(len(NA_beers)), 2)
EU_avg = round(sum(EU_beers) / float(len(EU_beers)), 2)


# Part 1 w/ DictReader:
with open('data/drinks.csv', 'rU') as f:
    data = [row for row in csv.DictReader(f)]
header = data[0].keys()

# Part 2 w/ Dictreader:
beers = [int(row['beer_servings']) for row in data]

# Part 3 w/ Dictreader:
NA_beers = [int(row['beer_servings']) for row in data if row['continent'] == 'NA']
EU_beers = [int(row['beer_servings']) for row in data if row['continent'] == 'EU']

# Part 4 w/ DictReader:
NA_avg = round(sum(NA_beers) / len(NA_beers), 2)
EU_avg = round(sum(EU_beers) / len(EU_beers), 2)
