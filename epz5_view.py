# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'epz.ui'
#
# Created: Wed May 27 11:58:47 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1055, 809)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pro1 = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pro1.sizePolicy().hasHeightForWidth())
        self.pro1.setSizePolicy(sizePolicy)
        self.pro1.setMinimum(-5000)
        self.pro1.setMaximum(5000)
        self.pro1.setProperty("value", 24)
        self.pro1.setTextVisible(True)
        self.pro1.setInvertedAppearance(False)
        self.pro1.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.pro1.setObjectName("pro1")
        self.verticalLayout.addWidget(self.pro1)
        self.pro2 = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pro2.sizePolicy().hasHeightForWidth())
        self.pro2.setSizePolicy(sizePolicy)
        self.pro2.setMinimum(-1000)
        self.pro2.setMaximum(1000)
        self.pro2.setProperty("value", -300)
        self.pro2.setObjectName("pro2")
        self.verticalLayout.addWidget(self.pro2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.grafomini = PlotWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grafomini.sizePolicy().hasHeightForWidth())
        self.grafomini.setSizePolicy(sizePolicy)
        self.grafomini.setObjectName("grafomini")
        self.horizontalLayout_2.addWidget(self.grafomini)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.grafo = PlotWidget(self.centralwidget)
        self.grafo.setObjectName("grafo")
        self.horizontalLayout_3.addWidget(self.grafo)
        self.grafomaxi = PlotWidget(self.centralwidget)
        self.grafomaxi.setObjectName("grafomaxi")
        self.horizontalLayout_3.addWidget(self.grafomaxi)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
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
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1055, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pro1.setFormat(_translate("MainWindow", "%v mV"))
        self.pro2.setFormat(_translate("MainWindow", "%v mV"))
        self.cmd.setItemText(0, _translate("MainWindow", "Z"))
        self.cmd.setItemText(1, _translate("MainWindow", "D"))
        self.cmd.setItemText(2, _translate("MainWindow", "P"))
        self.cmd.setItemText(3, _translate("MainWindow", "K"))
        self.cmd.setItemText(4, _translate("MainWindow", "s"))
        self.cmd.setItemText(5, _translate("MainWindow", "g"))
        self.butDo.setText(_translate("MainWindow", "GO"))

from pyqtgraph import PlotWidget