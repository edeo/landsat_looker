##initial step in the analysis process

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

##read in the february file
df = pd.read_csv("february2014_ONTIME.csv")
#check out the file
df.head
#remove any duplicates
df.ORIGIN.drop_duplicates()
## for the purposes of narrowing the scope of the project, initially
## look at flights in and out of DCA (washington National airport)
## two dataframes are created, one where the flgiths originate in DCA
## another where flights fly into DCA
dfDCA_out =df[df.ORIGIN=="DCA"]
dfDCA_in = df[df.DEST == "DCA"]

plt.scatter(dfDCA_out.DEP_DELAY, dfDCA_out.ARR_DELAY, c="b", alpha=.2)
plt.scatter(dfDCA_in.DEP_DELAY, dfDCA_in.ARR_DELAY, c="g", alpha=.2)

## aggregate the dataset to see how many outbound flights there are
## were destination airport
outbound = dfDCA_out.groupby('DEST').count()["YEAR"]
#sort outbound to see which airports have the greatest 
## number of flights originating out of DCA
outbound = pd.DataFrame(outbound).sort("YEAR",ascending=False)
outbound['airport']=outbound.index
outbound.columns = ('feb_flights','airport_id')

inbound = pd.DataFrame(dfDCA_in.groupby("ORIGIN").count()["YEAR"]).sort("YEAR", ascending=False)
inbound['airport']=inbound.index
inbound.columns = ('feb_flights','airport_id')

## look at the top carriers into DCA
top_carriers_in = dfDCA_in.groupby('CARRIER').count()["YEAR"]
top_carriers_in = pd.DataFrame(top_carriers_in).sort("YEAR", ascending=False)
## look at the top carriers out of DCA
top_carriers_out = dfDCA_out.groupby('CARRIER').count()["YEAR"]
top_carriers_out = pd.DataFrame(top_carriers_out).sort("YEAR", ascending=False)
## these tables are nearly identical 
## this is a good check - the number of flights into DCA should be the number
## of flights out DCA - broken down by Carrier

dfDCA_in.ORIGIN.describe()
#create some visualizations of arrival delay based on the origin airport
#for those flights flying INTO DCA
aoi =  np.array(inbound.airport_id[range(10)])
dfDCA_in[dfDCA_in.ORIGIN.isin(aoi)].boxplot(column="ARR_DELAY",by="ORIGIN").set_ylim(-50,200)
dfDCA_in[dfDCA_in.ORIGIN.isin(aoi)].groupby("ORIGIN")["ARR_DELAY"].agg(np.mean)
dfDCA_in.ARR_DELAY.mean()
#lets narrow down which flights we wnat to look at
aoi = np.array(outbound.airport_id[range(10)])
dfDCA_out[dfDCA_out.DEST.isin(aoi)].boxplot(column="DEP_DELAY",by="DEST").set_ylim(-50,200)
dfDCA_out[dfDCA_out.DEST.isin(aoi)].groupby("DEST")["DEP_DELAY"].agg(np.mean)
dfDCA_out.DEP_DELAY.mean()

#airports = df.groupby("ORIGIN")["ORIGIN"].agg(np.count_nonzero).order(ascending=False)[0:25]
#airports = pd.DataFrame(airports).index.values
#### US 1636
#### AA 696
#### DL 677
#### MQ 564
#### B6 488
#### UA 422
#df_origins =df[df.ORIGIN.isin(airports.index.values)]#airports.index.values]
###get rid of duplicates
#df_origins = df_origins[df_origins.duplicated()==False]
###how to handle missing values
#df_origins.value_counts(dropna=False)

##pull in airport dataset with column names
AIRPORT_COLS = ('airport_name', 'city', 'country', 'iata', 'icao', 'latitude', 'longitude', 'altitude', 'timezone', 'dst', 't')
airports = pd.read_csv('airports.dat', header=None, names=AIRPORT_COLS)

outbound2 = pd.merge(outbound,airports, left_on='airport_id', right_on='iata',how='left')
outbound2['originatingLat'] = 38.852083 #airports[airports.iata=="DCA"]["latitude"] 
outbound2['originatingLong'] = -77.037722
#plt.scatter(dfDCA.ORIGIN, dfDCA.DEST)

###aggregate the data based on flight number and carrier
#
#import matplotlib.cm as cm
#carrier_oi = ['US','AA','DL','MQ','B6','UA']
#colors = cm.rainbow(np.linspace(0, 1, 6)) #len(dfDCA_in.CARRIER[dfDCA_in.CARRIER.duplicated()==False])))
#
##colors = np.where(dfDCA_in.CARRIER=="AA","r","b")
#
##color=next(colors)
#for i in range(6)[1:6]:
#    ty = carrier_oi[i]
#    color = colors[i]
#    d = dfDCA_in[(dfDCA_in.ARR_DELAY > 0) & (dfDCA_in.CARRIER == ty)]
#    plt.scatter(x=d.DEP_TIME, y = d.ARR_DELAY, c=color,alpha=.3)
###map colors to carrier , x is dep time, y is arr delay

##aggregate flights based on the origin and the carrier (in this dataset all dest are DCA)
agg_in = dfDCA_in.groupby(["ORIGIN", "CARRIER"])[["ARR_DELAY","DISTANCE","DEP_DELAY","TAXI_OUT","TAXI_IN","AIR_TIME","CANCELLED"]].agg(np.mean)
##want to add a # of flight columns - indicate some type of frequency here
agg_in_1 = dfDCA_in.groupby(["ORIGIN", "CARRIER"])["ORIGIN"].agg(np.count_nonzero)
agg_in['FREQ'] = agg_in_1
agg_in['DEST'] = "DCA"
agg_in["Direction"]="Into" #indicate that we are flying into DCA
agg_in = agg_in.reset_index()

##aggregate flights based on the destination and the carrier (in this dataset all origin are DCA)
agg_out = dfDCA_out.groupby(["DEST","CARRIER"])[["ARR_DELAY","DISTANCE","DEP_DELAY","TAXI_OUT","TAXI_IN","AIR_TIME","CANCELLED"]].agg(np.mean)
agg_out_1 = dfDCA_out.groupby(["DEST", "CARRIER"])["ORIGIN"].agg(np.count_nonzero)
agg_out['FREQ'] = agg_out_1
agg_out["ORIGIN"]="DCA"
agg_out["Direction"]="Out" #indicate that we are leaving DCA
agg_out = agg_out.reset_index()

#both agg_in and agg_out have the same columns that we can append them

#now we pull in airport.dat
AIRPORT_COLS = ('airport_name', 'city', 'country', 'iata', 'icao', 'latitude', 'longitude', 'altitude', 'timezone', 'dst', 't')
airports = pd.read_csv('airports.dat', header=None, names=AIRPORT_COLS)
#use the merge function to crosswalk the origin airport with the aiport.dat's
#lats and longs
#use the IATA airport code to do so since that is the code used in RITAs dataset
agg_in = agg_in.merge(airports, left_on='ORIGIN', right_on='iata')
agg_in['DEST_lat'] = 38.852083 #use DCA's lsts and longs
agg_in['DEST_long'] = -77.037722
#next we make sure that all column names are the same 
agg_in=agg_in.rename(columns = {'latitude':'ORIGIN_lat'})
agg_in=agg_in.rename(columns = {'longitude':'ORIGIN_long'})

agg_out = agg_out.merge(airports, left_on='DEST', right_on='iata')
agg_out['ORIGIN_lat'] = 38.852083 #airports[airports.iata=="DCA"]["latitude"] 
agg_out['ORIGIN_long'] = -77.037722
#next we make sure that all column names are the same 
agg_out = agg_out.rename(columns = {'latitude': 'DEST_lat'})
agg_out = agg_out.rename(columns = {'longitude': 'DEST_long'})

#append the in and out aggregate files
agg = agg_in.append(agg_out)

#write to a csv so that it can be plotted in an r script
agg.to_csv("aggregate_DC.csv")

##plot distance and arrival delay and change the colors of points based on whether
##the flight is technically delayed (red)
##falls within the 0-15 minute grace period (green)
##arrives early is blue
color = np.where(agg.ARR_DELAY>15, 'r', np.where(agg.ARR_DELAY>0,'g', 'b'))
plt.scatter(agg.DISTANCE, agg.ARR_DELAY, c=color)#.set_ylim(-25,200)#, c=agg.CARRIER)#, cmap=cm.colormap_name, alpha=.2)
plt.ylim(-25,100)
plt.xlim(0,2500)
##looks like once you get 1500 your flight is less likely to be late
##makes sense - flights have a some buffer in time 
##30 minute late flight was SJU - Puerto Rico
##maybe flights direction is important in determing lateness
agg[agg.DISTANCE > 1500]
##outliers are DTW - single flight a year
delay_time_ratios = agg[agg.DISTANCE < 500].groupby("ORIGIN")[["AIR_TIME","ARR_DELAY"]].agg(np.mean)
delay_time_ratios["ratio"] = delay_time_ratios.ARR_DELAY/delay_time_ratios.AIR_TIME

###maybe look at Laguardia## airports notorious for delay


#######################################
##use variables to predict prob of cancelatoin and prob of delay or the actual delay


#################################################################################

dfDCA_in.groupby("ORIGIN").agg(np.mean)[["CARRIER_DELAY", "WEATHER_DELAY", "ARR_DELAY", "DEP_DELAY"]]
dfDCA_in.groupby("ORIGIN").agg(np.amin, np.amax, np.mean)[["CARRIER_DELAY", "WEATHER_DELAY", "ARR_DELAY", "DEP_DELAY"]]

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