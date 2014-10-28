# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 17:14:46 2014

@author: Heath
"""

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
