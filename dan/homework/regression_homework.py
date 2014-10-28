# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 18:06:59 2014

@author: danielmatthews
"""
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
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np

bike_dat = pd.read_csv("../data/day.csv")

est_s = smf.ols(formula='cnt ~ temp + hum + workingday + hour + C(weathersit)', data=bike_dat).fit()

rush_hour = 
