# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 15:57:23 2014

@author: lindaxie
"""

import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np


"""
HW EXERCISE:
1) Read in the 'hour.csv' file
2) Run the regression with: cnt ~ temp + hum + workingday + hour + C(weathersit)
"""
# read in hour data and run regression
bike_dat_hr = pd.read_csv("hour.csv")
plt.scatter(bike_dat_hr.hr, bike_dat_hr.cnt, alpha=0.3)# Scatter plot 
est_hr = smf.ols(formula='cnt ~ temp + hum + workingday + hr + C(weathersit)', 
                data=bike_dat_hr).fit()
#cols = ['cnt','hr','weathersit','temp','workingday','hum']
#pd.scatter_matrix(bike_dat_hr[cols])
#lines above might crash python console

# read in day data and run regression
bike_dat_day = pd.read_csv("day.csv")
est_day = smf.ols(formula='cnt ~ temp + hum + workingday + C(weathersit)', 
                data=bike_dat_day).fit()

"""
3) Evaluate the results, how does this compare with the day 
-The hourly csv contains a lot more data points than the daily csv. This might 
 explain why the R^2 value for the daily regression is slightly larger
-The 'workingday' variable was not signicant in the daily regression, but was
    in the hourly regression
-Other correlations remained the same
    -temp is positively correlated with count
    -humidity is negatively correlated with count
-The new input variable 'hr' is positively correlated with count, which makes 
    sense since most people do not ride bikes at 1-5am in the morning. But as
    the hour increases, people are more likely to rent bikes
-For the categorical variable 'weathersit', the trend is a little different
    -for the daily regression- the count is the highest when weathersit = 1
     (ie. sunny), and drops as the situation gets worse
    -for the hourly regression- the count about the same for weathersit = 1 and 2
     the count drops when the weathersit = 3 (rainy), but surprising increases when 
     weathersit = 4 (maybe b/c data with weathersit=4 is smaller?), and the p value
     is >0.05, which means that this coeff is inconclusive... the coef is also
     a lot smaller compared to the daily regression: which indicates that the
     other response variables play a more important role in the regression
"""

"""
4) Create a binary variable for rush hour defined by 6-9a & 4-6p
"""

bike_dat_hr_new = bike_dat_hr
bike_dat_hr_new['rushHourInd'] = (((bike_dat_hr_new['hr'] >= 6) & (bike_dat_hr_new['hr'] <= 9))
|((bike_dat_hr_new['hr'] >= 16) & (bike_dat_hr_new['hr'] <= 18))).astype(int)
est_hr_new = smf.ols(formula='cnt ~ temp + hum + workingday + hr + rushHourInd + C(weathersit)', 
                data=bike_dat_hr_new).fit()
"""
5) Run the regression again. Does this new variable improve the results?
I think adding a rushHourIndicator did improve the model. The new model thinks that there tends
to be more bikes rented out during rush hour (the coeff for rushHourInd is positive 150).
The introduction of the rush hour indicator did make weathersit = 3 and 4 insignificant.
But R^2 in this new model is 0.47, which is higher and means that it's a slightly better fit. 

"""