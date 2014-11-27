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
  
2. Change the DAT3_STUDENTS variable to point to you DAT3-STUDENTS directory
  * DAT3_STUDENTS = '/Users/chadleonard/Repos/DAT3/DAT3_students/DAT3-students/'

3. Execute the script.
4. Follow the popup commands.
   * A Start/Stop popup should appear. On Mac OS running through Spyder, it appears as another Spyder Icon on the Object Bar at the bottom of the screen. Not sure what'll happen on Windows.

![Start/Stop Button](https://github.com/cleonard1261/DAT3-students/blob/master/chad/project/StartStopScreenShot.png "Start/Stop") 
   * Expand the Start/Stop button like so:
 
![Expanded Start/Stop](https://github.com/cleonard1261/DAT3-students/blob/master/chad/project/expanded_start_stop.png "Big Start/Stop") 

![Enter filename](https://github.com/cleonard1261/DAT3-students/blob/master/chad/project/get_file.png "filename") 
 
   * Enter "Dog_1_interictal_segment_0001.mat" in the text box and press 'OK'.

This should create the Raw and FFT plots above.