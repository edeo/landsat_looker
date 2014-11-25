import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt

jan = pd.read_csv('January_2014.csv')
dec = pd.read_csv('December_2013.csv')
nov = pd.read_csv('November_2013.csv')

### try regressing or KNN classification over the following variables

jan.columns.get_values

## aggregate time to hourly buckets
jan["HOUR"] = (jan["ARR_TIME"]/100.0).round(0)
dec["HOUR"] = (dec["ARR_TIME"]/100.0).round(0)
nov["HOUR"] = (nov["ARR_TIME"]/100.0).round(0)


#columns of interest
coi = ["CARRIER","ORIGIN","DEST","HOUR","CANCELLED","AIR_TIME","ARR_DEL15","ARR_DELAY"] #"MONTH","DAY_OF_WEEK",
coi_pred = ["CARRIER","ORIGIN","DEST","HOUR"] #"MONTH","DAY_OF_WEEK",
target = ["ARR_DEL15","ARR_DELAY","CANCELLED","AIR_TIME"]

jan = jan[coi]
dec = dec[coi]
nov = nov[coi]

winter = jan.append(dec)
winter = winter.append(nov)
winter1 = winter.groupby(coi_pred)[target].agg([np.mean])#, np.count_nonzero])
winter2 = winter.groupby(coi_pred)["ARR_DELAY"].agg(np.count_nonzero)
winter1["FREQ"] = winter2
winter2 = None
winter = winter1
winter1 = None
##add in counts later
jan = None
dec = None
nov = None
winter = winter.reset_index()

winter["AVG_DELAY"]=[1 if x>15 else 0 for x in winter.ARR_DELAY]

winter_agg = winter.groupby(["CARRIER","HOUR"])["ARR_DELAY"].agg(np.mean)
#winter_agg_1 = winter.groupby()
winter_agg = winter_agg.reset_index()

colormap = plt.cm.gist_ncar
plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9, 13)])
labels = []
pd.unique(winter.CARRIER.values.ravel())
t = pd.DataFrame(winter.groupby("CARRIER")["FREQ"].agg(np.sum)).sort("FREQ",ascending=False)
t = t.reset_index()
carrier_oi = t.CARRIER[range(10)]#['US','AA','DL','MQ','B6','UA','WN']
for i in carrier_oi:
    plt.plot(winter_agg[winter_agg.CARRIER==i].HOUR, winter_agg[winter_agg.CARRIER==i].ARR_DELAY)
    labels.append(i)

plt.legend(labels, ncol=4, loc='upper center', 
           bbox_to_anchor=[0.5, 1.1], 
           columnspacing=1.0, labelspacing=0.0,
           handletextpad=0.0, handlelength=1.5,
           fancybox=True, shadow=True)

plt.show()

sub = winter[(winter.HOUR < 6)]
AIRPORT_COLS = ('airport_name', 'city', 'country', 'iata', 'icao', 'latitude', 'longitude', 'altitude', 'timezone', 'dst', 't')
airports = pd.read_csv('airports.dat', header=None, names=AIRPORT_COLS)
sub = sub.merge(airports, left_on='ORIGIN', right_on='iata').merge(airports, left_on='DEST',right_on='iata')

time_zones = sub[sub.ARR_DELAY>100].groupby(["t_x","t_y"])["FREQ"].agg(np.count_nonzero)
time_zones = time_zones.reset_index()
## i thought the worst offenders would be cross-contientail but it seems that most flights

x = pd.DataFrame(sub.groupby(["CARRIER", "HOUR"])["ARR_DELAY"].agg([np.mean, np.count_nonzero])).sort("mean",ascending=False)
##top offender is F9 - Frontier, Virigin, JetBlue, Delta, southwest, envoy
sub.to_csv("night_loop.csv")


#train, test = train_test_split(winter,test_size=0.3, random_state=1)
#train = pd.DataFrame(data=train, columns=winter.columns)
#test = pd.DataFrame(data=test, columns=winter.columns)

#train.plot(x='HOUR', y='AIR_TIME', kind='scatter', alpha=0.3)
#delay = smf.logit('AVG_DELAY ~ HOUR', data = train.head(100)).fit()
#delay.summary



