# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 17:01:45 2014

@author: danielmatthews
"""

import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np

DF = pd.read_csv('project/data/nflWeather.csv')
DF

nfl_dat = DF.drop('Unnamed: 0', 1)
nfl_dat

plt.scatter(nfl_dat.score_dif, nfl_dat.temperature, alpha=0.3)
pd.scatter_matrix(nfl_dat)

est = smf.ols(formula='np.log(score_dif) ~ temperature', data=nfl_dat).fit()

plt.scatter(nfl_dat.score_dif, np.log(nfl_dat.humid), alpha=0.3)

est.summary()

x_prime = pd.DataFrame({'temperature': np.linspace(nfl_dat.temperature.min(), 
                                             nfl_dat.temperature.max(), 100)})
                                             
nfl_dat['w'] =  1 / (nfl_dat['temperature'])

est_wls = smf.wls(formula='score_dif ~ temperature', data=nfl_dat, weights = nfl_dat['w']).fit()


y_hat = est.predict(x_prime)
y_hat_wls = est_wls.predict(x_prime)

plt.xlabel("temperature")
plt.ylabel("score differential")
plt.title("OLS (red) vs. WLS (blue)")
plt.scatter(nfl_dat.score_dif, nfl_dat.temperature, alpha=0.3)
plt.plot(x_prime, y_hat, 'r', linewidth=2, alpha=0.9)
plt.plot(x_prime, y_hat_wls, 'b', linewidth=2, alpha=0.9)
