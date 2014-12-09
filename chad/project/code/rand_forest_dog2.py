# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 12:20:17 2014

@author: chadleonard
"""
##########################################################################
# rand_forest_dog2.py
# script to execute randoem forest against the data
#
#
# Author:   Chad Leonard
# Created:  December 7, 2014
#
##########################################################################

import patient as pat
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn.grid_search import GridSearchCV
import traceback




if __name__ == '__main__':
    path = '/Users/chadleonard/Repos/DAT3_project/data/'
    dg_name = 'Dog_2'
    dog = pat.Patient(dg_name, path)
#    df = pd.read_csv(dog_1.patpath + 'crossval_dir/all_test_files.csv_24_30')
    df = pd.read_csv(dog.patpath + 'mat_dir.csv_24_30')
    print dog.name
    
    X_cols = ['NVC0905_22_002_Ecog_c001_f1',
    'NVC0905_22_002_Ecog_c001_f4',
    'NVC0905_22_002_Ecog_c001_f5',
    'NVC0905_22_002_Ecog_c001_f9',
    'NVC0905_22_002_Ecog_c001_f12',
    'NVC0905_22_002_Ecog_c001_f14',
    'NVC0905_22_002_Ecog_c001_f17',
    'NVC0905_22_002_Ecog_c002_f1',
    'NVC0905_22_002_Ecog_c002_f3',
    'NVC0905_22_002_Ecog_c002_f9',
    'NVC0905_22_002_Ecog_c002_f11',
    'NVC0905_22_002_Ecog_c002_f12',
    'NVC0905_22_002_Ecog_c002_f16',
    'NVC0905_22_002_Ecog_c002_f17',
    'NVC0905_22_002_Ecog_c002_f20',
    'NVC0905_22_002_Ecog_c003_f1',
    'NVC0905_22_002_Ecog_c003_f24',
    'NVC0905_22_002_Ecog_c004_f1',
    'NVC0905_22_002_Ecog_c004_f2',
    'NVC0905_22_002_Ecog_c004_f10',
    'NVC0905_22_002_Ecog_c004_f17',
    'NVC0905_22_002_Ecog_c004_f19',
    'NVC0905_22_002_Ecog_c005_f2',
    'NVC0905_22_002_Ecog_c005_f3',
    'NVC0905_22_002_Ecog_c005_f7',
    'NVC0905_22_002_Ecog_c005_f8',
    'NVC0905_22_002_Ecog_c005_f10',
    'NVC0905_22_002_Ecog_c005_f11',
    'NVC0905_22_002_Ecog_c005_f14',
    'NVC0905_22_002_Ecog_c005_f16',
    'NVC0905_22_002_Ecog_c005_f17',
    'NVC0905_22_002_Ecog_c006_f2',
    'NVC0905_22_002_Ecog_c006_f3',
    'NVC0905_22_002_Ecog_c006_f14',
    'NVC0905_22_002_Ecog_c006_f17',
    'NVC0905_22_002_Ecog_c007_f2',
    'NVC0905_22_002_Ecog_c007_f3',
    'NVC0905_22_002_Ecog_c007_f8',
    'NVC0905_22_002_Ecog_c007_f14',
    'NVC0905_22_002_Ecog_c007_f16',
    'NVC0905_22_002_Ecog_c007_f17',
    'NVC0905_22_002_Ecog_c007_f18',
    'NVC0905_22_002_Ecog_c007_f19',
    'NVC0905_22_002_Ecog_c007_f21',
    'NVC0905_22_002_Ecog_c008_f1',
    'NVC0905_22_002_Ecog_c008_f3',
    'NVC0905_22_002_Ecog_c008_f4',
    'NVC0905_22_002_Ecog_c008_f16',
    'NVC0905_22_002_Ecog_c008_f18',
    'NVC0905_22_002_Ecog_c008_f21',
    'NVC0905_22_002_Ecog_c008_f22',
    'NVC0905_22_002_Ecog_c009_f1',
    'NVC0905_22_002_Ecog_c009_f8',
    'NVC0905_22_002_Ecog_c010_f1',
    'NVC0905_22_002_Ecog_c010_f4',
    'NVC0905_22_002_Ecog_c010_f8',
    'NVC0905_22_002_Ecog_c010_f14',
    'NVC0905_22_002_Ecog_c010_f20',
    'NVC0905_22_002_Ecog_c011_f3',
    'NVC0905_22_002_Ecog_c011_f10',
    'NVC0905_22_002_Ecog_c012_f5',
    'NVC0905_22_002_Ecog_c012_f7',
    'NVC0905_22_002_Ecog_c012_f10',
    'NVC0905_22_002_Ecog_c012_f11',
    'NVC0905_22_002_Ecog_c012_f15',
    'NVC0905_22_002_Ecog_c012_f16',
    'NVC0905_22_002_Ecog_c012_f17',
    'NVC0905_22_002_Ecog_c012_f21',
    'NVC0905_22_002_Ecog_c012_f23',
    'NVC0905_22_002_Ecog_c013_f1',
    'NVC0905_22_002_Ecog_c013_f2',
    'NVC0905_22_002_Ecog_c013_f24',
    'NVC0905_22_002_Ecog_c014_f1',
    'NVC0905_22_002_Ecog_c014_f4',
    'NVC0905_22_002_Ecog_c014_f5',
    'NVC0905_22_002_Ecog_c014_f8',
    'NVC0905_22_002_Ecog_c014_f9',
    'NVC0905_22_002_Ecog_c014_f14',
    'NVC0905_22_002_Ecog_c014_f15',
    'NVC0905_22_002_Ecog_c014_f16',
    'NVC0905_22_002_Ecog_c015_f1',
    'NVC0905_22_002_Ecog_c015_f2',
    'NVC0905_22_002_Ecog_c015_f8',
    'NVC0905_22_002_Ecog_c015_f9',
    'NVC0905_22_002_Ecog_c016_f1',
    'NVC0905_22_002_Ecog_c016_f4',
    'NVC0905_22_002_Ecog_c016_f13',
    'NVC0905_22_002_Ecog_c016_f16',
    'NVC0905_22_002_Ecog_c016_f17',
    'NVC0905_22_002_Ecog_c016_f21',
    'NVC0905_22_002_Ecog_c016_f23']
    X_train, X_test, y_train, y_test = train_test_split(df[X_cols], 
                               df['ictal_ind'],test_size=0.3, random_state=1)   
    rf = RandomForestClassifier(random_state=1)
    rf.fit(X_train, y_train)
    probs = rf.predict_proba(X_test)[:,1]
    print metrics.roc_auc_score(y_test, probs)
    print probs
    
    list_estimators = list(xrange(1, 30, 2)) + list(xrange(30, 101, 10))
    param_grid = dict(n_estimators=list_estimators)
    grid = GridSearchCV(rf, param_grid, cv=5, scoring='roc_auc')
    grid.fit(df[X_cols], df['ictal_ind'])
    
    # Plot the results of the grid search
    grid_mean_scores = [result[1] for result in grid.grid_scores_]
    plt.xlim([0,100])
    plt.scatter(list_estimators, grid_mean_scores, s=40)
    plt.grid(True)
    plt.title('Tuning Random Forests for Dog 2')
    plt.ylabel('AUC for 5-fold CV')
    plt.xlabel('Number of Trees')



