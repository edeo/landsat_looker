##########################################################################
# logit_reg_Dog1.py
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
import time


def log_reg(formula, df):
    try:
        model1 = smf.logit(formula = formula, data=df).fit()
        print model1.summary()
    except Exception:
        print "+" * 40
        print "bad formula"
        print traceback.format_exc()
        print "+" * 40




if __name__ == '__main__':
    path = '/Users/chadleonard/Repos/DAT3_project/data/'
    dg_name = 'Dog_1'
    dog_1 = pat.Patient(dg_name, path)

    df = pd.read_csv(dog_1.patpath + 'crossval_dir/all_test_files.csv_24_30')
    #print df.head()

    cols = [col for col in df.columns if col.split('_')[0] == 'NVC1202']

    # There are 24 versions of each channel. Things to try:
    # 1) Split each version into 3 sets of 8 channels. i.e. _f1 thru _f8, _f9 thru _f16, and _f17 thru _f24
    # 2) add each set to the logit formula "ictal_ind ~ _f1 + ... _f8" etc.
    # 3) pass forula to log_reg function
    # 4) Use "try/catch" to capture any exception and write some message to a file.
    formula2 = 'x'
    flag = 'Y'
    # all of this is to create the logit formula
    # there were too many channels (features), so they were pruned back to only 8 at a time.
#NVC1202_32_002_Ecog_c010_f2|0.038
#NVC1202_32_002_Ecog_c008_f6|0.042
#NVC1202_32_002_Ecog_c008_f6|0.043
#NVC1202_32_002_Ecog_c003_f12|0.038
#NVC1202_32_002_Ecog_c003_f13|0.042
#NVC1202_32_002_Ecog_c003_f20|0.045
#NVC1202_32_002_Ecog_c004_f20|0.048
#NVC1202_32_002_Ecog_c013_f23|0.048    
    if flag == 'N':
        formula = 'ictal_ind ~ NVC1202_32_002_Ecog_c010_f2 + NVC1202_32_002_Ecog_c008_f6 \
             + NVC1202_32_002_Ecog_c008_f6  + NVC1202_32_002_Ecog_c003_f12 + NVC1202_32_002_Ecog_c003_f13 \
             + NVC1202_32_002_Ecog_c003_f20 + NVC1202_32_002_Ecog_c004_f20 + NVC1202_32_002_Ecog_c013_f23'
        print formula
        log_reg(formula, df)
    else:
        val = 0
        formula = ''    
        for f in range(1,24):
            print "=" * 10
            for c in cols:
                vs = int(c.split('_')[4].replace('c',''))
                if c.split('_')[5] == 'f'+str(f):
                    if val != f:
                        formula = 'ictal_ind ~ ' + c 
                        val = f                    
                    elif val == f and vs == 7:
                        print formula
                        log_reg(formula, df)
#                        time.sleep(1)
                        formula = 'ictal_ind ~ ' + c 
                        val = f
                    elif val == f and vs == 13:
                        print formula
                        log_reg(formula, df)
#                        time.sleep(1)
                        formula = 'ictal_ind ~ ' + c 
                        val = f
                    elif val == f and vs == 19:
                        print formula
                        log_reg(formula, df)
#                        time.sleep(1)
                        formula = 'ictal_ind ~ ' + c 
                        val = f  
                    else:
                        formula = formula + ' + ' + c
        print formula
        log_reg(formula, df)









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






