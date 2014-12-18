##initial step in the analysis process

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

##read in the february file
df = pd.read_csv("December_2013.csv")#february2014_ONTIME.csv")
#check out the file
df.head
#remove any duplicates
df.ORIGIN.drop_duplicates()
## for the purposes of narrowing the scope of the project, initially
## look at flights in and out of DCA (washington National airport)
## two dataframes are created, one where the flgiths originate in DCA
## another where flights fly into DCA
dfDCA_out =df[df.ORIGIN=="DCA"]
dfDCA_out.Direction = "outbound"
dfDCA_in = df[df.DEST == "DCA"]
dfDCA_in.Direction = "inbound"

df_DCA = dfDCA_in.append(dfDCA_out)

#now we pull in airport.dat
AIRPORT_COLS = ('airport_name', 'city', 'country', 'iata', 'icao', 'latitude', 'longitude', 'altitude', 'timezone', 'dst', 't')
airports = pd.read_csv('airports.dat', header=None, names=AIRPORT_COLS)
#use the merge function to crosswalk the origin airport with the aiport.dat's
#lats and longs
#use the IATA airport code to do so since that is the code used in RITAs dataset
df_DCA = df_DCA.merge(airports, left_on='ORIGIN', right_on='iata').merge(airports, left_on='DEST',right_on='iata')

#next we make sure that all column names are the same 
df_DCA=df_DCA.rename(columns = {'latitude_x':'ORIGIN_lat'})
df_DCA=df_DCA.rename(columns = {'longitude_x':'ORIGIN_long'})

#next we make sure that all column names are the same 
df_DCA = df_DCA.rename(columns = {'latitude_y': 'DEST_lat'})
df_DCA = df_DCA.rename(columns = {'longitude_y': 'DEST_long'})

#write to a csv so that it can be plotted in an r script
#agg.to_csv("aggregate_DC.csv")

##lets merge weather!

# we need to make sure that the time will matchup with the time of the weather data

weather = pd.read_csv("weather_m.csv")
weather.columns = ["station","valid","temp","wind_direct", "wind_speed", "percip","visibility", "Month", "Day", "Time", "HOUR"]
weather = weather[(weather.temp!="M") & (weather.direct != "M") & (weather.wind_speed !="M") & (weather.visibility != "M")]# & (weather.vsby != "M")]
weather = weather.groupby(["station","Month","Day","HOUR"])[["temp","wind_direct","wind_speed", "visibility","percip"]].agg(np.mean)
weather = weather.reset_index()
#weather.vsby = float(weather.vsby)
#weather.to_csv("weather_aggregated.csv")

#weather = weather.groupby(["station","Month","Day","HOUR"])["vsby"].agg(np.mean)


df_DCA["HOUR_ARR"]=(df_DCA["ARR_TIME"]/100.0).round(0)
df_DCA["HOUR_DEP"]=(df_DCA["DEP_TIME"]/100.0).round(0)

df_DCA_w = df_DCA.merge(weather, how = "left",
                        left_on=['DEST','MONTH','DAY_OF_MONTH',"HOUR_DEP"],right_on=["station","Month", "Day", "HOUR"])
#df_DCA_w.columns[-5:-1] =[df_DCA_w.columns[:-6],["DEST_temp", "DEST_wind_direct", "DEST_wind_speed", "DEST_visiblity", "DEST_percip"]] 
df_DCA_w = df_DCA_w.merge(weather, how = "left",
                        left_on=['ORIGIN','MONTH','DAY_OF_MONTH',"HOUR_ARR"],right_on=["station","Month", "Day", "HOUR"])


df_DCA_w=df_DCA_w.rename(columns = {'temp_y':'ORIGIN_temp'})
df_DCA_w=df_DCA_w.rename(columns = {'wind_direct_y':'ORIGIN_wind_direct'})
df_DCA_w=df_DCA_w.rename(columns = {'wind_speed_y':'ORIGIN_wind_speed'})
df_DCA_w=df_DCA_w.rename(columns = {'visibility_y':'ORIGIN_visibility'})
df_DCA_w=df_DCA_w.rename(columns = {'percip_y':'ORIGIN_percip'})
df_DCA_w=df_DCA_w.rename(columns = {'temp_x':'DEST_temp'})
df_DCA_w=df_DCA_w.rename(columns = {'wind_direct_x':'DEST_wind_direct'})
df_DCA_w=df_DCA_w.rename(columns = {'wind_speed_x':'DEST_wind_speed'})
df_DCA_w=df_DCA_w.rename(columns = {'visibility_x':'DEST_visibility'})
df_DCA_w=df_DCA_w.rename(columns = {'percip_x':'DEST_percip'})

df_DCA_w = df_DCA_w.drop(['station_x','Month_x','Day_x', 'HOUR_x','station_y','Month_y','Day_y','HOUR_y'], 1)
df_DCA_w = df_DCA_w.drop(['airport_name_x', 'city_x', 'country_x', 'iata_x', 'icao_x',
                          'airport_name_y', 'city_y', 'country_y', 'iata_y', 'icao_y'],1)
df_DCA_w = df_DCA_w.drop(["CARRIER_DELAY","WEATHER_DELAY","NAS_DELAY","SECURITY_DELAY","LATE_AIRCRAFT_DELAY",
                          "TAXI_OUT", "TAXI_IN", "CANCELLATION_CODE"],1)
#df_DCA_w.to_csv("DCA_data_withweather.csv")


#df_DCA_w[np.isnan(df_DCA_w['CANCELLATION_CODE'])]

##let departure delay be an independent variable

coi = ["CARRIER", "DEP_TIME","AIR_TIME","DISTANCE","ORIGIN_lat","ORIGIN_long", "CANCELLATION_CODE",
       "DEST_lat", "DEST_long","MONTH","DAY_OF_WEEK","DAY_OF_MONTH","HOUR_DEP",
       "HOUR_ARR",'temp_x', 'wind_direct_x', 'wind_speed_x','visibility_x', 'percip_x',
       'temp_y', 'wind_direct_y', 'wind_speed_y','visibility_y', 'percip_y',"ARR_DELAY", "DEP_DELAY"]
coi_2 = ["CARRIER", "DEP_TIME","AIR_TIME","DISTANCE","ORIGIN_lat","ORIGIN_long", "CANCELLATION_CODE",
       "DEST_lat", "DEST_long","MONTH","DAY_OF_WEEK","DAY_OF_MONTH","HOUR_DEP",
       "HOUR_ARR",'temp_x', 'wind_direct_x', 'wind_speed_x','visibility_x', 'percip_x',
       'temp_y', 'wind_direct_y', 'wind_speed_y','visibility_y', 'percip_y', "DEP_DELAY"]       
#df_DCA_w_notcancelled.dropna()
target = ["ARR_DELAY"]

winter = df_DCA_w.dropna() ##3% ofthese flights were cancelled
winter["DELAYED_YN"] = [1 if x>15 else 0 for x in winter.ARR_DELAY]


##create weekend/weekday binary variable
winter["weekend_YN"] = [1 if ((x==1) | (x==7)) else 0 for x in winter.DAY_OF_WEEK]
winter.groupby(winter.weekend_YN).agg({'DELAYED_YN' : [np.size, np.mean]})

##maybe instead of weekend/weekday we should do rush/non-rush

winter["HOUR_OF_WEEK"] = (winter.DAY_OF_WEEK-1)*24 + winter.HOUR_ARR
d= winter[["DAY_OF_WEEK","HOUR_ARR","HOUR_OF_WEEK","DISTANCE", "ARR_DELAY"]]
d = d.dropna()
#t0 = pd.DataFrame(range(169))
t=pd.DataFrame(d.groupby(d.HOUR_OF_WEEK)["HOUR_OF_WEEK"].agg(np.size))
t1 = pd.DataFrame(d.groupby(d.HOUR_OF_WEEK)[["DISTANCE","ARR_DELAY"]].agg(np.mean))
t2 = d[["DAY_OF_WEEK", "HOUR_ARR", "HOUR_OF_WEEK"]][d.HOUR_ARR < 24].drop_duplicates()
t1["size"]=t
t1["HOUR_OF_WEEK"]=pd.DataFrame(range(169))
t1=t1.merge(t2,on="HOUR_OF_WEEK")
d= t1[["size","DAY_OF_WEEK","HOUR_ARR", "DISTANCE"]] #, "ARR_DELAY" "DISTANCE"
#try to put sunday and saturday together
d1 = d
d1.DAY_OF_WEEK = [8 if x == 1 else x for x in d1.DAY_OF_WEEK]
# Create a bunch of different models
from sklearn.cluster import KMeans
k_rng = range(1,15)
est = [KMeans(n_clusters = k).fit(d1) for k in k_rng]
#================================
# Option 1: Silhouette Coefficient
# Generally want SC to be closer to 1, while also minimizing k
from sklearn import metrics
silhouette_score = [metrics.silhouette_score(d1, e.labels_, metric='euclidean') for e in est[1:]]

# Plot the results
#plt.figure(figsize=(7, 8))
#plt.subplot(211)
plt.figure()
plt.title('Using the elbow method to inform k choice')
plt.plot(k_rng[1:], silhouette_score, 'b*-')
plt.xlim([1,15])
plt.grid(True)
plt.ylabel('Silhouette Coefficient')
plt.xlabel("Values of K")
plt.plot(3,silhouette_score[1], 'o', markersize=12, markeredgewidth=1.5,
         markerfacecolor='None', markeredgecolor='r')
###plot three clusters
est = KMeans(n_clusters=3, init='random')
est.fit(d1)
y_kmeans = est.predict(d1)
colors = np.array(['r','b','g'])
plt.figure()
plt.scatter(d1.DAY_OF_WEEK, d1.HOUR_ARR, c=colors[y_kmeans], s=50)
plt.xlim(1.5,8.5)
plt.xticks([2, 3,4,5,6,7,8], ['Mon', 'Tue', 'Wed', "Thu", "Fri", "Sat", "Sun"])
plt.ylim(-.5,24)
plt.yticks([0,6,12,18],["12:00 AM", "6:00 AM", "12:00 PM", "6:00 PM"])
plt.title("Rush Hour Determination from K-Means Clustering")
t2['cluster']= y_kmeans

commuter_hours = t2[t2.cluster==1]["HOUR_OF_WEEK"]

winter["rush"]= [1 if x in set(commuter_hours) else 0 for x in winter.HOUR_OF_WEEK]


winter.DELAYED_YN.hist(by=winter.HOUR_DEP)
#winter.groupby(winter.HOUR_DEP).DELAYED_YN.mean()
winter.groupby(winter.HOUR_DEP).agg({'DELAYED_YN' : [np.size, np.mean]})
plt.scatter(winter.HOUR_DEP,)

winter["northsouth"] = winter.ORIGIN_long - winter.DEST_long
winter["eastwest"] = winter.ORIGIN_lat - winter.DEST_lat
pd.scatter_matrix(winter[["northsouth","eastwest", "DISTANCE", "AIR_TIME", "ARR_DELAY"]])

winter["bearing"]=0

import math

for x in range(len(winter)):
    rlat1 = math.radians(winter.ORIGIN_lat.iloc[x])
    rlat2 = math.radians(winter.DEST_lat.iloc[x])
    rlon1 = math.radians(winter.ORIGIN_long.iloc[x])
    rlon2 = math.radians(winter.DEST_long.iloc[x])
    dlon = math.radians(winter.DEST_long.iloc[x]-winter.ORIGIN_long.iloc[x])
    b = math.atan2(math.sin(dlon)*math.cos(rlat2),math.cos(rlat1)*math.sin(rlat2)-math.sin(rlat1)*math.cos(rlat2)*math.cos(dlon)) # bearing calc
    bd = math.degrees(b)
    br,bn = divmod(bd+360,360) # the bearing remainder and final bearing
    winter.bearing.iloc[x]=bn
    print(x)    

############ 


winter["bearing_buckets"] =(winter.bearing/45).astype(int) # bucket bearing by 45 degrees
#winter.groupby(["bearing_buckets","Direction"]).agg({'DELAYED_YN' : [np.size, np.mean]})
##there might be a confounding factor - in or out of DCA



import random
r = [(random.random() - .5) for _ in range(winter.shape[0])]
winter["ARR_DELAY_Random"] = winter.ARR_DELAY + r

winter.to_csv("winter_months_DCA_12142014.csv")

from sklearn.cross_validation import train_test_split
train, test = train_test_split(winter,test_size=0.3, random_state=1)
train = pd.DataFrame(data=train, columns=winter.columns)
test = pd.DataFrame(data=test, columns=winter.columns)

##bearing, carrier

delay = smf.ols('ARR_DELAY_Random ~ AIR_TIME + vsby + CARRIER + DISTANCE + ORIGIN_lat + ORIGIN_long + DEST_lat + DEST_long', 
                data = train).fit()
delay.summary()

#train["DELAY_YN"] = [1 if x>15 else 0 for x in train.ARR_DELAY]

delay1 = smf.logit('DELAY_YN ~ AIR_TIME + vsby + ', data = train).fit()
delay1.summary()

### you can sub sample your 
X = winter[coi_2]
y = winter["DELAYED_YN"]

from sklearn.neighbors import KNeighborsClassifier  # import class
knn = KNeighborsClassifier(n_neighbors=1)           # instantiate the estimator
knn.fit(X, y)








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
