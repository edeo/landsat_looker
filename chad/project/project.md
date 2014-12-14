# Course Project -- American Epilepsy Society Seizure Prediction Challenge


## Null Hypothesis
It's not possible to accurately classify preictal brain states in dogs and humans.

## Alternative Hypothesis
The preictal brain state in dogs and humans does exist and can be accurately classified with naturally occurring epilepsy.

## Background: [Kaggle Competition - Seizure Prediction Challenge](http://www.kaggle.com/c/seizure-prediction)
Seizure forecasting systems have the potential to help patients with epilepsy lead more normal lives. In order for EEG-based seizure forecasting systems to work effectively, computational algorithms must reliably identify periods of increased probability of seizure occurrence. If these seizure-permissive brain states can be identified, devices designed to warn patients of impeding seizures would be possible. Patients could avoid potentially dangerous activities like driving or swimming, and medications could be administered only when needed to prevent impending seizures, reducing overall side effects.

There is emerging evidence that the temporal dynamics of brain activity can be classified into 4 states: Interictal (between seizures, or baseline), Preictal (prior to seizure), Ictal (seizure), and Post-ictal (after seizures). Seizure forecasting requires the ability to reliably identify a preictal state that can be differentiated from the interictal, ictal, and postictal state. The primary challenge in seizure forecasting is differentiating between the preictal and interictal states.

## Reason for choosing this project
Wasn't having much luck coming up with a project of my own, so I looked at what was going on at Kaggle. Of all the active Kaggle competitions, this one seemed the most interesting to me. The idea of using Data Science to predict an epileptic seizure, and possibly giving people suffering from epilepsy a chance to alleviate the extent of the seizure, seems both noble and worthwhile.

## Data as described @ Kaggle

[Siezure Data](http://www.kaggle.com/c/seizure-prediction/data)

## Data Dictionary

| Fields               | Description   |
| -------------        |-------------  |
| data                 | a matrix of EEG sample values arranged row x column as electrode x time. |
| data_length_sec      | the time duration of each data row      |
| sampling_frequency   | the number of data samples representing 1 second of EEG data.  |
| channels             | a list of electrode names corresponding to the rows in the data field |
| sequence             | the index of the data segment within the one hour series of clips. For example, preictal_segment_6.mat has a sequence number of 6, and represents the iEEG data from 50 to 60 minutes into the preictal data. |

### Data Files

* preictal_segment_n.mat - the nth preictal training data segment
* interictal_segment_n.mat - the nth non-seizure training data segment
* test_segment_n.mat - the nth testing data segment

NOTE: where n goes from 0 to N  ==> N is the total number of data segments

## Data Issues
* Data is in matlab '.mat' files. 
* scipy.io.loadmat() creates a dict with np.ndarrays inside. 
* Need to go down many levels to get to data
* Preictal and Interictal data needs to be Transposed before being loaded to tables.
* For Dog_1 alone there are 480 interictal files, 24 preictal files, and 502 test files. Predictions on the test files are what get submitted to Kaggle.
* There is a lot of data:
  * Each file has 239766 records. That's 10 minutes worth of measurments taken approx. every .002 seconds. There are 399 measurements taken every second.
* The data has 16 channels (columns) that will be the feature list to choose from. The channels are the electrodes that produce the measurements.
 
## The Methodology  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The data is stored in matlab .mat files. The data represents iEEG measurements, in Hz, of the subjects across 16 electrodes on the subject's body and cranium. The data needs to be transformed in order to make it of any use. Research identified that using a Fast Fourier Tranformation was probably the best way to manipulate the data. Some additional research found a script written in R that did the FFT, then took the absolute values of the FFT and averaged them across channels. But the average was not taken across the entire channel. The code only used the first 7200 records of the file and then took chunks of 300 measurements at a time. This created 24 versions of each channel. The entire file was then condensed down to one record. There were 16 channels coming in, but there were 16 X 24 = 384 channels going out. The R script was also designed to run in parallel, which made it faster than what could be reproduced in Python. After numerous attempts, I was unable to migrate the code to Python, so the R script was used with some minor modifications to it. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Each file was either a preictal or interictal file. All of the files were to be condensed down to one record each and put into a single file for that subject. An indicator variable (ictal_ind) was created to signify whether the file/record was interictal or preictal. This would be used as the response variable for the logistic regression and Random Forest algorithms.
 
* An ictal_ind flag has been added to each record where ictal_ind = 1 if a record comes from a preictal file else 0.
* A record represents one time interval for each of the 16 channels. There are 239766 time intervals.
* The following three formats for the data will be used to determine which more accurately predicts whether the data comes from a preictal or interictal data set.
  * The raw measurements for each channel as they are.
  * The absolute value differences between each time interval measurement as they are. There are 239766 time interval measurements, so there will be 239765 difference measurements.
  * The mean for difference measurements for each channel. This reduces the data considerably. Each file becomes just one record.
* Classification Algorithms (not all of these will be used in the final report)
  * Logistic Regression
  * Random Forest
  
## Random Forest -- Final Results 

|Subject |Number of Trees |Random State |ROC AUC Score    | 
| --------|-------------|-------------|-------------  |
| Dog_1        | 60| 1 |0.82202 |
| Dog_2        | 30| 1 |0.92927 |
| Dog_3        | 50| 1 |0.87484 |
| Dog_4        | 40| 1 |0.86558 |
| Dog_5        | 30| 1 |0.98432 |
| Patient_1    | 40| 1 |1.00000 |
| Patient_2    | 40| 1 |0.88461 |



