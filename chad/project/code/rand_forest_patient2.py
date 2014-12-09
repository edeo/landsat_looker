# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 12:20:17 2014

@author: chadleonard
"""
##########################################################################
# rand_forest_patient2.py
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
    dg_name = 'Patient_2'
    dog = pat.Patient(dg_name, path)
#    df = pd.read_csv(dog_1.patpath + 'crossval_dir/all_test_files.csv_24_30')
    df = pd.read_csv(dog.patpath + 'mat_dir.csv_24_30')
    print dog.name
    
    X_cols = ['LTG_01_f1',
    'LTG_01_f3',
    'LTG_01_f4',
    'LTG_01_f8',
    'LTG_01_f14',
    'LTG_01_f16',
    'LTG_01_f21',
    'LTG_02_f1',
    'LTG_02_f2',
    'LTG_02_f8',
    'LTG_02_f9',
    'LTG_02_f10',
    'LTG_02_f20',
    'LTG_02_f21',
    'LTG_02_f24',
    'LTG_03_f11',
    'LTG_03_f19',
    'LTG_04_f10',
    'LTG_04_f24',
    'LTG_05_f10',
    'LTG_06_f3',
    'LTG_06_f6',
    'LTG_06_f10',
    'LTG_06_f17',
    'LTG_06_f19',
    'LTG_06_f20',
    'LTG_07_f1',
    'LTG_07_f2',
    'LTG_07_f3',
    'LTG_07_f10',
    'LTG_07_f14',
    'LTG_08_f1',
    'LTG_08_f3',
    'LTG_08_f4',
    'LTG_08_f11',
    'LTG_08_f12',
    'LTG_09_f1',
    'LTG_09_f10',
    'LTG_09_f16',
    'LTG_10_f1',
    'LTG_10_f10',
    'LTG_10_f16',
    'LTG_11_f21',
    'LTG_12_f2',
    'LTG_12_f10',
    'LTG_12_f13',
    'LTG_12_f16',
    'LTG_13_f1',
    'LTG_13_f4',
    'LTG_13_f8',
    'LTG_14_f3',
    'LTG_14_f4',
    'LTG_14_f6',
    'LTG_14_f17',
    'LTG_15_f1',
    'LTG_15_f2',
    'LTG_15_f3',
    'LTG_15_f10',
    'LTG_15_f11',
    'LTG_16_f3',
    'LTG_16_f4',
    'LTG_16_f11',
    'LTG_16_f12',
    'LTG_17_f1',
    'LTG_17_f3',
    'LTG_17_f4',
    'LTG_17_f10',
    'LTG_17_f14',
    'LTG_17_f16',
    'LTG_17_f17',
    'LTG_18_f1',
    'LTG_18_f3',
    'LTG_18_f4',
    'LTG_18_f10',
    'LTG_18_f16',
    'LTG_19_f1',
    'LTG_19_f4',
    'LTG_19_f8',
    'LTG_19_f20',
    'LTG_20_f10',
    'LTG_20_f12',
    'LTG_20_f15',
    'LTG_21_f3',
    'LTG_21_f4',
    'LTG_21_f10',
    'LTG_21_f14',
    'LTG_22_f3',
    'LTG_22_f4',
    'LTG_22_f10',
    'LTG_23_f4',
    'LTG_23_f10',
    'LTG_23_f11',
    'LTG_24_f1',
    'LTG_24_f4',
    'LTG_24_f11']
    
    X_train, X_test, y_train, y_test = train_test_split(df[X_cols], 
                               df['ictal_ind'],test_size=0.3, random_state=1)   
    rf = RandomForestClassifier(random_state=1)
    rf.fit(X_train, y_train)
    probs = rf.predict_proba(X_test)[:,1]
    print metrics.roc_auc_score(y_test, probs)
    print probs


