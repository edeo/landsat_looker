# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 12:20:17 2014

@author: chadleonard
"""
##########################################################################
# rand_forest_patient1.py
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




if __name__ == '__main__':
    path = '/Users/chadleonard/Repos/DAT3_project/data/'
    dg_name = 'Patient_1'
    dog = pat.Patient(dg_name, path)
#    df = pd.read_csv(dog_1.patpath + 'crossval_dir/all_test_files.csv_24_30')
    df = pd.read_csv(dog.patpath + 'mat_dir.csv_24_30')
    print dog.name
    
    X_cols = ['LD_1_f18',
    'LD_3_f18',
    'LD_4_f1',
    'LD_4_f2',
    'LD_4_f4',
    'LD_4_f6',
    'LD_4_f8',
    'LD_7_f2',
    'LD_7_f4']
    
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
    plt.title('Tuning Random Forests for Patient 1')
    plt.ylabel('AUC for 5-fold CV')
    plt.xlabel('Number of Trees')


