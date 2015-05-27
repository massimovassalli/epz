# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'epz.ui'
#
# Created: Wed May 27 11:58:53 2015
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
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pro1 = QtGui.QProgressBar(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pro1.sizePolicy().hasHeightForWidth())
        self.pro1.setSizePolicy(sizePolicy)
        self.pro1.setMinimum(-5000)
        self.pro1.setMaximum(5000)
        self.pro1.setProperty("value", 24)
        self.pro1.setTextVisible(True)
        self.pro1.setInvertedAppearance(False)
        self.pro1.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.pro1.setObjectName(_fromUtf8("pro1"))
        self.verticalLayout.addWidget(self.pro1)
        self.pro2 = QtGui.QProgressBar(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pro2.sizePolicy().hasHeightForWidth())
        self.pro2.setSizePolicy(sizePolicy)
        self.pro2.setMinimum(-1000)
        self.pro2.setMaximum(1000)
        self.pro2.setProperty("value", -300)
        self.pro2.setObjectName(_fromUtf8("pro2"))
        self.verticalLayout.addWidget(self.pro2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.grafomini = PlotWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grafomini.sizePolicy().hasHeightForWidth())
        self.grafomini.setSizePolicy(sizePolicy)
        self.grafomini.setObjectName(_fromUtf8("grafomini"))
        self.horizontalLayout_2.addWidget(self.grafomini)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.grafo = PlotWidget(self.centralwidget)
        self.grafo.setObjectName(_fromUtf8("grafo"))
        self.horizontalLayout_3.addWidget(self.grafo)
        self.grafomaxi = PlotWidget(self.centralwidget)
        self.grafomaxi.setObjectName(_fromUtf8("grafomaxi"))
        self.horizontalLayout_3.addWidget(self.grafomaxi)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
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
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1055, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pro1.setFormat(_translate("MainWindow", "%v mV", None))
        self.pro2.setFormat(_translate("MainWindow", "%v mV", None))
        self.cmd.setItemText(0, _translate("MainWindow", "Z", None))
        self.cmd.setItemText(1, _translate("MainWindow", "D", None))
        self.cmd.setItemText(2, _translate("MainWindow", "P", None))
        self.cmd.setItemText(3, _translate("MainWindow", "K", None))
        self.cmd.setItemText(4, _translate("MainWindow", "s", None))
        self.cmd.setItemText(5, _translate("MainWindow", "g", None))
        self.butDo.setText(_translate("MainWindow", "GO", None))

from pyqtgraph import PlotWidget
