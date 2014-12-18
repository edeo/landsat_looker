# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 20:28:33 2014

@author: 563572
"""

## read in the csv file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf


winter = pd.read_csv("winter_months_DCA_12142014.csv")

c = ["ARR_TIME","DEP_TIME","AIR_TIME", "DISTANCE", "ARR_DELAY"]
pd.scatter_matrix(winter[c])

plt.figure()
plt.scatter(winter.AIR_TIME,winter.ARR_DELAY)
plt.xlabel('Flight Times in Minutes')
plt.ylabel('Arrival Delay in Minutes')
plt.ylim(-20,600)
plt.xlim(25, 400)

plt.figure()
plt.scatter(winter.DEP_TIME,winter.ARR_DELAY)
plt.xlabel('Daily Departure Time from 0:00 to 23:59')
plt.ylabel('Arrival Delay in Minutes')
plt.xlim(-5,2400)
plt.ylim(-20,600)

plt.figure()
plt.scatter(winter.DISTANCE,winter.ARR_DELAY)
plt.xlabel('Airport to Airport Distances in Miles')
plt.ylabel('Arrival Delay in Minutes')
plt.xlim(0,2500)
plt.ylim(-20,600)



plt.figure()
plt.scatter(winter.ARR_TIME,winter.ARR_DELAY, c='r')
plt.scatter(winter.DEP_TIME,winter.ARR_DELAY, c='b')
plt.xlabel('Daily Departure Time and Arrival Times from 0:00 to 23:59')
plt.ylabel('Arrival Delay in Minutes')
plt.xlim(-5,2400)
plt.ylim(-20,600)



pd.scatter_matrix(winter[["bearing","rush", "weekend_YN", "DELAYED_YN", "ARR_DELAY",
                          "DEST_wind_direct", "DEST_wind_speed", "DEST_visibility", "DEST_percip", "DEST_temp"]])

pd.scatter_matrix(winter[["bearing", "ARR_DELAY",
                          "DEST_wind_direct", "DEST_wind_speed", "DEST_visibility", "DEST_percip", "DEST_temp"]])
#speed, visibility, percip and temp seem to have a relationship with arr_delay
pd.scatter_matrix(winter[["CARRIER","DISTANCE", "DEP_TIME", "ARR_TIME", "AIR_TIME", "timezone_x", "timezone_y"]])
#only include arr_time or dep_time
#air time
pd.scatter_matrix(winter[["ARR_DELAY", "DEP_DELAY"]])

dep_arr = smf.ols('ARR_DELAY ~ DEP_DELAY', data=winter).fit()
dep_arr.summary()

winter.DELAYED_YN.hist(by=winter.CARRIER)
winter.DELAYED_YN.mean()
winter.groupby(winter.CARRIER).agg({'DELAYED_YN' : [np.size, np.mean, lambda x: winter.DELAYED_YN.mean() - np.mean(x)]})#.sort("mean")
##B6 MQ good
##DL AA US bad
###looks like Jet Blue has both the volume and history of delays; same with MQ

winter.DELAYED_YN.hist(by=winter.DAY_OF_WEEK)
winter.groupby(winter.DAY_OF_WEEK).agg({'DELAYED_YN' : [np.size, np.mean,lambda x: winter.DELAYED_YN.mean() - np.mean(x)]})
winter.groupby(winter.weekend_YN).agg({'DELAYED_YN' : [np.size, np.mean]})


winter.DELAYED_YN.hist(by=winter.HOUR_DEP)
winter.DELAYED_YN.hist(by=winter.HOUR_ARR)
#winter.groupby(winter.HOUR_DEP).DELAYED_YN.mean()
winter.groupby(winter.HOUR_DEP).agg({'DELAYED_YN' : [np.size, np.mean]})
plt.scatter(winter.HOUR_DEP,winter.ARR_DELAY)

winter.bearing.hist()
winter.DELAYED_YN.mean()
plt.scatter(winter.bearing, winter.ARR_DELAY)

winter.groupby(winter.bearing_buckets).agg({'DELAYED_YN' : [np.size, np.mean]})
winter.DELAYED_YN.hist(winter.bearing_buckets)

winter.bearing_buckets= winter.bearing_buckets.astype(int)
winter.bearing = winter.bearing.astype(int)
winter.rush = winter.rush.astype(int)
winter.weekend_YN = winter.weekend_YN.astype(int)
winter.HOUR_OF_WEEK = winter.HOUR_OF_WEEK.astype(int)
winter.DELAYED_YN = winter.DELAYED_YN.astype(int)
winter.ORIGIN_percip = winter.ORIGIN_percip.astype(float)
winter.ORIGIN_visibility = winter.ORIGIN_visibility.astype(int)
winter.ORIGIN_wind_speed = winter.ORIGIN_wind_speed.astype(int)
winter.ORIGIN_temp = winter.ORIGIN_temp.astype(int)
winter.ORIGIN_wind_direct = winter.ORIGIN_wind_direct.astype(int)
winter.HOUR_ARR = winter.HOUR_ARR.astype(int)
winter.HOUR_DEP = winter.HOUR_DEP.astype(int)
winter.DEST_percip = winter.DEST_percip.astype(float)
winter.DEST_visibility = winter.DEST_visibility.astype(int)
winter.DEST_wind_speed = winter.DEST_wind_speed.astype(int)
winter.DEST_temp = winter.DEST_temp.astype(int)
winter.DEST_wind_direct = winter.DEST_wind_direct.astype(int)
winter.DISTANCE = winter.DISTANCE.astype(float)
winter.ORIGIN_lat = winter.ORIGIN_lat.astype(float)
winter.ORIGIN_long = winter.ORIGIN_long.astype(float)
winter.DEST_lat = winter.DEST_lat.astype(float)
winter.DSET_long = winter.DEST_long.astype(float)
winter.AIR_TIME = winter.AIR_TIME.astype(float)
winter.timezone_y = winter.timezone_y.astype(int)
winter.timezone_x = winter.timezone_x.astype(int)

winter["JETBLUE"] = [1 if x == "B6" else 0 for x in winter.CARRIER]
winter["ENVOY"] = [1 if x == "MQ" else 0 for x in winter.CARRIER]

winter["AMER"] = [1 if x == "AA" else 0 for x in winter.CARRIER]
winter["USAir"] = [1 if x == "US" else 0 for x in winter.CARRIER]
winter["DELTA"] = [1 if x == "DL" else 0 for x in winter.CARRIER]


winter_hour = winter.groupby(["HOUR_ARR"])["ARR_DELAY"].agg(np.mean)
#winter_agg_1 = winter.groupby()
winter_hour = winter_hour.reset_index()

plt.plot(winter_hour.HOUR_ARR, winter_hour.ARR_DELAY)
plt.xlim(-.5,24)
plt.xticks([0,6,12,18],["12:00 AM", "6:00 AM", "12:00 PM", "6:00 PM"])
plt.ylim(-30,400)
plt.xlabel("Arrival Time")
plt.ylabel("Average Flight Delay")
plt.title("Average Flight Delay (Min) by Arrival Time")


winter["night_hours"] = [1 if (x < 6) | (x> 19) else 0 for x in winter.HOUR_ARR]

from sklearn.cross_validation import train_test_split
train, test = train_test_split(winter,test_size=0.3, random_state=1)
train = pd.DataFrame(data=train, columns=winter.columns)
test = pd.DataFrame(data=test, columns=winter.columns)

train.bearing_buckets= train.bearing_buckets.astype(int)
train.bearing = train.bearing.astype(int)
train.rush = train.rush.astype(int)
train.weekend_YN = train.weekend_YN.astype(int)
train.HOUR_OF_WEEK = train.HOUR_OF_WEEK.astype(int)
train.DELAYED_YN = train.DELAYED_YN.astype(int)
train.ORIGIN_percip = train.ORIGIN_percip.astype(float)
train.ORIGIN_visibility = train.ORIGIN_visibility.astype(float)
train.ORIGIN_wind_speed = train.ORIGIN_wind_speed.astype(float)
train.ORIGIN_temp = train.ORIGIN_temp.astype(float)
train.ORIGIN_wind_direct = train.ORIGIN_wind_direct.astype(float)
train.HOUR_ARR = train.HOUR_ARR.astype(int)
train.HOUR_DEP = train.HOUR_DEP.astype(int)
train.DEST_percip = train.DEST_percip.astype(float)
train.DEST_visibility = train.DEST_visibility.astype(float)
train.DEST_wind_speed = train.DEST_wind_speed.astype(float)
train.DEST_temp = train.DEST_temp.astype(float)
train.DEST_wind_direct = train.DEST_wind_direct.astype(float)
train.DISTANCE = train.DISTANCE.astype(float)
train.ORIGIN_lat = train.ORIGIN_lat.astype(float)
train.ORIGIN_long = train.ORIGIN_long.astype(float)
train.DEST_lat = train.DEST_lat.astype(float)
train.DEST_long = train.DEST_long.astype(float)
train.AIR_TIME = train.AIR_TIME.astype(float)
train.timezone_y = train.timezone_y.astype(int)
train.timezone_x = train.timezone_x.astype(int)
train.JETBLUE = train.JETBLUE.astype(int)
train.ENVOY = train.ENVOY.astype(int)
train.AMER = train.AMER.astype(int)
train.USAir = train.USAir.astype(int)
train.DELTA = train.DELTA.astype(int)
train.DEP_DELAY = train.DEP_DELAY.astype(float)
train.night_hours = train.night_hours.astype(int)
##bearing, carrier

#delay = smf.ols('ARR_DELAY_Random ~ AIR_TIME + DISTANCE + ORIGIN_lat + ORIGIN_long + timezone_x + DEST_lat + DEST_long + timezone_y + HOUR_ARR +'
#                    ' HOUR_DEP + DEST_temp + DEST_wind_direct + DEST_wind_speed + DEST_visibility + DEST_percip '
#                    '+ ORIGIN_temp + ORIGIN_wind_direct + ORIGIN_wind_speed + ORIGIN_visibility + ORIGIN_percip '
#                    ' + HOUR_OF_WEEK + weekend_YN + rush + bearing + C(CARRIER)', data = train).fit()
#delay.summary()


coi = ["DAY_OF_WEEK", "DEP_TIME", "AIR_TIME","DISTANCE", "ORIGIN_lat", "ORIGIN_long", "DEST_lat",
       "DEST_long", "DEST_wind_speed", "DEST_visibility", "DEST_percip", "ORIGIN_temp", "ORIGIN_wind_direct",
       "ORIGIN_wind_speed", "ORIGIN_visibility","ORIGIN_percip", "weekend_YN", "bearing"]
coi2 = ['DEP_DELAY','AIR_TIME','DISTANCE','bearing','weekend_YN','DEST_visibility','ORIGIN_visibility']



#train["DELAY_YN"] = [1 if x>15 else 0 for x in train.ARR_DELAY]
delay2 = smf.logit('DELAYED_YN ~ AIR_TIME + DISTANCE + ORIGIN_lat + ORIGIN_long + timezone_x + DEST_lat + DEST_long + timezone_y + HOUR_ARR +'
                    ' HOUR_DEP + DEST_temp + DEST_wind_direct + DEST_wind_speed + DEST_visibility + DEST_percip '
                    '+ ORIGIN_temp + ORIGIN_wind_direct + ORIGIN_wind_speed + ORIGIN_visibility + ORIGIN_percip '
                    ' + HOUR_OF_WEEK + weekend_YN + rush + bearing + C(CARRIER)', data = train).fit()
delay2.summary()
## R^2 is .15

delay1 = smf.logit('DELAYED_YN ~  AIR_TIME + DISTANCE + ORIGIN_lat + ORIGIN_long + DEST_long  + HOUR_ARR +'#+  DEST_lat +
                    ' HOUR_DEP + DEST_temp + DEST_wind_direct + DEST_wind_speed + DEST_visibility + '# DEST_percip +timezone_x + bearing  + rush + HOUR_OF_WEEK +'
                    '+ ORIGIN_temp + ORIGIN_wind_direct + ORIGIN_wind_speed + ORIGIN_visibility + '# ORIGIN_percip + timezone_y' 
                    ' +  weekend_YN  + JETBLUE + ENVOY + AMER + USAir + DELTA', data = train).fit()
delay1.summary()

# R^2 is .1463
#get rid of DEST_percip
#get rid of rush
#get rid of HOUR_OF_WEEK 
#get rid of bearing
#.1461
#get rid of timezone_x
#.1460
#ORIGIN_percip 
#.1458
#timezone_y 
#DEST_lat
#.1451 

# FYI: you can use AUC as your scoring parameter with sklearn
from sklearn.cross_validation import cross_val_score
from sklearn.grid_search import GridSearchCV
from sklearn.linear_model import LogisticRegression

X = winter[coi]
y = winter.DELAYED_YN

scores = cross_val_score(LogisticRegression(), X, y, cv=5, scoring='roc_auc')
scores.mean()
#grid = GridSearchCV(LogisticRegression(), param_grid, cv=5, scoring='roc_auc')
X_2 = winter[coi2]
scores = cross_val_score(LogisticRegression(), X_2, y, cv=5, scoring='roc_auc')
scores.mean()



delay2 = smf.logit('DELAYED_YN ~ DEP_DELAY + AIR_TIME +DISTANCE + bearing + weekend_YN '#+ night_hour '
                    '+ DEST_visibility + ORIGIN_visibility' ,data = train).fit()
delay2.summary()


#replace HOUR_ARR with HOUR_DEP 
## R^2 is .5652 instead of .5648
#bearing .5737
#rush doesnt add anything
#weekendYN is slightly better
#distance and air time are both significant i thought only would be
#got rid of HOUR_DEP
#added night hour doesnt seem to add much either

test.DEP_DELAY = test.DEP_DELAY.astype(float)
test.AIR_TIME = test.AIR_TIME.astype(float)
test.DISTANCE = test.DISTANCE.astype(float)
test.bearing = test.bearing.astype(float)
test.weekend_YN = test.weekend_YN.astype(int)
test.DEST_visibility = test.DEST_visibility.astype(float)
test.ORIGIN_visibility = test.ORIGIN_visibility.astype(float)
test.DELAYED_YN = test.DELAYED_YN.astype(int)

#Create predictions using the balance model on the test set
test['pred'] = delay2.predict(test)
test['pred_class']= np.where(test['pred'] >= 0.5, 1, 0)
test['pred_class75']=np.where(test['pred'] >= 0.75, 1, 0)
test['pred_class25']=np.where(test['pred'] >= 0.25, 1, 0)

#Compute the overall accuracy, the sensitivity and specificity
# Accuracy
accuracy = sum(test.pred_class == test.DELAYED_YN) / float(len(test.DELAYED_YN))
accuracy75 = sum(test.pred_class75 == test.DELAYED_YN) / float(len(test.DELAYED_YN))
accuracy25 = sum(test.pred_class25 == test.DELAYED_YN) / float(len(test.DELAYED_YN))

# Specificity
# For those who didn't default, how many did it predict correctly?
test_nd = test[test.DELAYED_YN == 0]
specificity = sum(test_nd.pred_class == test_nd.DELAYED_YN) / float(len(test_nd.DELAYED_YN))
specificity75 = sum(test_nd.pred_class75 == test_nd.DELAYED_YN) / float(len(test_nd.DELAYED_YN))
specificity25 = sum(test_nd.pred_class25 == test_nd.DELAYED_YN) / float(len(test_nd.DELAYED_YN))


# Sensitivity
# For those who did default, how many did it predict correctly? 
test_d = test[test.DELAYED_YN == 1]
sensitivity = sum(test_d.pred_class == test_d.DELAYED_YN) / float(len(test_d.DELAYED_YN))
sensitivity75 = sum(test_d.pred_class75 == test_d.DELAYED_YN) / float(len(test_d.DELAYED_YN))
sensitivity25 = sum(test_d.pred_class25 == test_d.DELAYED_YN) / float(len(test_d.DELAYED_YN))


null = 1 - sum(winter.DELAYED_YN) / float(len(winter.DELAYED_YN))

# generate metrics
from sklearn import metrics
print metrics.accuracy_score(test.DELAYED_YN, test.pred_class)
print metrics.confusion_matrix(test.DELAYED_YN, test.pred_class)
print metrics.roc_auc_score(test.DELAYED_YN, test.pred)

# plot ROC curve
fpr, tpr, thresholds = metrics.roc_curve(test.DELAYED_YN, test.pred)
plt.figure()
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title("Logistic Regression Model ROC-AUC Plot")
plt.plot(1-specificity, sensitivity, 'o', markersize=12, markeredgewidth=1.5,
         markerfacecolor='None', markeredgecolor='r')
plt.text(1-specificity + .05 , sensitivity - .05, '50% Threshold')

plt.plot(1-specificity75, sensitivity75, 'o', markersize=12, markeredgewidth=1.5,
         markerfacecolor='None', markeredgecolor='g')
plt.text(1-specificity75 + .05 , sensitivity75 - .05, '75% Threshold')
plt.plot(1-specificity25, sensitivity25, 'o', markersize=12, markeredgewidth=1.5,
         markerfacecolor='None', markeredgecolor='k')
plt.text(1-specificity25 + .05 , sensitivity25 - .05, '25% Threshold')






X_train = train[coi] 
y_train = [-1 if x < 0 else 0 for x in train.ARR_DELAY]#train.DELAYED_YN
y_train = np.where(train.ARR_DELAY > 15, 1, y_train)
y_train = pd.DataFrame(y_train)
y_train_b = train.ARR_DELAY
y_train_b[y_train_b < -60] = -60
y_train_b[y_train_b > 180] = 180
y_train_b_2 = ((y_train_b)/15).astype(int)
y_train_b_3 = ((y_train_b)/10).astype(int)
plt.plot(np.arange(-45,13*15,15),y_train_b_2.groupby(y_train_b_2).agg(np.size))
plt.plot(np.arange(-5*10,19*10, 10),y_train_b_3.groupby(y_train_b_3).agg(np.size))

#y1[y1<0]=0 
## or other buckets
X_train_2 = train[coi2]

## we're trying to create buckets or arrival delay
np.histogram(train.ARR_DELAY, bins=np.arange(-60,120,15))

from sklearn.neighbors import KNeighborsClassifier  # import class
for i in range(3,15):
    knn = KNeighborsClassifier(n_neighbors=i)           # instantiate the estimator
    knn.fit(X_train, y_train)
    knn.score(X_train, y_train)
    print i ,' neighbhors has an assuracy of ', knn.score(X_train, y_train)

##
## CROSS-VALIDATION

from sklearn.cross_validation import cross_val_score
from sklearn.grid_search import GridSearchCV

winter_knn = winter[coi]
winter_knn_y = winter.DELAYED_YN


# check CV score for K=1
# automatic grid search for an optimal value of K
knn = KNeighborsClassifier()
k_range = range(1, 50)
param_grid = dict(n_neighbors=k_range)
grid = GridSearchCV(knn, param_grid, cv=5, scoring='accuracy')
grid.fit(winter_knn, winter_knn_y)
# check the results of the grid search
#grid.grid_scores_
grid2 = GridSearchCV(knn, param_grid, cv=5, scoring='roc_auc')
grid2.fit(winter_knn, winter_knn_y)

grid_mean_scores = [result[1] for result in grid.grid_scores_]
grid_mean_scores_2 = [result[1] for result in grid2.grid_scores_]
plt.figure()
plt.plot(k_range, grid_mean_scores)
plt.figure()
plt.plot(k_range, grid_mean_scores_2)
grid.best_score_
grid.best_params_
grid.best_estimator_

grid2.best_score_
grid2.best_params_
grid2.best_estimator_
## says that three neighborhoods is best
knn = KNeighborsClassifier(n_neighbors=3)           # instantiate the estimator
knn.fit(winter_knn, winter_knn_y)
knn.score(winter_knn, winter_knn_y)
## 87% accuracy


from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(winter_knn, winter_knn_y)
logreg.score(winter_knn, winter_knn_y)
#79% accuracy

from sklearn import tree
clf = tree.DecisionTreeClassifier(max_depth=5)
clf.fit(X,y)

features = X.columns.values
with open("delays.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f, feature_names=features, close=True)

# How to interpret the diagram?
clf.classes_ # 
imp = pd.DataFrame(clf.feature_importances_.reshape(1,18), columns=features)
preds_train = clf.predict(X)
preds = clf.predict(X_new)

# Calculate accuracy
metrics.accuracy_score(y, preds_train)
metrics.accuracy_score(y_new, preds)

# Confusion matrix
pd.crosstab(test[:,0], preds, rownames=['actual'], colnames=['predicted'])

# Make predictions on the test set using predict_proba
probs = clf.predict_proba(test[:,1:])[:,1]

# Calculate the AUC metric
metrics.roc_auc_score(test[:,0], probs)

