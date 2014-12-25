# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 15:25:30 2014

@author: danielmatthews
"""

import pandas as pd
import csv
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

raw = pd.read_csv('project/data/nfl_weather_data.csv')

d = raw[['home_score','away_score','temperature','wind_chill','humidity','wind_mph','weather']]

d['score_differential'] = raw.home_score - raw.away_score
d['score_dif'] = d.score_differential.abs()

d['humidity_stripped'] = raw.humidity.str.strip("%")
d.humidity_stripped.fillna(0, inplace=True)
d['humid'] = d.humidity_stripped.astype('int')
d.humid

df = d[['temperature','wind_mph','humid','score_dif']]
df.wind_mph.fillna(0, inplace=True)


df.to_csv('nflWeather.csv')

plt.scatter(d.score_dif, d.temperature, alpha=0.3)

with open('nfl_weather.csv', 'wb') as f:
    csv.writer(f).writerows(df)
