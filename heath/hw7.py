# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 17:14:46 2014

@author: Heath
"""
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np

"""
HW EXERCISE:
1) Read in the 'hour.csv' file
"""
hours_dat = pd.read_csv("../data/hour.csv")

"""
2) Run the regression with: cnt ~ temp + hum + workingday + hour + C(weathersit)
"""

est_m = smf.ols(formula='cnt ~ temp + hum + workingday + hr + C(weathersit)', data=hours_dat).fit()
est_m.summary()

"""
3) Evaluate the results, how does this compare with the day 
"""

est_n = smf.ols(formula='cnt ~ temp + hum + workingday + C(weathersit)', data=bike_dat).fit()
est_n.summary()

# R^2 for bike-data is larger than for hourly-data
# Bike-data is a better fit than the hourly-data

"""
4) Create a binary variable for rush hour defined by 6-9a & 4-6p
"""

#hour['rush2'] = 0
#hour['rush2'][((hour['hr'] >= 6 & (hour['hr'] <= 9)) | ((hour['hr']) >= 16 & (hour['hr'] <= 18)))] = 1

hour['rush5'] = [1 if hour_it in [6,7,8,9,16,17,18] else 0 for hour_it in hour['hr']]

"""
5) Run the regression again. Does this new variable improve the results?
"""
est_m = smf.ols(formula='cnt ~ temp + hum + workingday + hr + C(weathersit)', data=hours_dat).fit()
est_m.summary()
