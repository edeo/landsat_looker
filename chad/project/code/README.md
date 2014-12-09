# Instructions on how to run the code.


## explore_test.py
This code creates the following plots:
![Raw and FFTW Plot](https://github.com/cleonard1261/DAT3-students/blob/master/chad/project/RawAndFFTWPlot.png "Raw and FFTW Plot") 

1. Install the following Python Packages
  * [pyFFTW](https://github.com/hgomersall/pyFFTW) and follow the install instructions.
  * pyqtgraph: Regular package install should suffice -- pip or easy_install 
    * pip install pyqtgraph
    * sudo easy_install pyqtgraph
  * objgraph: Regular package install should suffice -- pip or easy_install 
    * pip install objgraph
    * sudo easy_install objgraph
  
2. Change the DAT3_STUDENTS variable to point to your DAT3-STUDENTS directory
  * DAT3_STUDENTS = '/Users/chadleonard/Repos/DAT3/DAT3_students/DAT3-students/'

3. Execute the script.
4. Follow the popup commands.
   * A Start/Stop popup should appear. On Mac OS running through Spyder, it appears as another Spyder Icon on the Object Bar at the bottom of the screen. Not sure what'll happen on Windows.

![Start/Stop Button](https://github.com/cleonard1261/DAT3-students/blob/master/chad/project/StartStopScreenShot.png "Start/Stop") 
   * Expand the Start/Stop button like so:
 
![Expanded Start/Stop](https://github.com/cleonard1261/DAT3-students/blob/master/chad/project/expanded_start_stop.png "Big Start/Stop") 

  * Press "Start":

![Enter filename](https://github.com/cleonard1261/DAT3-students/blob/master/chad/project/get_file.png "filename") 
 
   * Enter "Dog_1_interictal_segment_0001.mat" in the text box and press 'OK'.

This should create the Raw and FFT plots above.

If you want to view the same plots for multiple files, press "Start" again and add in the other file name.

![Plot of Mutliple files](https://github.com/cleonard1261/DAT3-students/blob/master/chad/project/multi_file.png "multi filenames") 

## patient.py
patient.py has a class called patient that gets called in logit_reg.py. It contains the functions to read in the .mat file and write it to a csv file. It also contains functions to create the cross validation directories based on the k in k-fold. Then it randomly selects interictal and preictal files to put in each of the cv directories. The idea behind the patient class was to create a generic class that could be called for each of the 5 dogs and 2 human patients and would already contain the functions to read in the data, modify it, and write it to a csv file or pass it along to a Machine Learning algorithm. It's almost there. 

## init_pac_f.R
This is R code that creates a csv file of the data after it has gone through a Fast Fourier Transformation. It's a temporary file just to get the FFT to work. The file that is created from this is used in logit_reg.py. It's probably not necessary to concern yourself with init_pac_f.R as it'll be going away and it's quite confusing. Now that I have some code in explore_test.py that does the FFT, it probably won't even be used as a model. 

## logit_reg_SUBJECT.py (NOTE: where SUBJECT is Dog_1,  Dog_2 etc.
logit_reg.py has a function called log_reg that runs statsmodels.formula.api.logit(). In the main function, a patient object is created and the csv file created by init_pac_f.R is read into a DataFrame. Each patient has channels. These are the electrodes placed on the patients body to record the currents. For Dog_1 there are 16 of them. init_pac_f.R took these 16 channels and created even more of them when it divvied up the data for the FFT. So in logit_reg.py the idea was to find out which channels were statistically significant in a logit regression. The first few tries using all the channels in the logit regression caused errors, so the number of channels had to be cut down. That's what the code in the main function does. It cuts the number of channels down into smaller segments and runs multiple logits to see which channels are significant. There is no easy way to get at the p-value from the summary output, so the output was written to a file. Not in the code itself but when executing the code from the command line i.e. python logit_reg.py > log.out 2>&1 . logit_reg_SUBJECT.py is used to select features for the random forest algorithms.

## rand_forest_SUBJECT.py
Executes the random forests on the features (channels) that were chosen by looking at the pvalues from the logistic regression output. I tried to get each Random forest to at least .80 in the AUC curve. To run, just change the path to ../data/ i.e. path = '../data/' and then execute the script and see the output.  
