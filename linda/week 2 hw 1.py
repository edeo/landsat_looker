"""
Exercise 2 (homework):
Learn csv.DictReader() and redo all of Exercise 1 using csv.DictReader()
"""
import csv

"""
Part 1:
    Read in drinks.csv
    Store the header in a list called 'header'
    Store the data in a list of lists called 'data'
"""  
f = csv.DictReader(open('/Users/lindaxie/desktop/drinks.csv')) #edit path
header = f.fieldnames
data = [] #list of dictionaries
for row in f:
    data.append(row)
    
"""
Part 2:
    Isolate the beer_servings column in a list of integers called 'beers'
    Hint: use a list comprehension to do this in one line
"""
beers = [int(row['beer_servings']) for row in data]

"""        
Part 3:
    Create separate lists of NA and EU beer servings ('NA_beers', 'EU_beers')
    Hint: use list comprehensions
"""   
NA_beers = [int(row['beer_servings']) for row in data if row['continent']=='NA'] 
EU_beers = [int(row['beer_servings']) for row in data if row['continent']=='EU'] 

"""    
Part 4:
    Calculate the average NA and EU beer servings ('NA_avg', 'EU_avg') to 2 decimals
"""
mean_NA_beers = round(sum(NA_beers)/float(len(NA_beers)),2)
mean_EU_beers = round(sum(EU_beers)/float(len(EU_beers)),2)



