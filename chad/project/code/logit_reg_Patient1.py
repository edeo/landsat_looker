##########################################################################
# logit_reg_Patient1.py
# Create logistic regression script
#
# Author:   Chad Leonard
# Created:  November 14, 2014
#
##########################################################################


"""
Create patient object
"""

##########################################################################
## Imports
##########################################################################
import patient as pat
import sys
import pandas as pd
import statsmodels.formula.api as smf
from scipy.io import loadmat
import scipy
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import traceback


def log_reg(formula, df):
    try:
        model1 = smf.logit(formula = formula, data=df).fit()
        print model1.summary()
    except Exception:
        print "+" * 40
        print "bad formula"
        print "+" * 40




if __name__ == '__main__':
    path = '/Users/chadleonard/Repos/DAT3_project/data/'
    dg_name = 'Patient_1'
    dog = pat.Patient(dg_name, path)
    print dog.name

    df = pd.read_csv(dog.patpath + '/mat_dir.csv_24_30')
#    print df.head()

    cols = [col for col in df.columns if col.split('_')[0] == 'LD' or col.split('_')[0] == 'RD']

    # There are 24 versions of each channel. Things to try:
    # 1) Split each version into 3 sets of 8 channels. i.e. _f1 thru _f8, _f9 thru _f16, and _f17 thru _f24
    # 2) add each set to the logit formula "ictal_ind ~ _f1 + ... _f8" etc.
    # 3) pass forula to log_reg function
    # 4) Use "try/catch" to capture any exception and write some message to a file.
    formula2 = 'x'

    # all of this is to create the logit formula
    # there were too many channels (features), so they were pruned back to only 8 at a time.
    for c in cols:
        print c
        if c.split('_')[2] == 'f1':
            print "c is:", c
        x = int(c.split('_')[2].replace('f',''))
        if x == 1:
            formula = 'ictal_ind ~ ' + c
        elif x <= 8:
            formula =  formula + ' + ' + c
        elif x == 9:
            print '-' * 10
            print formula
            log_reg(formula, df)
            formula1 = 'ictal_ind ~ ' + c
        elif x <= 16:
            formula1 =  formula1 + ' + ' + c
        elif x == 17:
            print '-' * 10
            print formula1
            log_reg(formula1, df)
            formula2 = 'ictal_ind ~ ' + c
        elif x <= 23:
            formula2 =  formula2 + ' + ' + c
        elif x == 24:
            formula2 =  formula2 + ' + ' + c
            print '-' * 10
            print formula2
            log_reg(formula2, df)






        # print '+' * 10
        # print form
    
    
    
    # form = 'ictal_ind ~ NVC1202_32_002_Ecog_c002_f1 + NVC1202_32_002_Ecog_c002_f2 + NVC1202_32_002_Ecog_c002_f3 + \
    #             NVC1202_32_002_Ecog_c002_f4 + NVC1202_32_002_Ecog_c002_f5 + NVC1202_32_002_Ecog_c002_f6 + NVC1202_32_002_Ecog_c002_f7 \
    #             + NVC1202_32_002_Ecog_c002_f8 + NVC1202_32_002_Ecog_c002_f9 + NVC1202_32_002_Ecog_c002_f10 + NVC1202_32_002_Ecog_c002_f11 \
    #             + NVC1202_32_002_Ecog_c002_f12 + NVC1202_32_002_Ecog_c002_f13 '
    # more than 13 predictors seems to cause an issue. 
    # model1 = smf.logit(formula = form, data=df).fit()
    # print model1.summary()
        # form = ' '
        # print type(form)
        # a=0
        #print model1.summary()






