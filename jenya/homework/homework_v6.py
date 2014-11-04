# -*- coding: utf-8 -*-

# completed by @jenyazueva
"""
HW EXERCISE:
1) Read in the 'hour.csv' file
2) Run the regression with: cnt ~ temp + hum + workingday + hour + C(weathersit)
3) Evaluate the results, how does this compare with the day 
4) Create a binary variable for rush hour defined by 6-9a & 4-6p
5) Run the regression again. Does this new variable improve the results?
"""
import pandas as pd
import statsmodels.formula.api as smf

# 1) Read in the 'hour.csv' file

hour_file = pd.read_csv('data/hour.csv')
hour_file.columns
'''
Index([u'instant', u'dteday', u'season', u'yr', u'mnth', u'hr', u'holiday', u'weekday', 
       u'workingday', u'weathersit', u'temp', u'atemp', u'hum', u'windspeed', u'casual', 
       u'registered', u'cnt'], dtype='object')

alternative:

hour_file['hour'] = hour_file.hr
'''

# 2) Run the regression with: cnt ~ temp + hum + workingday + hour + C(weathersit)

reg_analyses = smf.ols(formula='cnt ~ temp + hum + workingday + hr + C(weathersit)', data=hour_file).fit()
reg_analyses.summary()

# 3) Evaluate the results, how does this compare with the day 
# do not understand the question?

# 4) Create a binary variable for rush hour defined by 6-9a & 4-6p
# bool value
hour_file['rush_hour'] = (hour_file.hr.between(6,9,inclusive=True)) | (hour_file.hr.between(16,18,inclusive=True))

# 5) Run the regression again. Does this new variable improve the results?

reg_analyses = smf.ols(formula='cnt ~ temp + hum + workingday + rush_hour + hr + C(weathersit)', data=hour_file).fit()
reg_analyses.summary()