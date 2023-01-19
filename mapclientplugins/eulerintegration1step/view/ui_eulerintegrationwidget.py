# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'eulerintegrationwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDockWidget, QDoubleSpinBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_EulerIntegrationWidget(object):
    def setupUi(self, EulerIntegrationWidget):
        if not EulerIntegrationWidget.objectName():
            EulerIntegrationWidget.setObjectName(u"EulerIntegrationWidget")
        EulerIntegrationWidget.resize(819, 567)
        self.horizontalLayout = QHBoxLayout(EulerIntegrationWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dockWidget = QDockWidget(EulerIntegrationWidget)
        self.dockWidget.setObjectName(u"dockWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setStyleSheet(u"QToolBox::tab {\n"
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
        self.dockWidget.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.dockWidgetContents)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.stepSizeSpinBox = QDoubleSpinBox(self.dockWidgetContents)
        self.stepSizeSpinBox.setObjectName(u"stepSizeSpinBox")
        self.stepSizeSpinBox.setDecimals(4)
        self.stepSizeSpinBox.setMinimum(0.001000000000000)
        self.stepSizeSpinBox.setMaximum(1.000000000000000)
        self.stepSizeSpinBox.setSingleStep(0.001000000000000)
        self.stepSizeSpinBox.setValue(0.100000000000000)

        self.horizontalLayout_2.addWidget(self.stepSizeSpinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.dockWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.nSpinBox = QSpinBox(self.dockWidgetContents)
        self.nSpinBox.setObjectName(u"nSpinBox")
        self.nSpinBox.setMinimum(2)
        self.nSpinBox.setMaximum(99)
        self.nSpinBox.setValue(30)

        self.horizontalLayout_5.addWidget(self.nSpinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.simulateButton = QPushButton(self.dockWidgetContents)
        self.simulateButton.setObjectName(u"simulateButton")

        self.verticalLayout.addWidget(self.simulateButton)

        self.clearButton = QPushButton(self.dockWidgetContents)
        self.clearButton.setObjectName(u"clearButton")

        self.verticalLayout.addWidget(self.clearButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.doneButton = QPushButton(self.dockWidgetContents)
        self.doneButton.setObjectName(u"doneButton")

        self.verticalLayout.addWidget(self.doneButton)

        self.dockWidget.setWidget(self.dockWidgetContents)

        self.horizontalLayout.addWidget(self.dockWidget)

        self.plotPane = QWidget(EulerIntegrationWidget)
        self.plotPane.setObjectName(u"plotPane")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.plotPane.sizePolicy().hasHeightForWidth())
        self.plotPane.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.plotPane)


        self.retranslateUi(EulerIntegrationWidget)

        QMetaObject.connectSlotsByName(EulerIntegrationWidget)
    # setupUi

    def retranslateUi(self, EulerIntegrationWidget):
        EulerIntegrationWidget.setWindowTitle(QCoreApplication.translate("EulerIntegrationWidget", u"Heart Transform", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("EulerIntegrationWidget", u"Euler integration example", None))
        self.label.setText(QCoreApplication.translate("EulerIntegrationWidget", u"step size (h):", None))
        self.label_2.setText(QCoreApplication.translate("EulerIntegrationWidget", u"number of points:", None))
        self.simulateButton.setText(QCoreApplication.translate("EulerIntegrationWidget", u"Simulate", None))
        self.clearButton.setText(QCoreApplication.translate("EulerIntegrationWidget", u"Clear graph", None))
        self.doneButton.setText(QCoreApplication.translate("EulerIntegrationWidget", u"Done", None))
    # retranslateUi

