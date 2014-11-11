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
df = pd.read_csv('data/Default.csv')

# Convert everything to numeric before splitting
for row in df['student']:
    if row == 'Yes':
        df['student_2'] = 1
    else:
        df['student_2'] = 0

del df['student']

# 2 - Split the data into train and test sets

train, test = train_test_split(df, test_size=0.3, random_state = 1)
                          
# Can convert arrays back into dataframes if desired, for convenience later on
train_df = pd.DataFrame(train, columns = ['default', 'balance', 'income','student_2'])
test_df = pd.DataFrame(test, columns = ['default', 'balance', 'income','student_2'])

# 3 - Create a histogram of all variables
# hint:                           train_dataframe.hist()

train_df.hist()
test_df.hist()
# 4 - Create a scatter plot of the income vs. balance

plt.scatter(train_df.income, train_df.balance, alpha=0.2) 

# 5 - Mark defaults with a different color and symbol
colors = np.where(train_df.default == 1, 'r', 'b')

train_df.plot(x='income', y='balance', kind='scatter', c=colors)


# 6 - What can you infer from this plot?

# hypothesis: People who set their card to be their default card are more likely to carry balance
