# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 20:09:56 2014

@author: rafaan

Predicting Default Using Logistic Regression
"""
import numpy as np
import pandas as pd
import random


#reading in the data
df = pd.read_csv('data/Default.csv')

#changing df.student to binary values
df['student'] = np.where(df.student=='Yes', 1, 0)

#creating test and training set
sample_rows = random.sample(df1.index, 1000)
df_test = df.ix[sample_rows]
df_train = df.drop(sample_rows)

#histogram of all the variables
df.hist()

colors = np.where(df.default==1, 'r', 'b')
df.plot(x='income', y='balance', kind='scatter', alpha=0.3, c=colors)

