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
        self.mon.memlen = 20

        self.cmd = epz.CMD(DEVICE)

        self.data = epz_qt.QtDATA(DEVICE)
        self.data.chunk = 1000
        self.data.save = False
        self.data.notify = True

        self.timer = QtCore.QTimer(self)

        self.setConnections()
        self.mon.start()
        self.data.start()
        #self.timer.start(100)

        self.tmp = np.array([  ])

    def plotmini(self):
        if len(self.mon.x)>=2:
#            self.ui.grafomini.plotItem.clear()
#            self.ui.grafomini.plotItem.plot(self.mon.x,self.mon.y)
            x = self.mon.x
            y = self.mon.y
            tx = np.linspace(0,len(x)-1,len(x))
            ty = np.linspace(0,len(y)-1,len(y))
            self.ui.grafomini.plotItem.clear()
            self.ui.grafomini.plotItem.plot(tx,x,pen='y')
            self.ui.grafomini.plotItem.plot(ty,y,pen='r')

    def plotmaxi(self,v):
        x = v[1]
        y = v[2]
        self.ui.grafomaxi.plotItem.clear()
        self.ui.grafomaxi.plotItem.plot(x,y)

    def plotTime(self,v):
        t = v[0]
        x = v[1]
        y = v[2]

        self.ui.grafo.plotItem.clear()
        self.ui.grafo.plotItem.plot(t,y,symbolPen='y',symbol='o',symbolSize=4)
        self.ui.grafomaxi.plotItem.clear()
        self.ui.grafomaxi.plotItem.plot(np.linspace(0,len(t),len(t)),t,symbolPen='r',symbol='o',symbolSize=4)
        #self.ui.grafo.plotItem.plot(np.linspace(0,len(y),len(y)),np.array(y)*1000.0,symbolPen='g',symbol='o',symbolSize=4)

        tt = np.array(t)

        dt = tt[1:]-tt[0:-1]

        dtime = 20

        ttransfer = dtime*(tt[-1]-tt[0])/(float(len(tt)))
        mini = min(dt)
        maxi = max(dt)
        ma = 0

        self.tmp = np.concatenate([self.tmp,dt])

        howmany = max(self.tmp)-min(self.tmp)
        if howmany > 0:
            dat,xx = np.histogram(self.tmp*dtime,100,(20,4000))
            xxx = (xx[0:-1]+xx[1:])/2.0
            xxx = xx[0:-1]
            ma = xxx[np.argmax(dat)]
            self.ui.grafomini.plotItem.clear()
            self.ui.grafomini.plotItem.plot(xxx,dat,symbolPen='g',symbol='o',symbolSize=4)

        print('Now: Transfer {4}kHz - Max dt: {0}={1}us [best: {5}us] - Min dt {2}={3}us'.format(maxi,maxi*dtime,mini,mini*dtime,1000.0/ttransfer,ma))


    def setConnections(self):
        self.mon.x_received.connect(self.ui.pro1.setValue)
        self.mon.y_received.connect(self.ui.pro2.setValue)
        #self.data.chunkReceived.connect(self.plotmaxi)
        self.data.chunkReceived.connect(self.plotTime)
        self.timer.timeout.connect(self.plotmini)
        self.ui.butDo.clicked.connect(self.sendCMD)

    def sendCMD(self):
        letter = str(self.ui.cmd.currentText() )
        parameters = self.ui.cpar.toPlainText()

        print('Sending {0} with parameters {1}'.format(letter,parameters))

        if letter == 'K':
            self.data.goahead=False
        elif letter == '8':
            self.tmp=np.array([])
        self.cmd.send(letter,parameters)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName( 'Qt4EP' )
    smfs = curveWindow()
    smfs.show()
    sys.exit(app.exec_())