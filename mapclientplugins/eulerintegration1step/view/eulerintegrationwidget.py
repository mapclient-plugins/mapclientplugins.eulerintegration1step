'''
Created on May 26, 2015

@author: andre
'''
from PySide import QtGui, QtCore

import numpy as np

import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'
import pylab

from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

from matplotlib.figure import Figure
from matplotlib.backend_bases import key_press_handler

from mapclientplugins.eulerintegration1step.view.ui_eulerintegrationwidget import Ui_EulerIntegrationWidget
from mapclientplugins.eulerintegration1step.sedml.execute import ExecuteSedml

class EulerIntegrationWidget(QtGui.QWidget):
    '''
    classdocs
    '''


    def __init__(self, parent=None):
        '''
        Constructor
        '''
	super(EulerIntegrationWidget, self).__init__(parent)
        self._ui = Ui_EulerIntegrationWidget()
        self._ui.setupUi(self)
	self.sedml = ExecuteSedml()
	# create the plot
	self.fig = Figure((5.0, 4.0), dpi=100)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self._ui.plotPane)
        self.canvas.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.canvas.setFocus()
        self.mpl_toolbar = NavigationToolbar(self.canvas, self._ui.plotPane)
        self.canvas.mpl_connect('key_press_event', self.on_key_press)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.canvas)  # the matplotlib canvas
        vbox.addWidget(self.mpl_toolbar)
        self._ui.plotPane.setLayout(vbox)
        #self.setCentralWidget(self.main_frame)
        
	self._makeConnections()

    def _makeConnections(self):
        self._ui.doneButton.clicked.connect(self._doneButtonClicked)
        self._ui.simulateButton.clicked.connect(self._simulateButtonClicked)
        self._ui.clearButton.clicked.connect(self._clearButtonClicked)
        
    def on_key_press(self, event):
        print('you pressed', event.key)
        # implement the default mpl key press events described at
        # http://matplotlib.org/users/navigation_toolbar.html#navigation-keyboard-shortcuts
        key_press_handler(event, self.canvas, self.mpl_toolbar)

    def _simulateButtonClicked(self):
        print "Simulate clicked"
	data = self.sedml.execute(self._ui.stepSizeSpinBox.value())
	if data == None:
		return
	self.axes = self.fig.add_subplot(111)
        #self.axes.plot(self.x, self.y, 'ro')
	data1 = np.arange(20).reshape([4, 5]).copy()
        self.axes.imshow(data1, interpolation='nearest')
        #self.axes.plot([1,2,3])
        self.canvas.draw()
    
    def _clearButtonClicked(self):
        print "Clear button clicked"
	self.fig.clear()
                        
    def initialise(self):
        print "Initialise called?"
        
    def registerDoneExecution(self, callback):
        self._callback = callback
        
    def _doneButtonClicked(self):
        self._callback()
        

