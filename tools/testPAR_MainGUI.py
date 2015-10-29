# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testPAR_MainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1106, 572)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.zmin = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.zmin.setMinimum(-100000.0)
        self.zmin.setMaximum(1000000.0)
        self.zmin.setProperty("value", -10.0)
        self.zmin.setObjectName("zmin")
        self.gridLayout.addWidget(self.zmin, 3, 1, 1, 1)
        self.xmax = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.xmax.setMinimum(-100000.0)
        self.xmax.setMaximum(1000000.0)
        self.xmax.setProperty("value", 10.0)
        self.xmax.setObjectName("xmax")
        self.gridLayout.addWidget(self.xmax, 1, 2, 1, 1)
        self.zmax = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.zmax.setMinimum(-100000.0)
        self.zmax.setMaximum(1000000.0)
        self.zmax.setProperty("value", 10.0)
        self.zmax.setObjectName("zmax")
        self.gridLayout.addWidget(self.zmax, 3, 2, 1, 1)
        self.ymax = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.ymax.setMinimum(-100000.0)
        self.ymax.setMaximum(1000000.0)
        self.ymax.setProperty("value", 10.0)
        self.ymax.setObjectName("ymax")
        self.gridLayout.addWidget(self.ymax, 2, 2, 1, 1)
        self.xmin = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.xmin.setMinimum(-100000.0)
        self.xmin.setMaximum(1000000.0)
        self.xmin.setProperty("value", -10.0)
        self.xmin.setObjectName("xmin")
        self.gridLayout.addWidget(self.xmin, 1, 1, 1, 1)
        self.ymin = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.ymin.setMinimum(-100000.0)
        self.ymin.setMaximum(1000000.0)
        self.ymin.setProperty("value", -10.0)
        self.ymin.setObjectName("ymin")
        self.gridLayout.addWidget(self.ymin, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.xdial = QtWidgets.QDial(self.centralwidget)
        self.xdial.setEnabled(False)
        self.xdial.setMinimum(0)
        self.xdial.setMaximum(10000)
        self.xdial.setProperty("value", 5000)
        self.xdial.setInvertedAppearance(False)
        self.xdial.setInvertedControls(False)
        self.xdial.setWrapping(False)
        self.xdial.setNotchTarget(25.0)
        self.xdial.setNotchesVisible(True)
        self.xdial.setObjectName("xdial")
        self.horizontalLayout_3.addWidget(self.xdial)
        self.ydial = QtWidgets.QDial(self.centralwidget)
        self.ydial.setEnabled(False)
        self.ydial.setMinimum(0)
        self.ydial.setMaximum(10000)
        self.ydial.setProperty("value", 5000)
        self.ydial.setWrapping(False)
        self.ydial.setNotchTarget(25.0)
        self.ydial.setNotchesVisible(True)
        self.ydial.setObjectName("ydial")
        self.horizontalLayout_3.addWidget(self.ydial)
        self.zdial = QtWidgets.QDial(self.centralwidget)
        self.zdial.setEnabled(False)
        self.zdial.setMinimum(0)
        self.zdial.setMaximum(10000)
        self.zdial.setProperty("value", 5000)
        self.zdial.setWrapping(False)
        self.zdial.setNotchTarget(25.0)
        self.zdial.setNotchesVisible(True)
        self.zdial.setObjectName("zdial")
        self.horizontalLayout_3.addWidget(self.zdial)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.xled = QtWidgets.QLCDNumber(self.centralwidget)
        self.xled.setSmallDecimalPoint(False)
        self.xled.setNumDigits(6)
        self.xled.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.xled.setObjectName("xled")
        self.verticalLayout_2.addWidget(self.xled)
        self.yled = QtWidgets.QLCDNumber(self.centralwidget)
        self.yled.setSmallDecimalPoint(False)
        self.yled.setNumDigits(6)
        self.yled.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.yled.setObjectName("yled")
        self.verticalLayout_2.addWidget(self.yled)
        self.zled = QtWidgets.QLCDNumber(self.centralwidget)
        self.zled.setSmallDecimalPoint(False)
        self.zled.setNumDigits(6)
        self.zled.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.zled.setObjectName("zled")
        self.verticalLayout_2.addWidget(self.zled)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.xmon = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xmon.sizePolicy().hasHeightForWidth())
        self.xmon.setSizePolicy(sizePolicy)
        self.xmon.setMinimum(0)
        self.xmon.setMaximum(10000)
        self.xmon.setProperty("value", 5000)
        self.xmon.setTextVisible(False)
        self.xmon.setInvertedAppearance(False)
        self.xmon.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.xmon.setObjectName("xmon")
        self.verticalLayout.addWidget(self.xmon)
        self.ymon = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ymon.sizePolicy().hasHeightForWidth())
        self.ymon.setSizePolicy(sizePolicy)
        self.ymon.setMinimum(0)
        self.ymon.setMaximum(10000)
        self.ymon.setProperty("value", 5000)
        self.ymon.setTextVisible(False)
        self.ymon.setObjectName("ymon")
        self.verticalLayout.addWidget(self.ymon)
        self.zmon = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zmon.sizePolicy().hasHeightForWidth())
        self.zmon.setSizePolicy(sizePolicy)
        self.zmon.setMinimum(0)
        self.zmon.setMaximum(10000)
        self.zmon.setProperty("value", 5000)
        self.zmon.setTextVisible(False)
        self.zmon.setObjectName("zmon")
        self.verticalLayout.addWidget(self.zmon)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.xgrafo = PlotWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xgrafo.sizePolicy().hasHeightForWidth())
        self.xgrafo.setSizePolicy(sizePolicy)
        self.xgrafo.setObjectName("xgrafo")
        self.horizontalLayout_4.addWidget(self.xgrafo)
        self.ygrafo = PlotWidget(self.centralwidget)
        self.ygrafo.setObjectName("ygrafo")
        self.horizontalLayout_4.addWidget(self.ygrafo)
        self.zgrafo = PlotWidget(self.centralwidget)
        self.zgrafo.setObjectName("zgrafo")
        self.horizontalLayout_4.addWidget(self.zgrafo)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cmd = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmd.sizePolicy().hasHeightForWidth())
        self.cmd.setSizePolicy(sizePolicy)
        self.cmd.setObjectName("cmd")
        self.cmd.addItem("")
        self.cmd.addItem("")
        self.cmd.addItem("")
        self.cmd.addItem("")
        self.cmd.addItem("")
        self.cmd.addItem("")
        self.cmd.addItem("")
        self.cmd.addItem("")
        self.cmd.addItem("")
        self.cmd.addItem("")
        self.cmd.addItem("")
        self.cmd.addItem("")
        self.cmd.addItem("")
        self.cmd.addItem("")
        self.cmd.addItem("")
        self.cmd.addItem("")
        self.cmd.addItem("")
        self.cmd.addItem("")
        self.cmd.addItem("")
        self.cmd.addItem("")
        self.cmd.addItem("")
        self.cmd.addItem("")
        self.horizontalLayout.addWidget(self.cmd)
        self.cpar = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cpar.sizePolicy().hasHeightForWidth())
        self.cpar.setSizePolicy(sizePolicy)
        self.cpar.setMinimumSize(QtCore.QSize(0, 20))
        self.cpar.setObjectName("cpar")
        self.horizontalLayout.addWidget(self.cpar)
        self.butDo = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butDo.sizePolicy().hasHeightForWidth())
        self.butDo.setSizePolicy(sizePolicy)
        self.butDo.setObjectName("butDo")
        self.horizontalLayout.addWidget(self.butDo)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 20)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.par = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.par.sizePolicy().hasHeightForWidth())
        self.par.setSizePolicy(sizePolicy)
        self.par.setObjectName("par")
        self.par.addItem("")
        self.par.addItem("")
        self.par.addItem("")
        self.par.addItem("")
        self.par.addItem("")
        self.par.addItem("")
        self.par.addItem("")
        self.par.addItem("")
        self.par.addItem("")
        self.par.addItem("")
        self.par.addItem("")
        self.par.addItem("")
        self.horizontalLayout_6.addWidget(self.par)
        self.sendPAR = QtWidgets.QPushButton(self.centralwidget)
        self.sendPAR.setObjectName("sendPAR")
        self.horizontalLayout_6.addWidget(self.sendPAR)
        self.parDisplay = QtWidgets.QLCDNumber(self.centralwidget)
        self.parDisplay.setObjectName("parDisplay")
        self.horizontalLayout_6.addWidget(self.parDisplay)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Min"))
        self.label_5.setText(_translate("MainWindow", "Max"))
        self.label_3.setText(_translate("MainWindow", "Z"))
        self.label_2.setText(_translate("MainWindow", "Y"))
        self.label.setText(_translate("MainWindow", "X"))
        self.xmon.setFormat(_translate("MainWindow", "%v"))
        self.ymon.setFormat(_translate("MainWindow", "%v"))
        self.zmon.setFormat(_translate("MainWindow", "%v"))
        self.cmd.setItemText(0, _translate("MainWindow", "SWITCH_SPI2 send data [1] or not [0] to this client"))
        self.cmd.setItemText(1, _translate("MainWindow", "SET_USECIRCBUFF use [1] or not [0] the Circular Buffer"))
        self.cmd.setItemText(2, _translate("MainWindow", "INIT_SPI2 init the SPI2 and set or reset var \'isTheFirstTime\'"))
        self.cmd.setItemText(3, _translate("MainWindow", "SET_TIMETRIG set variable \'stopTrigTime\'"))
        self.cmd.setItemText(4, _translate("MainWindow", "SET_DAC_2OR4 set DAC to 2V [Vref:5V] or 4V [Vref:10V]"))
        self.cmd.setItemText(5, _translate("MainWindow", "SET_DAC_SOFT soft-set DAC to specified value in Volt"))
        self.cmd.setItemText(6, _translate("MainWindow", "SET_DAC_HARD hard-set DAC to specified value in Volt"))
        self.cmd.setItemText(7, _translate("MainWindow", "SET_SPEEDSIGN set variable \'dacStepSign\' to 0 or 1"))
        self.cmd.setItemText(8, _translate("MainWindow", "SET_SPEED set variables \'dacStep\' and \'dacStepCumul\'"))
        self.cmd.setItemText(9, _translate("MainWindow", "SET_MODEDBG (debug command) set theMode"))
        self.cmd.setItemText(10, _translate("MainWindow", "SET_TESTPIN set TestPin to 0 or 1"))
        self.cmd.setItemText(11, _translate("MainWindow", "SET_DACMODE set DAC mode (unipolar [0] or bipolar [1])"))
        self.cmd.setItemText(12, _translate("MainWindow", "SET_DACTO0 set DAC output to zero"))
        self.cmd.setItemText(13, _translate("MainWindow", "SET_FTRIG set variable \'stopTrigADC\'"))
        self.cmd.setItemText(14, _translate("MainWindow", "SET_ZTRIG set variable \'stopTrigDAC\'"))
        self.cmd.setItemText(15, _translate("MainWindow", "SET_TRIGGERS set which stopTriggers must be used"))
        self.cmd.setItemText(16, _translate("MainWindow", "START_MODSAFE start an operating mode in a safe way"))
        self.cmd.setItemText(17, _translate("MainWindow", "SET_SETPOINT set control setpoint"))
        self.cmd.setItemText(18, _translate("MainWindow", "SET_PGAIN set control P gain"))
        self.cmd.setItemText(19, _translate("MainWindow", "SET_IGAIN set control I gain"))
        self.cmd.setItemText(20, _translate("MainWindow", "SET_DGAIN set control D gain"))
        self.cmd.setItemText(21, _translate("MainWindow", "KILL kills the epizmq program"))
        self.butDo.setText(_translate("MainWindow", "GO"))
        self.par.setItemText(0, _translate("MainWindow", "GET_DEVICE_TYPE "))
        self.par.setItemText(1, _translate("MainWindow", "GET_EXT_ADC_RANGE (red board)"))
        self.par.setItemText(2, _translate("MainWindow", "GET_EXT_ADC_VINMIN (red board)"))
        self.par.setItemText(3, _translate("MainWindow", "GET_EXT_ADC_VINMAX (red board)"))
        self.par.setItemText(4, _translate("MainWindow", "GET_INT_ADC_RESOLUTION (dsPic built-in adc)"))
        self.par.setItemText(5, _translate("MainWindow", "IS_ADCBUF_PRESENT (built-in adc range adapter buffer board)"))
        self.par.setItemText(6, _translate("MainWindow", "GET_ADCBUF_VINMIN"))
        self.par.setItemText(7, _translate("MainWindow", "GET_ADCBUF_VINMAX"))
        self.par.setItemText(8, _translate("MainWindow", "GET_ADCBUF_VOUTMIN"))
        self.par.setItemText(9, _translate("MainWindow", "GET_ADCBUF_VOUTMAX"))
        self.par.setItemText(10, _translate("MainWindow", "GET_DAC_VREF (red board)"))
        self.par.setItemText(11, _translate("MainWindow", "GET_DAC_POLARITY (red board)"))
        self.sendPAR.setText(_translate("MainWindow", "SendPAR"))

from pyqtgraph import PlotWidget
