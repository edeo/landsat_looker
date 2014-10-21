# ==================================================================
# Homework 2
# Chad Leonard
# October 15, 2014
# ==================================================================

# ==================================================================
#                           E X E R C I S E  2 
# ==================================================================

'''
Exercise 2 (homework):
Learn csv.DictReader() and redo all of Exercise 1 using csv.DictReader()
'''
'''
Part 1:
    Read in drinks.csv
    Store the header in a list called 'header'
    Store the data in a list of lists called 'data'
'''
path = '../../../DAT3_All/DAT3/data'
import csv
with open(path+'/drinks.csv', 'rU') as f:
    data = []
    all = csv.DictReader(f)
    header = all.fieldnames
    for f_csv in all:
        data.append(f_csv.values())
    print header
    print data

'''
Part 2:
    Isolate the beer_servings column in a list of integers called 'beers'
    Hint: use a list comprehension to do this in one line
'''
with open(path+'/drinks.csv', 'rU') as f:
    beers = [int(all['beer_servings']) for all in csv.DictReader(f) ]
print beers
        
'''
Part 3:
    Create separate lists of NA and EU beer servings ('NA_beers', 'EU_beers')
    Hint: use list comprehensions
'''
with open(path+'/drinks.csv', 'rU') as f:
    NA_beers = [int(all['beer_servings']) for all in csv.DictReader(f) if all['continent'] == 'NA' ]
with open(path+'/drinks.csv', 'rU') as f:
    EU_beers = [int(all['beer_servings']) for all in csv.DictReader(f)  if all['continent'] == 'EU' ]
print NA_beers
print EU_beers


'''
Part 4:
    Calculate the average NA and EU beer servings ('NA_avg', 'EU_avg') to 2 decimals
'''
print round(float(sum(NA_beers))/len(NA_beers),2)
print round(float(sum(EU_beers))/len(EU_beers),2)


# ==================================================================
#                           E X E R C I S E  3
# ==================================================================

'''
Exercise 3 (optional homework):
Learn zip() and write some 'nicer code' for Exercise 1 with zip() and csv.reader()
'''

'''
Part 1:
    Read in drinks.csv
    Store the header in a list called 'header'
    Store the data in a list of lists called 'data'
'''
import csv
with open(path+'/drinks.csv', 'rU') as f:
    header = csv.reader(f).next()
    records = [dict(zip(header, line))  for line in csv.reader(f)] 

    
'''
Part 2:
    Isolate the beer_servings column in a list of integers called 'beers'
    Hint: use a list comprehension to do this in one line
'''    
beers = [int(record['beer_servings']) for record in records ]
print beers

'''
Part 3:
    Create separate lists of NA and EU beer servings ('NA_beers', 'EU_beers')
    Hint: use list comprehensions
'''

NA_beers = [int(record['beer_servings']) for record in records if record['continent'] == 'NA' ]
print NA_beers

EU_beers = [int(record['beer_servings']) for record in records if record['continent'] == 'EU' ]
print EU_beers


'''
Part 4:
    Calculate the average NA and EU beer servings ('NA_avg', 'EU_avg') to 2 decimals
'''
print round(float(sum(NA_beers))/len(NA_beers),2)
print round(float(sum(EU_beers))/len(EU_beers),2)







