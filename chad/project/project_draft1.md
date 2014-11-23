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

* [subject]_n_preictal_segment_n.mat - the nth preictal training data segment
* [subject]_n_interictal_segment_n.mat - the nth non-seizure training data segment
* [subject]_n_test_segment_n.mat - the nth testing data segment

NOTE: where n goes from 0 to N  ==> N is the total number of data segments.
And [subject] is Dog_1 thru Dog_5 or Patient_1 thru Patient_2

### Directory Structure

```
├── PROJECT_DIR/data/
│   ├── Dog_1
│   │    crossval_dir
│   │    │   cv_0   
│   │    │   ├── Dog_1_preictal_segment_<randint>.mat
│   │    │   ├── Dog_1_interictal_segment_<randint>.mat
│   │    │   ├── [...] 
│   │    │   ├── Dog_1_preictal_segment_<randint>.mat
│   │    │   ├── Dog_1_interictal_segment_<radnint>.mat
│   │    │   cv_1   
│   │    │   ├── Dog_1_preictal_segment_<randint>.mat
│   │    │   ├── Dog_1_interictal_segment_<randint>.mat
│   │    │   ├── [...] 
│   │    │   ├── Dog_1_preictal_segment_<randint>.mat
│   │    │   ├── Dog_1_interictal_segment_<radnint>.mat
[...]
│   │    │   cv_N   
│   │    │   ├── Dog_1_preictal_segment_<randint>.mat
│   │    │   ├── Dog_1_interictal_segment_<randint>.mat
│   │    │   ├── [...] 
│   │    │   ├── Dog_1_preictal_segment_<randint>.mat
│   │    │   ├── Dog_1_interictal_segment_<radnint>.mat
Where <randint> represents the number of the randomly chosen file. 
```

# Data Exploration and Analysis

## Data Issues
* Data is in matlab '.mat' files. 
* scipy.io.loadmat() creates a dict with np.ndarrays inside. 
* Need to go down many levels to get to data
* Preictal and Interictal data needs to be Transposed before being loaded to tables.
* For Dog_1 alone there are 480 interictal files, 24 preictal files, and 502 test files. Predictions on the test files are what get submitted to Kaggle.
* There is a lot of data:
  * Each file has 239766 records. That's 10 minutes worth of measurments taken approx. every .002 seconds. There are 399 measurements taken every second.
* The data has 16 channels (columns) that will be the feature list to choose from. The channels are the electrodes that produce the measurements.
 
## Achievements To Date
* The code to read the data is written. 
* Found some code written in R and Python that runs Fast Fourier Transforms on the data. 
* Used the FFT transformed data to run logit regression. The first time the logit was run, no features were found to be statistically significant viz a viz their p-values.
 * The problem was the ratio of preictal to interictal files was too small. Changed the ratio up and started seeing some p-values below .05. 

* Classification Algorithms (not all of these will be used in the final report)
  * Logistic Regression
   * Tried Logit and saw some success.
  * Random Forest
   * Have yet to learn about Random Forests, but other contestants in the Kaggle competition have mentioned their successes using Random Forests.
  
  ### Cross Validation Data
* For Dog_1 there are 480 interictal files and 24 preictal files. About 5% of the files are preictal and 95% interictal. With that in mind, these are the different options available for CV:
   * Create a process that randomly selects 19 interictal files and 1 preictal file, and do this 5 or so different times, to determine the best model.
   * Use different ratios. 19:1, 10:2, 5:1,...etc.
* Use similar process for all dogs and patients.



