'''
L O G I S T I C   R E G R E S S I O N
Adapted From example given in Chapter 4 of 
Introduction to Statistical Learning
Data: Default Data Set
'''

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split

'''
QUIZ: UNDERSTANDING THE BASIC SHAPE
'''


'''
PART I - Exploration
'''

# 1 - Read in Default.csv and convert all data to numeric

def_dat  = pd.read_csv("../data/default.csv")

# Convert everything to numeric before splitting
def_dat.student = def_dat.student.map({'Yes': 1, 'No': 0})
def_dat.student.dtype
def_dat.balance.dtype
def_dat.income.dtype


# 2 - Split the data into train and test sets
columns = ['student','balance','income']

a_train, a_test, b_train, b_test = train_test_split(def_dat[columns], def_dat['default'], test_size=0.3, random_state=1)
# Can convert arrays back into dataframes if desired, for convenience later on

# 3 - Create a histogram of all variables
def_dat.hist()

# 4 - Create a scatter plot of the income vs. balance
def_dat.plot(x='income', y='balance', kind='scatter', alpha=0.3)

# 5 - Mark defaults with a different color and symbol
colors = np.where(def_dat.default, 'r', 'b')
##symbols = np.where(def_dat.default, u'o', u'v') -- doesn't work
def_dat.plot(x='income', y='balance', kind='scatter', c=colors)


# 6 - What can you infer from this plot?
'''
Defaults happen on larger loans most of the time
'''


'''
PART II - LOGISTIC REGRESSION
'''

# 1 - Run a logistic regression on the balance variable

# 2 - Is the beta value associated with balance significant?

# 3 - Predict the probability of default for someone with a balance of $1.2k and $2k

# 4 - Plot the fitted logistic function overtop of the data points

# 5 - Create predictions using the test set

# 6 - Compute the overall accuracy, the sensitivity and specificity
# Accuracy
# How many were classified correctly?

# Specificity
# For those who didn't default, how many did it predict correctly?

# Sensitivity
# For those who did default, how many did it predict correctly?