# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 20:09:42 2014

@author: Prathmesh
"""
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
import requests
from pprint import pprint
import csv

#Sample API for one Player
r = requests.get('http://fantasy.premierleague.com/web/api/elements/266/')
top = r.text    # unicode text string
top = r.json()  # dictionary
pprint(top)



#for loop for scrapping api
s1='http://fantasy.premierleague.com/web/api/elements/'

from time import sleep

players = []
for player_link in range(1,100,1):
    link = s1+""+str(player_link)
    r = requests.get(link)
    player =r.json() 
    players.append(player)
    sleep(2)

#CSV write
with open('/Users/Prathmesh/Documents/Data-Science-Course/Project/dict_output.csv', 'wb') as f:  # Just use 'w' mode in 3.x
     w = csv.DictWriter(f,player.keys())
     w.writeheader()
     for player in players:        
         w.writerow(player)

# Reading CSV into Pandas DataFrame
players_df = pd.read_csv('/Users/Prathmesh/Documents/Data-Science-Course/Project/dict_output.csv',index_col='web_name', na_filter=False)

players_df.head()
players_df.tail()

#Some random plotting to determine which attributes to use in the final model
plt.scatter(players_df.value_form, players_df.points_per_game, alpha=0.3)
plt.scatter(players_df.value_season, players_df.points_per_game, alpha=0.3) 

players_df.type_name

est_s = smf.ols(formula='points_per_game ~ type_name', data=players_df).fit()

"""
I wrote a script, to pull the data from the API hosted by the Fantasy Premier League Website into a Dictionary. 
Then I used CSVDict Writer that converted the Dictionary into a CSV file.
The CSV consists of 59 Columns Player attributes as Columns and each row consisting of each individual player.	
I'm trying to narrow the attributes to 3-4 key attributes. On which I will run the linear Regression model.
So I'm currently trying to plot the various attributes to see which has a bigger impact on the Y variable, which I've identified as the tota points scored.
Identifying this key variables is the biggest challenge I face currently.

"""