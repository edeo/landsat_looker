"""
EXERCISE:
1) Read in the 'hour.csv' file
"""
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
hour = pd.read_csv("hour.csv")
"""
2) Run the regression with: cnt ~ temp + hum + workingday + hour + C(weathersit)
"""
reg = smf.ols(formula='cnt ~ temp + hum + workingday + hr + C(weathersit)', data=hour).fit()
"""
3) Evaluate the results, how does this compare with the day
"""
reg.summary()
#the adjusted R-squared is lower (.328 vs .457)
#this model includes a a C(weathersit)[T.3] variable
#the 'workingday' variable is statistically significant with the inclusion of the 'hr' variable
"""
4) Create a binary variable for rush hour defined by 6-9a & 4-6p
"""
hour['rush'] = 0
hour['rush'][hour['hr'] == 6] = 1
hour['rush'][hour['hr'] == 7] = 1
hour['rush'][hour['hr'] == 8] = 1
hour['rush'][hour['hr'] == 9] = 1

hour['rush'][hour['hr'] == 16] = 1
hour['rush'][hour['hr'] == 17] = 1
hour['rush'][hour['hr'] == 18] = 1
"""
5) Run the regression again. Does this new variable improve the results?
"""
reg2 = smf.ols(formula='cnt ~ temp + hum + workingday + hr + C(weathersit) + rush', data=hour).fit()
reg2.summary()
#the adjusted R-squared is higher than both previous models at .47
#every variable is significant except [T.4]