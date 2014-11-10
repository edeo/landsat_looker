# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 20:09:44 2014

@author: lindaxie
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 1) Read in Default.csv and convert all data to numeric

raw = pd.read_csv('Default.csv')    
raw.student = raw.student=='Yes'
raw.student = raw.student.astype(int)


data = []
for x in range(0, len(raw.student.values)):
    data.append([raw.student.values[x], raw.balance.values[x], raw.income.values[x]]) 
target = raw.default.values

#2) Split the data into train and test sets
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data, target,
                                                    test_size=0.3, random_state=1)

#3) Create a histogram of all variables
#plt.hist(raw.student)
#plt.hist(raw.balance)
#plt.hist(raw.income)
raw.hist()

#4) Create a scatter plot of the income vs. balance
plt.scatter(raw.income, raw.balance, alpha = 0.7)

#5) Mark defaults with a different color (and symbol)
plt.scatter(raw.income[raw.default==0], raw.balance[raw.default==0], marker = '.',alpha = 0.3)
plt.scatter(raw.income[raw.default==1], raw.balance[raw.default==1], marker = '^', alpha = 0.7, color='r')
plt.xlabel('income')
plt.ylabel('balance')

#6) What can you infer from this plot?
"""
-there are very few defaults when the income is really low or really high
-the default rate seems high only when balance is high
"""