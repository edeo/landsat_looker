# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 12:20:17 2014

@author: chadleonard
"""
##########################################################################
# rand_forest_dog5.py
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
    dg_name = 'Dog_5'
    dog = pat.Patient(dg_name, path)
#    df = pd.read_csv(dog_1.patpath + 'crossval_dir/all_test_files.csv_24_30')
    df = pd.read_csv(dog.patpath + 'mat_dir.csv_24_30')
    print dog.name
    
    X_cols = ['NVC0905_22_004_Ecog_c001_f8',
    'NVC0905_22_004_Ecog_c002_f1',
    'NVC0905_22_004_Ecog_c002_f2',
    'NVC0905_22_004_Ecog_c002_f6',
    'NVC0905_22_004_Ecog_c002_f16',
    'NVC0905_22_004_Ecog_c003_f8',
    'NVC0905_22_004_Ecog_c003_f19',
    'NVC0905_22_004_Ecog_c005_f2',
    'NVC0905_22_004_Ecog_c005_f3',
    'NVC0905_22_004_Ecog_c005_f7',
    'NVC0905_22_004_Ecog_c005_f9',
    'NVC0905_22_004_Ecog_c005_f13',
    'NVC0905_22_004_Ecog_c005_f17',
    'NVC0905_22_004_Ecog_c006_f1',
    'NVC0905_22_004_Ecog_c006_f19',
    'NVC0905_22_004_Ecog_c007_f1',
    'NVC0905_22_004_Ecog_c007_f8',
    'NVC0905_22_004_Ecog_c007_f16',
    'NVC0905_22_004_Ecog_c007_f18',
    'NVC0905_22_004_Ecog_c008_f1',
    'NVC0905_22_004_Ecog_c008_f2',
    'NVC0905_22_004_Ecog_c008_f6',
    'NVC0905_22_004_Ecog_c008_f7',
    'NVC0905_22_004_Ecog_c008_f8',
    'NVC0905_22_004_Ecog_c008_f11',
    'NVC0905_22_004_Ecog_c008_f13',
    'NVC0905_22_004_Ecog_c009_f2',
    'NVC0905_22_004_Ecog_c009_f24',
    'NVC0905_22_004_Ecog_c010_f1',
    'NVC0905_22_004_Ecog_c010_f4',
    'NVC0905_22_004_Ecog_c010_f5',
    'NVC0905_22_004_Ecog_c010_f16',
    'NVC0905_22_004_Ecog_c011_f1',
    'NVC0905_22_004_Ecog_c011_f7',
    'NVC0905_22_004_Ecog_c011_f15',
    'NVC0905_22_004_Ecog_c011_f16',
    'NVC0905_22_004_Ecog_c013_f3',
    'NVC0905_22_004_Ecog_c013_f8',
    'NVC0905_22_004_Ecog_c013_f11',
    'NVC0905_22_004_Ecog_c013_f18',
    'NVC0905_22_004_Ecog_c014_f12',
    'NVC0905_22_004_Ecog_c014_f17',
    'NVC0905_22_004_Ecog_c014_f24',
    'NVC0905_22_004_Ecog_c015_f1',
    'NVC0905_22_004_Ecog_c015_f2',
    'NVC0905_22_004_Ecog_c016_f2',
    'NVC0905_22_004_Ecog_c016_f8',
    'NVC0905_22_004_Ecog_c016_f14',
    'NVC0905_22_004_Ecog_c016_f15']
    
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
    plt.title('Tuning Random Forests for Dog 5')
    plt.ylabel('AUC for 5-fold CV')
    plt.xlabel('Number of Trees')


