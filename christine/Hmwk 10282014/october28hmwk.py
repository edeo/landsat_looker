"""
EXERCISE:
1) Read in the 'hour.csv' file
2) Run the regression with: cnt ~ temp + hum + workingday + hour + C(weathersit)
3) Evaluate the results, how does this compare with the day 
3) Create a binary variable for rush hour defined by 6-9a & 4-6p
4) Run the regression again. Does this new variable improve the results?
"""
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
# 1
bike_dat = pd.read_csv("hours.csv")
bike_dat.head()
len(bike_dat)
"""
 weathersit : 
- 1: Clear, Few clouds, Partly cloudy, Partly cloudy 
- 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist 
- 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds 
- 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog 
"""

#2 and 3
hours_lm = smf.ols(formula='cnt ~ temp + hum + workingday + hr + C(weathersit)', data=bike_dat).fit()
hours_lm.summary()
##R-squared is only .328, the weathersit[T.4] is not significant
##all other variables' CI do not include 0



bike_dat_days = pd.read_csv("days.csv")
bike_dat_days.head()
len(bike_dat_days)
days_lm = smf.ols(formula='cnt ~ temp + hum + workingday + C(weathersit)', data=bike_dat_days).fit()
days_lm.summary()

##R-squared is higher for the daily model
## workingday is not significant if p is 5%

bike_dat['hr'].describe() #values take on 0  23
bike_dat['rushhour']=bike_dat['hr'].apply(lambda x: 1 if (x>=6 and x<=8) or (x>=16 and x<=18) else 0)
#[1 if (bike_dat['hr']>=6 & bike_dat['hr']<=8) | (bike_dat['hr']>=16 & bike_dat['hr']<=18) else 0 for row in bike_dat]

rush_lm = smf.ols(formula='cnt ~ temp + hum + workingday + rushhour + C(weathersit)', data=bike_dat).fit()
rush_lm.summary()
##this variable does improve results but the binary varialbes for weathersit are not significant
rush_lm_2 = smf.ols(formula='cnt ~ temp + hum + workingday + rushhour', data=bike_dat).fit()
rush_lm_2.summary()
##removing did not increase R squared
##how do you remove just one/two of the C(weathersit) variables
