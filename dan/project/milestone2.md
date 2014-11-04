# Data Exploration and Analysis Plan for high-growth neighborhoods in Washington, D.C.
* The goal of this exploration and analysis is to predict the top 10% high-growth neighborhoods in Washington, D.C. year-to-year using online real estate data.
* I am collecting three types of fixed time series real estate data from Trulia:
** Average listing price per neighborhood per week in 2012 and 2013
** Number of listings per neighborhood per week in 2012 and 2013
** Average search traffic per neighborhood per week in 2012 and 2013
* I will be using 12 highest growth neighborhoods in 2012 as my training set. Data from 2013 will be my test set 
* API calls per day are limited so I am still getting and cleaning data by month.  I will then combine data by month into two files - one for training, one for testing.
* This is a classification model so I may be using a logistic regression to make my predictions but I am exploring the possibility of using some of the financial analysis functions found in Wes McKinney's *Python for Data Analysis* to expand my prediction model.  