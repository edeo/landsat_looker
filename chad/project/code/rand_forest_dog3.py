# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 12:20:17 2014

@author: chadleonard
"""
##########################################################################
# rand_forest_dog3.py
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
    dg_name = 'Dog_3'
    dog = pat.Patient(dg_name, path)
#    df = pd.read_csv(dog_1.patpath + 'crossval_dir/all_test_files.csv_24_30')
    df = pd.read_csv(dog.patpath + 'mat_dir.csv_24_30')
    print dog.name
    
    X_cols = ['NVC0906_22_007_Ecog_c001_f2',
    'NVC0906_22_007_Ecog_c001_f15',
    'NVC0906_22_007_Ecog_c001_f18',
    'NVC0906_22_007_Ecog_c001_f23',
    'NVC0906_22_007_Ecog_c001_f24',
    'NVC0906_22_007_Ecog_c002_f1',
    'NVC0906_22_007_Ecog_c002_f8',
    'NVC0906_22_007_Ecog_c002_f18',
    'NVC0906_22_007_Ecog_c002_f24',
    'NVC0906_22_007_Ecog_c003_f1',
    'NVC0906_22_007_Ecog_c003_f7',
    'NVC0906_22_007_Ecog_c003_f8',
    'NVC0906_22_007_Ecog_c003_f10',
    'NVC0906_22_007_Ecog_c003_f12',
    'NVC0906_22_007_Ecog_c003_f14',
    'NVC0906_22_007_Ecog_c003_f17',
    'NVC0906_22_007_Ecog_c003_f24',
    'NVC0906_22_007_Ecog_c004_f1',
    'NVC0906_22_007_Ecog_c004_f2',
    'NVC0906_22_007_Ecog_c004_f3',
    'NVC0906_22_007_Ecog_c004_f10',
    'NVC0906_22_007_Ecog_c004_f11',
    'NVC0906_22_007_Ecog_c004_f12',
    'NVC0906_22_007_Ecog_c004_f14',
    'NVC0906_22_007_Ecog_c004_f18',
    'NVC0906_22_007_Ecog_c004_f23',
    'NVC0906_22_007_Ecog_c004_f24',
    'NVC0906_22_007_Ecog_c005_f1',
    'NVC0906_22_007_Ecog_c005_f8',
    'NVC0906_22_007_Ecog_c005_f10',
    'NVC0906_22_007_Ecog_c005_f12',
    'NVC0906_22_007_Ecog_c005_f16',
    'NVC0906_22_007_Ecog_c005_f17',
    'NVC0906_22_007_Ecog_c005_f20',
    'NVC0906_22_007_Ecog_c005_f24',
    'NVC0906_22_007_Ecog_c006_f1',
    'NVC0906_22_007_Ecog_c006_f2',
    'NVC0906_22_007_Ecog_c006_f4',
    'NVC0906_22_007_Ecog_c006_f8',
    'NVC0906_22_007_Ecog_c006_f12',
    'NVC0906_22_007_Ecog_c006_f17',
    'NVC0906_22_007_Ecog_c006_f18',
    'NVC0906_22_007_Ecog_c006_f23',
    'NVC0906_22_007_Ecog_c006_f24',
    'NVC0906_22_007_Ecog_c007_f1',
    'NVC0906_22_007_Ecog_c007_f9',
    'NVC0906_22_007_Ecog_c007_f21',
    'NVC0906_22_007_Ecog_c007_f23',
    'NVC0906_22_007_Ecog_c007_f24',
    'NVC0906_22_007_Ecog_c008_f5',
    'NVC0906_22_007_Ecog_c008_f7',
    'NVC0906_22_007_Ecog_c008_f8',
    'NVC0906_22_007_Ecog_c008_f24',
    'NVC0906_22_007_Ecog_c009_f9',
    'NVC0906_22_007_Ecog_c009_f12',
    'NVC0906_22_007_Ecog_c009_f15',
    'NVC0906_22_007_Ecog_c009_f17',
    'NVC0906_22_007_Ecog_c009_f20',
    'NVC0906_22_007_Ecog_c009_f22',
    'NVC0906_22_007_Ecog_c009_f23',
    'NVC0906_22_007_Ecog_c009_f24',
    'NVC0906_22_007_Ecog_c010_f1',
    'NVC0906_22_007_Ecog_c010_f2',
    'NVC0906_22_007_Ecog_c010_f7',
    'NVC0906_22_007_Ecog_c010_f8',
    'NVC0906_22_007_Ecog_c010_f17',
    'NVC0906_22_007_Ecog_c010_f24',
    'NVC0906_22_007_Ecog_c011_f1',
    'NVC0906_22_007_Ecog_c011_f2',
    'NVC0906_22_007_Ecog_c011_f6',
    'NVC0906_22_007_Ecog_c011_f8',
    'NVC0906_22_007_Ecog_c011_f13',
    'NVC0906_22_007_Ecog_c011_f17',
    'NVC0906_22_007_Ecog_c011_f19',
    'NVC0906_22_007_Ecog_c011_f24',
    'NVC0906_22_007_Ecog_c012_f1',
    'NVC0906_22_007_Ecog_c012_f2',
    'NVC0906_22_007_Ecog_c012_f3',
    'NVC0906_22_007_Ecog_c012_f5',
    'NVC0906_22_007_Ecog_c012_f8',
    'NVC0906_22_007_Ecog_c012_f12',
    'NVC0906_22_007_Ecog_c012_f19',
    'NVC0906_22_007_Ecog_c012_f24',
    'NVC0906_22_007_Ecog_c013_f1',
    'NVC0906_22_007_Ecog_c013_f8',
    'NVC0906_22_007_Ecog_c013_f15',
    'NVC0906_22_007_Ecog_c013_f19',
    'NVC0906_22_007_Ecog_c013_f24',
    'NVC0906_22_007_Ecog_c014_f1',
    'NVC0906_22_007_Ecog_c014_f3',
    'NVC0906_22_007_Ecog_c014_f4',
    'NVC0906_22_007_Ecog_c014_f8',
    'NVC0906_22_007_Ecog_c014_f10',
    'NVC0906_22_007_Ecog_c014_f13',
    'NVC0906_22_007_Ecog_c014_f18',
    'NVC0906_22_007_Ecog_c014_f24',
    'NVC0906_22_007_Ecog_c015_f1',
    'NVC0906_22_007_Ecog_c015_f2',
    'NVC0906_22_007_Ecog_c015_f5',
    'NVC0906_22_007_Ecog_c015_f8',
    'NVC0906_22_007_Ecog_c015_f9',
    'NVC0906_22_007_Ecog_c015_f10',
    'NVC0906_22_007_Ecog_c015_f11',
    'NVC0906_22_007_Ecog_c015_f24',
    'NVC0906_22_007_Ecog_c016_f3',
    'NVC0906_22_007_Ecog_c016_f9',
    'NVC0906_22_007_Ecog_c016_f10',
    'NVC0906_22_007_Ecog_c016_f12',
    'NVC0906_22_007_Ecog_c016_f16',
    'NVC0906_22_007_Ecog_c016_f24']
    
    X_train, X_test, y_train, y_test = train_test_split(df[X_cols], 
                               df['ictal_ind'],test_size=0.3, random_state=1)   
    rf = RandomForestClassifier(random_state=1)
    rf.fit(X_train, y_train)
    probs = rf.predict_proba(X_test)[:,1]
    print metrics.roc_auc_score(y_test, probs)
    print probs


