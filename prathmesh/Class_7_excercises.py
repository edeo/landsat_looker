# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 19:40:10 2014

@author: Prathmesh
"""

"""
HW EXERCISE:
1) Read in the 'hour.csv' file
"""

hours_dat = pd.read_csv("../data/hour.csv")

"""

2) Run the regression with: cnt ~ temp + hum + workingday + hour + C(weathersit)
"""

est_m = smf.ols(formula='cnt ~ temp + hum + workingday + hr + C(weathersit)', 
                data=hours_dat).fit()

"""
3) Evaluate the results, how does this compare with the day 
"""

est_n = smf.ols(formula='cnt ~ temp + hum + workingday + C(weathersit)', 
                data=bike_dat).fit()
                
The R squared value is higher in bike_dat as compared to hours_dat, meaning
that bike_dat model is a better fit than hours_dat. 

The hours _dat also has a Warning inidicating that the condition number is large,
 1.03e+03. This might indicate that there are strong multicollinearity or other numerical problems.


"""
4) Create a binary variable for rush hour defined by 6-9a & 4-6p
"""

rush_hour=(hours_dat.hr >= 6) & (hours_dat.hr <=9) | (hours_dat.hr >=16) & (hours_dat.hr<=18)

"""
5) Run the regression again. Does this new variable improve the results?
"""

est_m = smf.ols(formula='cnt ~ temp + hum + workingday + hr + C(weathersit) + rush_hour', 
                data=hours_dat).fit()
                
The new variable improves the model as the R squared value has increased from 
0.328 to 0.470.

The new model also shows clearly that during the rush hour there is higher
demand for  bikes. rush_hour[T.True]    150.2083

"""