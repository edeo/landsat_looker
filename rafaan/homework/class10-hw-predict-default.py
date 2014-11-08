# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 20:09:56 2014

@author: rafaan

Predicting Default Using Logistic Regression
"""
import numpy as np
import pandas as pd
import random
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split


#reading in the data
df = pd.read_csv('data/Default.csv')

#changing df.student to binary values
df['student'] = np.where(df.student=='Yes', 1, 0)

#creating test and training set
sample_rows = random.sample(df.index, 1000)
df_test = df.ix[sample_rows]
df_train = df.drop(sample_rows)
df_target = df['balance']

#another way to create test and training set
train, test = train_test_split(df, test_size=0.3, random_state=1)
train = pd.DataFrame(data=train, columns=df.columns)
test = pd.DataFrame(data=test, columns=df.columns)

#histogram of all the variables
df_train.hist()

#scatter plot of balance vs income
colors = np.where(df.default==1, 'r', 'b')
df.plot(x='balance', y='income', kind='scatter', alpha=0.3, c=colors)

'''
Fitting the Model and Predicting
'''

#fitting the logistic model i.e., running the regression
est_df = smf.logit(formula='default ~ balance' , data=df_train).fit()
est_df.summary()

#creating a dataframe of the x values to use to predict y
x_prime = pd.DataFrame({'balance': [1200,2000]})
x_prime2 = pd.DataFrame(df_test.balance)

#predicting the y values using the previously created dataframe of x values
y_hat = est_df.predict(x_prime)  
y_hat_test = est_df.predict(x_prime2)

    #another way to predict the y values
    prob = est_df.predict({'balance': [1200,2000]})
                                         



