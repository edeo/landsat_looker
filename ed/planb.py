# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 14:32:29 2014

@author: ed
"""


import csv
import re

with open('nywagefull.csv', 'rU') as f:
    header = csv.reader(f).next()
    data = [row for row in csv.reader(f)]

add = [el[3].upper() for el in data]

add2 = [re.findall(r'[0-9A-Z]+', address) for address in add]

exclude = set(['ROOM', 'AVENUE', 'FLOOR', 'RD','ROAD','ST','STREET','BLVD','GROUND','SUITE','#','NY','AVE','DRIVE','DR','1ST','FIRST','2ND','SECOND','3RD','THIRD','4TH','FOURTH','5TH','FIFTH','6TH','SIXTH','7TH','SEVENTH','8TH','EIGHTH','9TH','NINETH','BLVD','BOULEVARD','PLACE','PWKY','PARKWAY','N','NORTH','E','EAST','S','SOUTH','W','WEST','APT','APARTMENT'])

add3 = []
for add_list in add2:
    temp_list = []    
    for el in add_list:
        if el not in exclude:
            temp_list.append(el)
    add3.append(temp_list)

nycwage = [' '.join(el) for el in add3]


##########
import csv
import re

with open('nyc.csv', 'rU') as f:
    header = csv.reader(f).next()
    data = [row for row in csv.reader(f)]

add = [el[-1].upper() for el in data]

add2 = [re.findall(r'[0-9A-Z]+', address) for address in add]

exclude = set(['ROOM', 'AVENUE', 'FLOOR', 'RD','ROAD','ST','STREET','BLVD','GROUND','SUITE','#','NY','AVE','DRIVE','DR','1ST','FIRST','2ND','SECOND','3RD','THIRD','4TH','FOURTH','5TH','FIFTH','6TH','SIXTH','7TH','SEVENTH','8TH','EIGHTH','9TH','NINETH','BLVD','BOULEVARD','PLACE','PWKY','PARKWAY','N','NORTH','E','EAST','S','SOUTH','W','WEST'])

add3 = []
for add_list in add2:
    temp_list = []    
    for el in add_list:
        if el not in exclude:
            temp_list.append(el)
    add3.append(temp_list)

nychadd = [' '.join(el) for el in add3]
#outputs are nycwage and nychadd
#return here continue
#then add those string columns back to the frames
#nycwhd['clean'] = nycwage+' '+nycwhd.zip_cd
#nychealth['clean'] = nychadd
import pandas as pd
import numpy as np 

nywages = pd.read_csv('nywagefull.csv')
nychealth = pd.read_csv('nyc.csv')
#dump score = nychealth[nychealth.columns[-5]]
#there are lots of NAN - I think it depends on the type of inspections 
#all zip codes in nyc
nywages['clean'] = nycwage
nychealth['clean'] = nychadd
nywages.columns

nyczip= (10001, 10002, 10003, 10004, 10005, 10006, 10007, 10009, 10010, 10011, 10012, 10013, 10014, 10016, 10017, 10018, 10019, 10020, 10021, 10022, 10023, 10024, 10025, 10026, 10027, 10028, 10029, 10030, 10031, 10032, 10033, 10034, 10035, 10036, 10037, 10038, 10039, 10040, 10044, 10048, 10065, 10069, 10075, 10111, 10115, 10128, 10280, 10281, 10282, 11201, 11203, 11204, 11205, 11206, 11207, 11208, 11209, 11210, 11211, 11212, 11213, 11214, 11215, 11216, 11217, 11218, 11219, 11220, 11221, 11222, 11223, 11224, 11225, 11226, 11228, 11229, 11230, 11231, 11232, 11233, 11234, 11235, 11236, 11237, 11238, 11239, 11251, 11001, 11004, 11005, 11040, 11096, 11101, 11102, 11103, 11104, 11105, 11106, 11109, 11354, 11355, 11356, 11357, 11358, 11359, 11360, 11361, 11362, 11363, 11364, 11365, 11366, 11367, 11368, 11369, 11371, 11372, 11373, 11374, 11375, 11377, 11378, 11379, 11385, 11411, 11412, 11413, 11414, 11415, 11416, 11417, 11418, 11419, 11420, 11421, 11422, 11423, 11426, 11427, 11428, 11429, 11430, 11432, 11433, 11434, 11435, 11436, 11451, 11691, 11692, 11694, 11697, 10451, 10452, 10453, 10454, 10455, 10456, 10457, 10458, 10459, 10460, 10461, 10462, 10465, 10466, 10467, 10468, 10469, 10470, 10471, 10472, 10473, 10474, 10475, 10301, 10302, 10303, 10304, 10305, 10306, 10307, 10308, 10309, 10310, 10312, 10314)

nycwhd=nywages[nywages['Zip Code'].isin(nyczip)]


nycwhd.columns
'''
now, filter nycwhd for only nyc zipcodes
'''


'''
now, create a data frame just with CAMIS, score, clean, and street address
'''

'''
now, crate a data frame just with case number, number of violations, clean, and street address

'''

'''
now, join these two frames.
'''

'''
now, see how well it did.
if good, make a model.
if bad, try something else
'''


'''
that didnt work, now just going to try and get something to work off of 
the whd csv
'''
