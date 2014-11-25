##########################################################################
# patient.py
# Create patient object
#
# Author:   Chad Leonard
# Created:  November 8, 2014
#
##########################################################################


"""
Create patient object
"""

##########################################################################
## Imports
##########################################################################

import scipy.io
import numpy as np
import pandas as pd
import os
import csv
import traceback
import sys
import subprocess
import random

##########################################################################
## Patient Object
##########################################################################

class Patient(object):
    """
    Patient object that represents the 5 dogs and 2 humans that have epilepsy.
    """

    def __init__(self,name, path):
        """
        Initializes the patient object.
        """
        self.name = name
        self.patpath = path + self.name + '/'
        self.matpath = self.patpath + '/mat_dir/'
        self.csvpath = self.patpath+ '/csv_dir/'
        self.testpath = self.patpath + '/test_dir/'

    def get_diff_colnames(self,cols):
        """
        This code may not be valid any longer. It was used initially when I was experimenting
        with how to transform the data. 
        """
    	colnames =[]
    	for col in cols:
            # takes each of the "feature" columns and appends '_mean' and '_std' to them.
            # later the mean and standard deviation for each column (channel) will be calculated.
    		colnames.append(col + '_mean')
    		colnames.append(col + '_std')
    	colnames.append('filename')
        colnames.append('ictal_ind')
    	return colnames

    def create_df(self, fn, path):
    	"""
    	Create DataFrame for input file
    	"""
        # this function reads in the .mat (matlab) file and creates a dataframe...
    	noList = ['__version__', '__header__', '__globals__']
        # the .mat file has arrays of arrays of arrays. 
        # the three "keys" above are not needed. The 4th key has all the data, the column names of the data, 
        # the data_length_sec, the sampling_frequency, and the sequence. 
    	mat = scipy.io.loadmat(path + fn)
    	field = [fld for fld in mat.keys() if fld not in noList ]
        # take only the key from mat.keys() that is not in the list above...

    	colnames = []
    	for i in mat[field[0]][0][0][3][0]:
            # not sure how to describe this. The column names are the 3rd item (column?) a few levels down in the 
            # array of arrays. Figured this out by trial and error...
    		colnames.append(i[0])

    	lis = pd.DataFrame(mat[field[0]][0][0][0].T, columns=colnames)
        # the data is the 1st element. The data comes in as rows. The first column in the row is the name of the 
        # channel. A channel is a name of an electrode placed on the patient. The rest of the columns are the 
        # time intervals for each measurement. There are 239766 time intervals in 10 minutes of data. That's a measurement
        # approximately every .008 seconds.  I transpose the data to make every channel a column.

    	lis['data_length_sec'] = mat[field[0]][0][0][1][0][0]
        # data_length_sec is the 2nd element

    	lis['sampling_frequency'] = int(mat[field[0]][0][0][2][0][0])
        # sampling_frequency is the 3rd element.

    	lis['sequence'] = mat[field[0]][0][0][4][0][0]
        # sequence is the 4th element.

    	val = fn.split('_')[2]
    	# if "preictal" is in the file name then set the ictal_ind to 1 else 0. This will be the response
        # variable in a logistic regression. 
        if val == 'preictal':
    		lis['ictal_ind'] = 1
    	else:
    		lis['ictal_ind'] = 0
        lis['filename'] = fn
    	return lis

    def create_dir(self,patient, kfold):
        """
        Creates cross validation directories for each patient object.
        """
        # scikit.learn cross validation functions won't work here (I think). The data is very large and each file
        # only contains one of the response variables. 
        # This creates k cross validation directories for the patient object.
        # The interictal and preictal data files will be (later) randomly assigned to each of the k 
        # crossval directories. 
        if not os.path.exists(patient.patpath + 'crossval_dir'):
            os.mkdir(patient.patpath + 'crossval_dir', 0755 )
        for i in range(kfold):
            if not os.path.exists(patient.patpath + 'crossval_dir' + '/cv_' + str(i)):
                os.mkdir(patient.patpath + 'crossval_dir' + '/cv_' + str(i), 0755 )
            

    def setup_cross_val(self, patient, kfold):
        """
        Randomly moves preictal and interictal .mat files to the k crossval directories. 
        """
        # this function takes the number of folds for the cross validation and randomly chooses
        # preictal and interictal files and assigns them to each of the cv directories. 
        # the proporition of preictal to interictal, currently, reflects the proportion of
        # preictal to interictal files for the patient. This function will be modifed to pass in the proportion.
        print patient.name
        included_extenstions = ['mat'] 
        file_names = [fn for fn in os.listdir(patient.matpath) if any([fn.endswith(ext) for ext in included_extenstions])]
        # grab all the .mat filenames in the patient's matpath directory.
        preictal_files = [pre for pre in file_names if pre.split('_')[2].lower() == 'preictal']
        # get the list of preictal file names
        interictal_files = [inter for inter in file_names if inter.split('_')[2].lower() == 'interictal']
        # get the list of interictal file names
        print "preictal_length is:", len(preictal_files)
        print preictal_files
        print len(interictal_files)
        preprop = len(preictal_files) / float((len(preictal_files) + len(interictal_files)))
        # the proportion of files that are preictal
        interprop = 1 - preprop
        print "proportion are preictal:", preprop
        print "proportion are interictal:", interprop
        inter = len(interictal_files) / kfold
        pre   = len(preictal_files) / kfold
        print int((len(interictal_files) / kfold) * preprop)
        patient.create_dir(patient, kfold)
        print pre
        #pre_rand = random.sample(preictal_files, pre)
        #print inter
        #print random.sample(interictal_files,inter)
        for k in range(kfold):
            for fil in random.sample(preictal_files, pre):
                # randomly grab preictial files from the list and evenly spread them across all k crossval directories.
                print fil
                subprocess.call(["mv", patient.matpath + fil, patient.patpath + 'crossval_dir' + '/cv_' + str(k)])
                preictal_files.remove(fil) # once the file has been used remove its name from the list.
            for ifil in random.sample(interictal_files, inter):
                # randomly grab interictial files from the list and evenly spread them across all k crossval directories.
                subprocess.call(["mv", patient.matpath + ifil, patient.patpath + 'crossval_dir' + '/cv_' + str(k)])
                interictal_files.remove(ifil) # once the file has been used remove its name from the list.
        





##########################################################################
## Data Transformations
##########################################################################

    def create_diff_df(self,diffcols, filename, df):
        """
        Function finds the mean and standard deviation for the absolute difference in values between adjacent channel measurements.
        """
        # function is deprecated.
        # creates a Pandas DataFrame that has the mean and standard deviation for the absolute differences for each channel.
        dframe = pd.DataFrame(index=range(1),columns=diffcols)
        for col in cols:
            print col
            vlist = []
            for i in range(len(df)-1):
                vlist.append(float(abs(float(df[col][i+1])) - float(df[col][i])))
            dframe[col + '_mean'][0] = np.mean(vlist)
            dframe[col + '_std'][0] = np.std(vlist)
        dframe['filename'][0] = fl
        if filename.split('_')[2] == 'preictal':
            dframe['ictal_ind'][0] = 1
        else:
            dframe['ictal_ind'][0] = 0
        return dframe

    def fft(self, df):
        """
        Fast Fourier Transformation for the channel (feature) values measured in Hertz.
        """
        # currently the FFT function is written in R. Needs to be migrated to python.
        pass

##########################################################################
## Test the code....
##########################################################################

if __name__ == '__main__':
     """
     __main__ function to test some of the code from above. some functions won't be used going forward.
     """
    start = int(sys.argv[1])
    end   = int(sys.argv[2])
    # variables passed in from the command line to tell how many crossval directories to go to
    # and process the data from.
    print start, end
    path = '/Users/chadleonard/Repos/DAT3_project/data/'
    dg_name = 'Dog_1'
    dog_1 = Patient(dg_name, path)
    # instantiate patient by passing it the patient name, which is also the directory where the data resides, and the path to that 
    # directory to Patient().
    print dog_1.name
    for i in range(start,end):
        cv_dir = path + '/' + dg_name + '/crossval_dir/' + '/cv_' + str(i) +'/'
        included_extenstions = ['mat']
        file_names = [fn for fn in os.listdir(cv_dir) if any([fn.endswith(ext) for ext in included_extenstions])]
        # print cv_dir
        #print file_names
        dframe = []
        #file_names = [ 'Dog_1_interictal_segment_0001.mat', 'Dog_1_preictal_segment_0003.mat']
        for fl in file_names:
            df = dog_1.create_df(fl, cv_dir)
            print "file:", df.filename[0]
            cols = [col for col in df.columns if col.split('_')[0] == 'NVC1202']
            # the names of all the channels (features) begin with 'NVC1202'.
            # this is getting all of the channel names.
            diffcols = dog_1.get_diff_colnames(cols)
            #diffcols.append('ictal_ind')
            diff_df = dog_1.create_diff_df(diffcols, fl, df)
            # for each .mat file with 239766 records one diff record is created.

            if isinstance(dframe, pd.DataFrame):
                # takes all of the diff records and appends them to one dataframe.
                dlist = []
                dlist.append(dframe[:])
                dlist.append(diff_df[:])
                dframe = pd.concat(dlist)
            else:
                dframe = diff_df
            #print dframe
        dframe.to_csv(cv_dir + 'cv_' + str(i) + '_diff.csv', sep=',', encoding='utf-8', index=False)
        # write the dataframe to a csv file.




