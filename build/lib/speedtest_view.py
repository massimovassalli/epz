# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'speedtest.ui'
#
# Created: Tue Sep  8 09:55:31 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1055, 809)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.grafomini = PlotWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grafomini.sizePolicy().hasHeightForWidth())
        self.grafomini.setSizePolicy(sizePolicy)
        self.grafomini.setObjectName(_fromUtf8("grafomini"))
        self.horizontalLayout_2.addWidget(self.grafomini)
        self.grafomaxi = PlotWidget(self.centralwidget)
        self.grafomaxi.setObjectName(_fromUtf8("grafomaxi"))
        self.horizontalLayout_2.addWidget(self.grafomaxi)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lcd1 = QtGui.QLCDNumber(self.centralwidget)
        self.lcd1.setNumDigits(6)
        self.lcd1.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd1.setObjectName(_fromUtf8("lcd1"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lcd1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lcd2 = QtGui.QLCDNumber(self.centralwidget)
        self.lcd2.setNumDigits(6)
        self.lcd2.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd2.setObjectName(_fromUtf8("lcd2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lcd2)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lcd3 = QtGui.QLCDNumber(self.centralwidget)
        self.lcd3.setNumDigits(6)
        self.lcd3.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd3.setObjectName(_fromUtf8("lcd3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lcd3)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lcd4 = QtGui.QLCDNumber(self.centralwidget)
        self.lcd4.setNumDigits(6)
        self.lcd4.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd4.setObjectName(_fromUtf8("lcd4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lcd4)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lcd5 = QtGui.QLCDNumber(self.centralwidget)
        self.lcd5.setNumDigits(6)
        self.lcd5.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd5.setObjectName(_fromUtf8("lcd5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lcd5)
        self.Peakus = QtGui.QLabel(self.centralwidget)
        self.Peakus.setObjectName(_fromUtf8("Peakus"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.Peakus)
        self.lcd6 = QtGui.QLCDNumber(self.centralwidget)
        self.lcd6.setNumDigits(6)
        self.lcd6.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd6.setObjectName(_fromUtf8("lcd6"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.lcd6)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_6)
        self.sLED = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sLED.setFont(font)
        self.sLED.setStyleSheet(_fromUtf8("background-color: gray;"))
        self.sLED.setAlignment(QtCore.Qt.AlignCenter)
        self.sLED.setObjectName(_fromUtf8("sLED"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.sLED)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_7)
        self.sINT = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sINT.setFont(font)
        self.sINT.setStyleSheet(_fromUtf8("background-color:green;"))
        self.sINT.setAlignment(QtCore.Qt.AlignCenter)
        self.sINT.setObjectName(_fromUtf8("sINT"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.sINT)
        self.horizontalLayout_2.addLayout(self.formLayout)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.grafo = PlotWidget(self.centralwidget)
        self.grafo.setObjectName(_fromUtf8("grafo"))
        self.verticalLayout.addWidget(self.grafo)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmd = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmd.sizePolicy().hasHeightForWidth())
        self.cmd.setSizePolicy(sizePolicy)
        self.cmd.setObjectName(_fromUtf8("cmd"))
        self.cmd.addItem(_fromUtf8(""))
        self.cmd.addItem(_fromUtf8(""))
        self.cmd.addItem(_fromUtf8(""))
        self.cmd.addItem(_fromUtf8(""))
        self.cmd.addItem(_fromUtf8(""))
        self.cmd.addItem(_fromUtf8(""))
        self.cmd.addItem(_fromUtf8(""))
        self.cmd.addItem(_fromUtf8(""))
        self.cmd.addItem(_fromUtf8(""))
        self.cmd.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.cmd)
        self.cpar = QtGui.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cpar.sizePolicy().hasHeightForWidth())
        self.cpar.setSizePolicy(sizePolicy)
        self.cpar.setMinimumSize(QtCore.QSize(0, 20))
        self.cpar.setObjectName(_fromUtf8("cpar"))
        self.horizontalLayout.addWidget(self.cpar)
        self.butDo = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butDo.sizePolicy().hasHeightForWidth())
        self.butDo.setSizePolicy(sizePolicy)
        self.butDo.setObjectName(_fromUtf8("butDo"))
        self.horizontalLayout.addWidget(self.butDo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "AvSpeed [Hz]", None))
        self.label_2.setText(_translate("MainWindow", "dt Min [step]", None))
        self.label_3.setText(_translate("MainWindow", "dt Min [us]", None))
        self.label_5.setText(_translate("MainWindow", "dt Max [step]", None))
        self.label_4.setText(_translate("MainWindow", "dt Max [us]", None))
        self.Peakus.setText(_translate("MainWindow", "Peak [us]", None))
        self.label_6.setText(_translate("MainWindow", "Status", None))
        self.sLED.setText(_translate("MainWindow", "OFF", None))
        self.label_7.setText(_translate("MainWindow", "Integrity", None))
        self.sINT.setText(_translate("MainWindow", "OK", None))
        self.cmd.setItemText(0, _translate("MainWindow", "Z", None))
        self.cmd.setItemText(1, _translate("MainWindow", "Y", None))
        self.cmd.setItemText(2, _translate("MainWindow", "D", None))
        self.cmd.setItemText(3, _translate("MainWindow", "P", None))
        self.cmd.setItemText(4, _translate("MainWindow", "K", None))
        self.cmd.setItemText(5, _translate("MainWindow", "s", None))
        self.cmd.setItemText(6, _translate("MainWindow", "g", None))
        self.cmd.setItemText(7, _translate("MainWindow", "8", None))
        self.cmd.setItemText(8, _translate("MainWindow", "R", None))
        self.cmd.setItemText(9, _translate("MainWindow", "Q", None))
        self.butDo.setText(_translate("MainWindow", "GO", None))

from pyqtgraph import PlotWidget
