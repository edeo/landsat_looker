# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 20:09:42 2014

@author: Prathmesh
"""
#Importing Various Python modules 

import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
import requests
from pprint import pprint
import csv
from time import sleep

#Sample API for one Player
r = requests.get('http://fantasy.premierleague.com/web/api/elements/266/')
top = r.text    # unicode text string
top = r.json()  # dictionary
pprint(top)



#for loop for scrapping api for all the players
#Reviewers Don't need to Run this Step as I've already got the data in CSV
#This is a time consuming process as this step is accessing web api

s1='http://fantasy.premierleague.com/web/api/elements/'

players = []
for player_link in range(1,624,1):
    link = s1+""+str(player_link)
    r = requests.get(link)
    player =r.json() 
    players.append(player)
    sleep(1)

#Writing the Data from the API into a CSV file
with open('/Users/Prathmesh/Documents/Data-Science-Course/Project/dict_output1.csv', 'wb') as f:  # Just use 'w' mode in 3.x
     w = csv.DictWriter(f,player.keys())
     w.writeheader()
     for player in players:        
         w.writerow(player)

# Reading CSV into Pandas DataFrame
players_df = pd.read_csv('/Users/Prathmesh/Documents/Data-Science-Course/Project/dict_output1.csv',index_col='web_name', na_filter=False)

#Observing the Data for Exploration
players_df.head()
players_df.tail()

#Some random plotting to determine which attributes to use in the final model
# I did this step for various variables but it didn't reveal much to me.
plt.scatter(players_df.value_form, players_df.points_per_game, alpha=0.3)
plt.scatter(players_df.value_season, players_df.points_per_game, alpha=0.3) 
plt.scatter(forwards_df.bps, forwards_df.points_per_game, alpha=0.3) 
plt.xlabel("BPS")
plt.ylabel("Points Per Game")

#Filtering the data only for Forwards
players_df[players_df.type_name=='Forward'].to_csv('../data/players_updated.csv')

forwards_df = pd.read_csv('/Users/Prathmesh/Documents/Data-Science-Course/Project/players_updated.csv',index_col='web_name', na_filter=False)

#Creating Linear Model for Forwards

forwards_model = smf.ols(formula='event_total ~ selected_by + value_form + value_season + form + ea_index + bps', data=forwards_df).fit()
forwards_model.summary()

# Exploring Multi-collinearity between Variables
columns = ['event_total', 'selected_by', 'value_form', 'value_season', 'form','ea_index','bps']
pd.scatter_matrix(forwards_df[columns])

corr_matrix = np.corrcoef(forwards_df[columns].T)
sm.graphics.plot_corr(corr_matrix, xnames=columns)

# Its obvious from the Correlation Matrix that there is correlation between bps - ea_index & form - value_form
# Hence removing bps & value_from model and exploring
forwards_model = smf.ols(formula='event_total ~ selected_by + form + value_season + ea_index', data=forwards_df).fit()
forwards_model.summary()


#Trying Interaction terms to handle Correlation
# But it still produces multicollinearity Error.
interaction_model = smf.ols(formula='event_total ~ selected_by + value_form:form + value_season + ea_index:bps', data=forwards_df).fit()
interaction_model.summary()


# Split the data into train and test sets
#Using different method to create train test due to error using the train_test_split
forwards_df = pd.read_csv('/Users/Prathmesh/Documents/Data-Science-Course/Project/players_updated.csv',index_col='id', na_filter=True)

df = pd.DataFrame(np.random.randn(107, 2))

msk = np.random.rand(len(forwards_df)) < 0.8

train = forwards_df[msk]

test = forwards_df[~msk]

# Run a linear regression on the train test
f1_model = smf.ols(formula='event_total ~ selected_by + form + value_season + ea_index', data=train).fit()
f1_model.summary()

# Create predictions using the train model on the test set
test['pred'] = f1_model.predict(test)

# Printing actual and predicted values side by side to explore
#Clearly at this stage the predictions are not accurate & model needs more tweaking.
test[['event_total','pred']]



#Extra exploring
# Creating a model using the variables which directly affect the totals points scored
# This is just for Exploration purposes and Reviewers and Ignore This
#I've eliminated this variables from final model because of the direct relationship between them and Y. 
obvious_model = smf.ols(formula='event_total ~ goals_scored + assists + minutes ', data=forwards_df).fit()
obvious_model.summary()
