# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 12:20:17 2014

@author: chadleonard
"""
##########################################################################
# rand_forest_dog1.py
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
    dg_name = 'Dog_1'
    dog_1 = pat.Patient(dg_name, path)
#    df = pd.read_csv(dog_1.patpath + 'crossval_dir/all_test_files.csv_24_30')
    df = pd.read_csv(dog_1.patpath + 'mat_dir.csv_24_30')
    print dog_1.name
    
#    The best auc score so far with 0.804464285714 ...
#   X_cols = ['NVC1202_32_002_Ecog_c002_f1' 
#    ,'NVC1202_32_002_Ecog_c004_f1' 
#    ,'NVC1202_32_002_Ecog_c006_f1' 
#    ,'NVC1202_32_002_Ecog_c011_f1'
#    ,'NVC1202_32_002_Ecog_c003_f2'
#    ,'NVC1202_32_002_Ecog_c007_f3'
#    ,'NVC1202_32_002_Ecog_c005_f7'
#    ,'NVC1202_32_002_Ecog_c012_f19']
#    
    X_cols = ['NVC1202_32_002_Ecog_c002_f1' 
    ,'NVC1202_32_002_Ecog_c004_f1' 
    ,'NVC1202_32_002_Ecog_c006_f1' 
    ,'NVC1202_32_002_Ecog_c011_f1'
    ,'NVC1202_32_002_Ecog_c003_f2'
    ,'NVC1202_32_002_Ecog_c007_f3'
    ,'NVC1202_32_002_Ecog_c005_f7'
    ,'NVC1202_32_002_Ecog_c012_f19']
    
    X_train, X_test, y_train, y_test = train_test_split(df[X_cols], 
                               df['ictal_ind'],test_size=0.3, random_state=1)
    rf = RandomForestClassifier(random_state=1)
    rf.fit(X_train, y_train)
    probs = rf.predict_proba(X_test)[:,1]
    print metrics.roc_auc_score(y_test, probs)
    print probs
#    print y_test
#    print X_test


