# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eulerintegrationwidget.ui'
#
# Created: Tue Jul 28 00:24:29 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_EulerIntegrationWidget(object):
    def setupUi(self, EulerIntegrationWidget):
        EulerIntegrationWidget.setObjectName("EulerIntegrationWidget")
        EulerIntegrationWidget.resize(819, 567)
        self.horizontalLayout = QtGui.QHBoxLayout(EulerIntegrationWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dockWidget = QtGui.QDockWidget(EulerIntegrationWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setStyleSheet("QToolBox::tab {\n"
"         background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                     stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"         border-radius: 5px;\n"
"         color: black;\n"
"     }\n"
"\n"
"     QToolBox::tab:selected { /* italicize selected tabs */\n"
"         font: bold;\n"
"         color: black;\n"
"     }\n"
"QToolBox {\n"
"    padding : 0\n"
"}")
        self.dockWidget.setFloating(False)
        self.dockWidget.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.stepSizeSpinBox = QtGui.QDoubleSpinBox(self.dockWidgetContents)
        self.stepSizeSpinBox.setDecimals(4)
        self.stepSizeSpinBox.setMinimum(0.001)
        self.stepSizeSpinBox.setMaximum(1.0)
        self.stepSizeSpinBox.setSingleStep(0.001)
        self.stepSizeSpinBox.setProperty("value", 0.1)
        self.stepSizeSpinBox.setObjectName("stepSizeSpinBox")
        self.horizontalLayout_2.addWidget(self.stepSizeSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.nSpinBox = QtGui.QSpinBox(self.dockWidgetContents)
        self.nSpinBox.setMinimum(2)
        self.nSpinBox.setMaximum(99)
        self.nSpinBox.setProperty("value", 30)
        self.nSpinBox.setObjectName("nSpinBox")
        self.horizontalLayout_5.addWidget(self.nSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.simulateButton = QtGui.QPushButton(self.dockWidgetContents)
        self.simulateButton.setObjectName("simulateButton")
        self.verticalLayout.addWidget(self.simulateButton)
        self.clearButton = QtGui.QPushButton(self.dockWidgetContents)
        self.clearButton.setObjectName("clearButton")
        self.verticalLayout.addWidget(self.clearButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.doneButton = QtGui.QPushButton(self.dockWidgetContents)
        self.doneButton.setObjectName("doneButton")
        self.verticalLayout.addWidget(self.doneButton)
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.horizontalLayout.addWidget(self.dockWidget)
        self.plotPane = QtGui.QWidget(EulerIntegrationWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotPane.sizePolicy().hasHeightForWidth())
        self.plotPane.setSizePolicy(sizePolicy)
        self.plotPane.setObjectName("plotPane")
        self.horizontalLayout.addWidget(self.plotPane)

        self.retranslateUi(EulerIntegrationWidget)
        QtCore.QMetaObject.connectSlotsByName(EulerIntegrationWidget)

    def retranslateUi(self, EulerIntegrationWidget):
        EulerIntegrationWidget.setWindowTitle(QtGui.QApplication.translate("EulerIntegrationWidget", "Heart Transform", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget.setWindowTitle(QtGui.QApplication.translate("EulerIntegrationWidget", "Euler integration example", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EulerIntegrationWidget", "step size (h):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EulerIntegrationWidget", "number of points:", None, QtGui.QApplication.UnicodeUTF8))
        self.simulateButton.setText(QtGui.QApplication.translate("EulerIntegrationWidget", "Simulate", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("EulerIntegrationWidget", "Clear graph", None, QtGui.QApplication.UnicodeUTF8))
        self.doneButton.setText(QtGui.QApplication.translate("EulerIntegrationWidget", "Done", None, QtGui.QApplication.UnicodeUTF8))

