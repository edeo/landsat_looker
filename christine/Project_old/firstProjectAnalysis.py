# -*- coding: utf-8 -*-
"""
Created on Sat Nov 01 16:54:16 2014

@author: 563572
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

df = pd.read_csv("february2014_ONTIME.csv")
df.head

plt.scatter(df.DEP_DELAY, df.ARR_DELAY)

plt.scatter(df.ORIGIN, df.DEST)

df.ORIGIN.describe()
airports = df.groupby("ORIGIN")["ORIGIN"].agg(np.count_nonzero).order(ascending=False)[0:25]
airports = pd.DataFrame(airports).index.values

df_origins =df[df.ORIGIN.isin(airports.index.values)]#airports.index.values]
##get rid of duplicates
df_origins = df_origins[df_origins.duplicated()==False]
##how to handle missing values
df_origins.value_counts(dropna=False)

##aggregate the data based on flight number and carrier



df_origins.boxplot(column="ARR_DELAY",by="ORIGIN")
df_origins.groupby("ORIGIN").agg(np.mean)[["CARRIER_DELAY", "WEATHER_DELAY", "ARR_DELAY", "DEP_DELAY"]]
df_origins.groupby("ORIGIN").agg(np.amin, np.amax, np.mean)[["CARRIER_DELAY", "WEATHER_DELAY", "ARR_DELAY", "DEP_DELAY"]]

df_origins.boxplot(column="ARR_DELAY", by = "CARRIER")
df_origins.groupby("CARRIER")["CARRIER"].agg(np.count_nonzero).order(ascending=False)
## Delta, Southwest, American, United,
##i dont recognize alot of these carriers 
a = df_origins.groupby("CARRIER")["ARR_DELAY"].describe()
df_origins.groupby("CARRIER").agg({"ARR_DELAY": [np.mean, np.median]})
df_origins.groupby("CARRIER").agg({"DEP_DELAY": [np.mean, np.median]})
df_origins.groupby("CARRIER").agg({"ARR_DELAY": [np.mean, np.median]})

df_origins.CANCELLED.describe() #binary 

from sklearn.neighbors import KNeighborsClassifier  # import class
X = df[["DAY_OF_WEEK","CARRIER", "ORIGIN", "DEST", "DEP_TIME", "AIR_TIME", "DISTANCE", "SECURITY_DELAY", "LONGEST_ADD_GTIME"]] 
X = df_origins[["DAY_OF_WEEK","DEP_TIME", "AIR_TIME", "DISTANCE","SECURITY_DELAY", "LONGEST_ADD_GTIME"]]
y = df_origins["CANCELLED"]
X.shape
y.shape
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)                                       # fit with data


df_origins.DIVERTED.describe() #binary

##we can also 

df_origins[df_origins.ARR_DELAY < 0 ].ARR_DELAY.hist(by=df_origins.ORIGIN,sharex=True)
df_origins[df_origins.ARR_DELAY > 0 ].ARR_DELAY.hist(by=df_origins.ORIGIN,sharex=True)

### plot delay times (y axis) and time of day (x axis)
colors = np.where(df_origins.CARRIER=="AA","r","b")

df_origins.plot(x="DEP_TIME", y = "ARR_DELAY", kind="SCATTER",c=colors,alpha=.3)

###plot delay times over the course of the entire time

df_origins.groupby("ORIGIN").agg(np.percentile)["ARR_DELAY"]

df_origins.groupby("ORIGIN")["ARR_DELAY"].describe()

est_s = smf.ols(formula='ARR_DELAY ~ C(ORIGIN) ', data=df_origins).fit() #+ C(CARRIER)
est_s.summary()

## just look at time
est_s = smf.ols(formula = "ARR_DELAY ~ DAY_OF_WEEK + DEP_TIME + AIR_TIME + DISTANCE + SECURITY_DELAY + TOTAL_ADD_GTIME", data=df_origins).fit()
est_s.summary()
## CARRIER


#DEp_TIME, 