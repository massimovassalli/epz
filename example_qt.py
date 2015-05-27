import sys
from PyQt4.QtGui import QApplication, QMainWindow
from PyQt4 import QtCore

#from PyQt5.QtWidgets import QApplication, QMainWindow
#from PyQt5 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

import sys,os,time
import epz4_view as view
#import epz5_view as view
import numpy as np

import pyqtgraph as pg

import consumer as epz
import consumer_qt as epz_qt

import configparser
config = configparser.ConfigParser()
config.read('epz.ini')

EPSERVER = config['ZMQ']['EPSERVER']
SUBPORT = config['ZMQ']['SUBPORT']
PUBPORT = config['ZMQ']['PUBPORT']

DEVICE = 'EPIZMQ'

class curveWindow ( QMainWindow ):

    def __init__ ( self, parent = None ):
        super().__init__( parent )
        self.setWindowTitle( 'Qt4EP' )
        self.ui = view.Ui_MainWindow()
        self.ui.setupUi( self )

        self.mon = epz_qt.QtMON(DEVICE)
        self.mon.memory = True
        self.mon.memlen = 100
        self.cmd = epz.CMD(DEVICE)

        self.data = epz_qt.QtDATA(DEVICE)
        self.data.chunk = 9000
        self.data.save = False
        self.data.notify = True

        self.timer = QtCore.QTimer(self)

        self.setConnections()
        self.mon.start()
        self.data.start()
        self.timer.start(100)

    def plotmini(self):
        if len(self.mon.x)>=2:
            self.ui.grafomini.plotItem.clear()
            self.ui.grafomini.plotItem.plot(self.mon.x,self.mon.y)

    def plotmaxi(self,v):
        x = v[0]
        y = v[1]
        self.ui.grafomaxi.plotItem.clear()
        self.ui.grafomaxi.plotItem.plot(x,y)

    def plotTime(self,v):
        x = v[0]
        y = v[1]
        t = np.linspace(0,len(x)-1,len(x))
        self.ui.grafo.plotItem.clear()
        self.ui.grafo.plotItem.plot(t,x,pen='y')
        self.ui.grafo.plotItem.plot(t,y,pen='r')

    def setConnections(self):
        self.mon.x_received.connect(self.ui.pro1.setValue)
        self.mon.y_received.connect(self.ui.pro2.setValue)
        self.data.chunkReceived.connect(self.plotmaxi)
        self.data.chunkReceived.connect(self.plotTime)
        self.timer.timeout.connect(self.plotmini)
        self.ui.butDo.clicked.connect(self.sendCMD)

    def sendCMD(self):
        letter = str(self.ui.cmd.currentText() )
        parameters = self.ui.cpar.toPlainText()
        if letter == 'K':
            self.data.goahead=False
        self.cmd.send(letter,parameters)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName( 'Qt4EP' )
    smfs = curveWindow()
    smfs.show()
    sys.exit(app.exec_())