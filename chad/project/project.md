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

### Directory Structure

```
├── PROJECT_DIR/data/
│   ├── Dog_1
│   │   ├── preictal_segment_0001.mat
│   │   ├── interictal_segment_0001.mat
│   │   ├── test_segment_0001.mat
|   |   ├── [...] 
│   │   ├── preictal_segment_N.mat
│   │   ├── interictal_segment_N.mat
│   │   ├── test_segment_N.mat
[...]
│   ├── Dog_5
│   │   ├── preictal_segment_0001.mat
│   │   ├── interictal_segment_0001.mat
│   │   ├── test_segment_0001.mat
|   |   ├── [...] 
│   │   ├── preictal_segment_N.mat
│   │   ├── interictal_segment_N.mat
│   │   ├── test_segment_N.mat
│   ├── Patient_1
│   │   ├── preictal_segment_0001.mat
│   │   ├── interictal_segment_0001.mat
│   │   ├── test_segment_0001.mat
|   |   ├── [...] 
│   │   ├── preictal_segment_N.mat
│   │   ├── interictal_segment_N.mat
│   │   ├── test_segment_N.mat
│   ├── Patient_2
│   │   ├── preictal_segment_0001.mat
│   │   ├── interictal_segment_0001.mat
│   │   ├── test_segment_0001.mat
|   |   ├── [...] 
│   │   ├── preictal_segment_N.mat
│   │   ├── interictal_segment_N.mat
│   │   ├── test_segment_N.mat
```

# Milestone II: Data Exploration and Analysis Plan

## Data Issues
* Data is in matlab '.mat' files. 
* scipy.io.loadmat() creates a dict with np.ndarrays inside. 
* Need to go down many levels to get to data
* Preictal and Interictal data needs to be Transposed before being loaded to tables.
* For Dog_1 alone there are 480 interictal files, 24 preictal files, and 502 test files. Predictions on the test files are what get submitted to Kaggle.
* There is a lot of data:
  * Each file has 239766 records. That's 10 minutes worth of measurments taken approx. every .002 seconds. There are 399 measurements taken every second.
* The data has 16 channels (columns) that will be the feature list to choose from. The channels are the electrodes that produce the measurements.
 
## Data Questions
1. Can an ML algorithm be run on the data as it is?
2. Or will the data need to be transformed first?
3. Some testing has been done on getting the difference (the absolute value difference) between each measurement in each channel and taking the average difference for each channel. I am trying to see if there is a pattern that differentiates an interictal file from a preictal file. A little difference has been noticed, but it has not been tested to see if it is statistically significant yet.

## The Plan
* Previously, the plan was to load 5 tables in a Postgres DB. Because of the sheer size of the data, that task is taking too much time. In order to do it quickly, csv files needed to be created anyhow, so only csv files will be created from the .mat files for now.
* An ictal_ind flag has been added to each record where ictal_ind = 1 if record comes from a preictal file else 0.
* A record represents one time interval for each of the 16 channels. There are 239766 time intervals.
* The following three formats for the data will be used to determine which more accurately predicts whether the data comes from a preictal or interictal data set.
  * The raw measurements for each channel as they are.
  * The absolute value differences between each time interval measurement as they are. There are 239766 time interval measurement, so there will be 239765 difference measurements.
  * The mean for difference measurements for each channel. This reduces the data considerably. Each file becomes just one record.
* Classification Algorithms (not all of these will be used in the final report)
  * Logistic Regression
  * Linear Regression Classification
  * Support Vector Machine (SVM)
  * Neural Network
  * Random Forest



