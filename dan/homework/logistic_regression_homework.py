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

default = pd.read_csv('data/Default.csv')

# Convert everything to numeric before splitting
default.replace(to_replace='Yes', value=0, inplace=True)
default.replace(to_replace='No', value=1, inplace=True)

# 2 - Split the data into train and test sets

# Can convert arrays back into dataframes if desired, for convenience later on
defaultTrain = default[0:6999]
defaultTest = default[7000:10000]
X, y = defaultTrain, defaultTest

# 3 - Create a histogram of all variables
default.hist()
# 4 - Create a scatter plot of the income vs. balance

default.plot(x='income', y='balance', kind = 'scatter')

# 5 - Mark defaults with a different color and symbol
colors = np.where(default.default==1, 'r', 'b')
default.plot(x='income', y='balance', kind = 'scatter', c='colors')

# 6 - What can you infer from this plot?

#Solutions:
d = pd.read_csv('data/Default.csv')
d.head()
d.describe()

d.student = np.where(d.student == 'Yes', 1, 0)

train, test = train_test_split(d,test_size=0.3, random_state=1)

train = pd.DataFrame(data=train, columns=d.columns)
test = pd.DataFrame(data=test, columns=d.columns)

train.hist()

train.plot(x='balance', y='income', kind='scatter', alpha=0.3)

train_nd = train[train.default == 0]
train_d = train[train.default == 1]

plt.figure()
plt.scatter(train_nd.balance, train_nd.income, alpha=.5, marker='+', c='b')

plt.scatter(train_d.balance, train_d.income, marker = 'o', 
            edgecolors = 'r', facecolors = 'none')
plt.ylim([0,8000]); plt.xlim([0,2800])
plt.legend(('default','no default'), loc='upper right')

'''
PART II - LOGISTIC REGRESSION
'''

#Solution:

balance = smf.logit('default ~ balance', data=train).fit()
balance.summary()
np.exp(balance.params.balance)

prob = balance.predict({'balance': [1200,2000]})

x= np.linspace(test.balance.min(), test.balance.max(),500)
beta = [balance.params.Intercept, balance.params.balance]

y = np.exp(beta[0] + beta[1]*x) / (1 + np.exp(beta[0] + beta[1]*x))

odds = np.exp(beta[0] + beta[1]*x)
log_odds = beta[0] + beta[1]*x


plt.figure(figsize=(7,8))

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