# -*- coding: utf-8 -*-

'''
PART I - Exploration
'''

# 1 - Read in Default.csv and convert all data to numeric
import pandas as pd
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split

default_dat = pd.read_csv("../data/default.csv")
default_dat.head()

# Convert everything to numeric before splitting

default_dat.student = default_dat.student.map({'Yes': 1, 'No': 0})

# 2 - Split the data into train and test sets

cols = ['student','balance','income']


X_train, X_test, y_train, y_test = train_test_split(default_dat[cols], default_dat['default'],

# 3 - Create a histogram of all variables                                                    test_size=0.3, random_state=1)
default_dat.hist()                                                   

# 4 - Create a scatter plot of the income vs. balance
default_dat.plot(x='income', y='balance', kind='scatter', alpha=0.3)

# 5 - Mark defaults with a different color and symbol

colors = np.where(default_dat.default, 'r', 'b')                                                    
default_dat.plot(x='income', y='balance', kind='scatter', c=colors)