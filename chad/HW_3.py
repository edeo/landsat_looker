#!/usr/bin/env python
# ==================================================================
# Homework 3
# Chad Leonard
# October 24, 2014
# ==================================================================



"""
HW EXERCISE:
1) Read in the 'hour.csv' file
2) Run the regression with: cnt ~ temp + hum + workingday + hour + C(weathersit)
3) Evaluate the results, how does this compare with the day 
4) Create a binary variable for rush hour defined by 6-9a & 4-6p
5) Run the regression again. Does this new variable improve the results?

ANSWERS:
3) The day model has the best R squared value of all the models at .458 . 
5) After fixing the multicollinearity and creating the new binary variable for rush hour, 
   the R-squared for the Hours data improved from .328 to .395, so whether the time of day was in rush hour or not 
   does make a difference. 
"""

# Here is some made up data
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np

def my_scatter_plot(df,cols):
	my_scatter = pd.scatter_matrix(df[cols])
	plt.savefig(path + "/my_scatter.png")

def compare_counts(daydf,hourdf):
	matches = 0
	for i, row in enumerate(daydf.values):
		for idx in range(len(hourdf.index)):
			if row[1] == hourdf.index[idx]:
				if row[15] == hourdf[hourdf.index[idx]]:
					matches += 1
	return matches

def predictions(df,cols, model):
	val = df[cols]
	for i in range(len(df)):
		#print val.loc[[i]]
		y_hat = model.predict(val.loc[[i]])
		return y_hat

if __name__ == "__main__":
	path="../../../DAT3_All/DAT3/data"

	bike_hour_dat = pd.read_csv(path + "/hour.csv")

	#cols = ['cnt','temp','hum','workingday','hr','weathersit']


	# Create a ols model using the bike hour data
	model1 = smf.ols(formula='cnt ~ temp + hum + workingday + hr + C(weathersit)', data=bike_hour_dat).fit()

	#print est.summary()

	# Create a new ols model using the bike hour data where weathersit 4's are changed to 1's
	bike_hour_dat['new_weathersit'] = [wsit if wsit in [1,2,3] else 1 for wsit in bike_hour_dat['weathersit']]

	model2 = smf.ols(formula='cnt ~ temp + hum + workingday + hr + C(new_weathersit)', data=bike_hour_dat).fit()

	#print est_2.summary()

	
    #################################################
	# This section is to compare day.csv to hour.csv
	#################################################

	# Read in day.csv
	bike_dat = pd.read_csv(path + "/day.csv")

	# Create an OLS model for day data.
	model3 = smf.ols(formula='cnt ~ temp + hum +  C(weathersit)', data=bike_dat).fit()

	#print est_m.summary()

	# Use a bar plot to plot the 'Counts per hour'
	bike_hour_dat.groupby('hr').cnt.sum().plot(kind='bar', title='Counts per hour')
	plt.xlabel('Hour')
	plt.ylabel('Count')
	plt.savefig(path + "/my_bar_hr.png")

	# Use a groupby to get the total day counts for the hourly dataset.
	hourdf = bike_hour_dat.groupby('dteday').cnt.sum()

	# Do a little test to make sure the counts in the hour.csv match the counts in day.csv for the day, for sanity's sake.
	num_of_matches = compare_counts(bike_dat,hourdf)

	# Show results of comparison
	print "number of records in day.csv:", len(bike_dat), "number of records in hour.csv after groupby:", len(hourdf) \
	       , "number of counts that match from day.csv and hour.csv after groupby:", num_of_matches

	# Create a binary variable for rush hour defined by 6-9a & 4-6p
	bike_hour_dat['rush_hr_ind'] = [1 if hour in [6,7,8,9,16,17,18] else 0 for hour in bike_hour_dat['hr']]

	model4 = smf.ols(formula='cnt ~ temp + hum + workingday + C(rush_hr_ind) + C(new_weathersit)', data=bike_hour_dat).fit()

	# print new_est_m.summary()

	# print bike_hour_dat[['dteday','hr','rush_hr_ind']]

    #################################################
	# Test models and compare them.
	#################################################

	get_predictions = False
	est_cols = ['temp','hum','workingday','rush_hr_ind','new_weathersit']
	if get_predictions == True:
		result = predictions(bike_hour_dat, est_cols, model4)

	print "Model 1: Hours data with multicollinearity"
	print model1.summary()

	print "Model 2: Hours data without multicollinearity: created new_weathersit, which fixed the multicollinearity"
	print model2.summary()


	print "Model 3: Day data"
	print model3.summary()

	print "Model 4: Hours data without multicollinearity and with rush_hr_ind"
	print model4.summary()

	print "Rsquared for Model 1", model1.rsquared
	print "Rsquared for Model 2", model2.rsquared
	print "Rsquared for Model 3", model3.rsquared
	print "Rsquared for Model 4", model4.rsquared



