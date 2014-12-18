##########################################################################
# explore.py
# script to explore matlab siezure data
#
#
# Author:   Chad Leonard
# Created:  November 22, 2014
#
##########################################################################
'''
data structure is a follows:
data[0] == channel # x sample count array of raw data from 
data[1] == data_length_sec: the time duration of each data row
data[2] == sampling_frequency: the number of data samples representing 1 second of EEG data
data[3] == channels: a list of electrode names corresponding to the rows in the data field
data[4] == sequence: the index of the data segment within the one hour series of clips. For example, preictal_segment_6.mat has a sequence number of 6, and represents the iEEG data from 50 to 60 minutes into the preictal data.
'''

import scipy.io
import numpy as np
import os
import sys
from pyfftw import FFTW
from itertools import islice
from collections import deque
from PyQt4 import QtGui, QtCore
import pyqtgraph as pg

import objgraph

class FileHandler(object):
  DAT3_STUDENTS = '/Users/lindaxie/desktop/DAT3-students/'
  DATA_DIR = DAT3_STUDENTS + 'chad/project/data/Dog_1/crossval_dir/cv_0/'
  if not os.path.exists(DATA_DIR):
    DATA_DIR = None
    print "Configure the data directory to match local directory structure"

  def __init__(self):
    self.file_in = '../data/Dog_1/crossval_dir/cv_0/Dog_1_interictal_segment_0001.mat' 

  def get_data(self):
    # Reads data in from .mat file. File name is passed in to the dialog box.
    #self.file_in = "_".join(self.file_in.split("_")[0:2]) + "/" + self.file_in
    print "this is self.file_in", self.file_in
    with open(self.DATA_DIR + self.file_in) as f:
      mat = scipy.io.loadmat(f)
      keys = mat.keys()
      print keys
      i = [mat.keys().index(key) for key in mat.keys() if key.find('segment') > 0][0]
      # gets the index of the key where the data is: for instance the key 'interictal_segment_4' is where the data and columns are
      data = mat[mat.keys()[i]]
    self.data = data[0,0]
    self.data_length_sec = self.data[1][0]
    self.frequency = self.data[2][0]
    self.electrode_names = self.data[3][0]
    self.sequence_num = self.data[4]

class Cine(object):
  def __init__(self, FileHandler):
    self.filehandler = FileHandler
    self.app = QtGui.QApplication(sys.argv)
    # QtGui application takes input from the popup ...
    self.widget = QtGui.QWidget()
    self.start_btn = QtGui.QPushButton('Start')
    self.stop_btn = QtGui.QPushButton('Stop')
    self.file_in = QtGui.QInputDialog()
    self.layout = QtGui.QGridLayout()
    self.layout.addWidget(self.start_btn, 0, 0)
    self.layout.addWidget(self.stop_btn, 0, 1)
    self.widget.setLayout(self.layout)
    # execute self.start if start button is selected.
    self.start_btn.clicked.connect(self.start)
    self.stop_btn.clicked.connect(self.stop)
    self.widget.show()

  def cons_plots(self, num_channels):
    #for i in range(num_channels):
    for i in range(1):
      i = str(i)
      setattr(self, 'rawplot_' + i, pg.PlotWidget())
      # creates the 'rawplot_0' thru 'rawplot_15' which are pg.PlotWidget() object
      #getattr(self, 'rawplot_' + i).setRange(yRange=(1000, -1000))
      getattr(self, 'rawplot_' + i).setRange(yRange=(200, -200))
      # calls pg.PlotWidget().setRange ==> setRange sets the visible range of the ViewBox.
      setattr(self, 'fftplot_' + i, pg.PlotWidget())
      #getattr(self, 'fftplot_' + i).setRange(yRange=(0, 170))
      getattr(self, 'fftplot_' + i).setRange(yRange=(40, 120))
      self.layout.addWidget(getattr(self, 'rawplot_' + i))
      # Adds the given widget to the cell grid at row, column. The top-left position is (0, 0) by default.
      # in the output this is the first rawplot.. each additionaly rawplot is added below this
      self.layout.addWidget(getattr(self, 'fftplot_' + i))
      # Adds the given widget to the cell grid at row, column. The top-left position is (0, 0) by default.
      # in the output this is the first fftplot_.. each additionaly fftplot_ is added below this

  def start(self):
    print "inside start"
    self.filehandler.file_in = str(self.file_in.getText(self.widget, "", "what file?")[0])
    # this is what gets executed when the start button on the popbox/button is clicked
    print self.filehandler.file_in 
    self.filehandler.get_data()
    # calls FileHandler.get_data() ... this gets the data from the .mat file.
    num_channels = self.filehandler.data[0].shape[0]
    print num_channels
    num_samples = self.filehandler.data[0].shape[1]
    print num_samples
    self.make_iterators(num_channels)
    # turns the channels into flat iterator...
    self.plot(num_channels, num_samples)
    # calls Cine.plot()

  def stop(self):
    # this is what gets executed when the stop button on the popbox/button is clicked.
    sys.exit()
    self.x_time.clear()
    self.y_val.clear()

  def make_iterators(self, num_channels):
    # makes an iterator of a list that has been flattened.
    for i in range(num_channels):
      setattr(self, 'rawchan_' + str(i), self.filehandler.data[0][i].flat)
      
  def do_fft(self, inputa):
    outputa = np.zeros(self.fft_size, dtype=complex)
    fft_plan = FFTW(inputa, outputa, direction='FFTW_FORWARD')
    #fft_plan = FFTW.Plan(inputa, outputa, direction='forward', flags=['estimate'])
    fft_plan.execute()
    return (np.log10(np.abs(outputa)) * 20)[:self.fft_size/2]

  def plot(self, num_channels, num_samples):
    #initialize parameters, graphs, and collections for plotting
    self.cons_plots(num_channels)

    self.fft_size, fft_stop = 5000, 10000
    fft_start = fft_stop - self.fft_size

    bins = [i for i in xrange(self.fft_size/2)]
    #print len(bins)
    # bin is a list of integers from 0 to 2499
    x_time = deque([0], fft_stop)
    y_val = [deque([0], fft_stop) for i in range(num_channels)]
    # deque pronounced "deck" is a double-ended queue...
    #iterate over the data and make plots
    for time_s in xrange(num_samples):
      x_time.append(time_s)
      # appending 239766 time intervals to x_time
      for i in range(num_channels):
        y_val[i].append(getattr(self, 'rawchan_' + str(i)).next())
        # populating y_val[channel_number] with the next value from rawchan_channelnumber
      if time_s % 5000 == 0 and len(y_val[0]) >= fft_stop:
        # for every 5000 time intervals 
        # 
        #for i in range(num_channels):
        for i in range(1):
          #print 'fftplot_' + str(i)
          outputa = self.do_fft(np.array(list(islice(y_val[i], fft_start, fft_stop)), dtype=complex))
          #print len(outputa)
          # run FFTW against time intervals 5000 to 10000 for each channel.
          #getattr(self, 'fftplot_' + str(i)).plot(bins[:200], outputa[0:200], clear=True)
          getattr(self, 'fftplot_' + str(i)).plot(bins, outputa[0:], clear=True)
          #print type(getattr(self, 'fftplot_' + str(i))
          # <pyqtgraph.widgets.PlotWidget.PlotWidget object at 0x116f935a8>
          #print [x/5000.0 for x in x_time]
          getattr(self, 'rawplot_' + str(i)).plot([x/5000.0 for x in x_time], y_val[i], clear=True)
          #self.app.processEvents()
        self.app.processEvents()
        # processEvents
        #print objgraph.show_most_common_types()

if __name__ == '__main__':
  fh = FileHandler()
  cine = Cine(fh)
  print "after Cine"
  cine.app.exec_()
  print "electrode_names", fh.electrode_names
  print "after cine.app.exec_()"
    

