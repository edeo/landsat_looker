bike_dat = pd.read_csv("hour.csv")
bike_dat.head()

# Plot the data in a scatter plot
plt.scatter(bike_dat.atemp, bike_dat.cnt, alpha=0.3)  # Plot the raw data

# Estimate the model parameters
est_s = smf.ols(formula='cnt ~ temp', data=bike_dat).fit()

# View the model estimates
est_s.summary()

est_m = smf.ols(formula='cnt ~ temp + hum + workingday + hr + C(weathersit)', 
                data=bike_dat).fit()
est_m.summary()



# stole this from http://stackoverflow.com/questions/15315452/selecting-with-complex-criteria-from-pandas-dataframe

bike_dat['rushmorn']=(bike_dat["hr"] > 6) & (bike_dat["hr"] < 9)
bike_dat['rusheve']=(bike_dat["hr"] > 16) & (bike_dat["hr"] < 18)
bike_dat['rush']=(bike_dat["rushmorn"] ==True) & (bike_dat["rusheve"] ==True)
est_rush = smf.ols(formula='cnt ~ temp + hum + workingday + hr + C(weathersit)+ rush', 
                data=bike_dat).fit()
est_rush.summary()
est_s.summary()
