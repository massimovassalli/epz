from PyQt4.QtGui import QApplication, QMainWindow
from PyQt4 import QtCore

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

# import sys,os,time

import speedtest_view as view
import numpy as np
# import pyqtgraph as pg
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from epz import epz

fconf = 'test.conf'
if len(sys.argv) == 2:
    fconf = sys.argv[1]
ENV = epz.Environment(fconf)

TIMEBASE = 20.0
TIMETIME = 50


class curveWindow ( QMainWindow ):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('SpeedTest')
        self.ui = view.Ui_MainWindow()
        self.ui.setupUi(self)

        self.cmd = epz.CMD(ENV)
        self.data = epz.QtDATA(ENV)
        self.data.chunk = 1000
        self.data.save = False
        self.data.notify = True

        self.setConnections()
        self.data.start()

        self.tmp = np.array([])
        self.speed = []
        self.ui.grafo.plotItem.clear()
        self.ui.grafo.plotItem.plot([],[],symbolPen='y',symbol='o',symbolSize=4)

    def plotmini(self):
        if len(self.tmp) >= 2:
            dat,xx = np.histogram(self.tmp*TIMEBASE,100,(0,20000))
            xxx = (xx[0:-1]+xx[1:])/2.0
            xxx = xx[0:-1]
            #self.ui.grafomini.setXRange(TIMEBASE,TIMEBASE*1000)
            self.ui.grafomini.plotItem.clear()
            self.ui.grafomini.plotItem.plot(xxx,100.0*dat/max(dat),symbolPen='g',symbol='o',symbolSize=4)

    def plotmaxi(self):
        if len(self.tmp) >= 2:
            dat,xx = np.histogram(self.tmp*TIMEBASE,100,(0,2000))
            xxx = (xx[0:-1]+xx[1:])/2.0
            xxx = xx[0:-1]
            #self.ui.grafomini.setXRange(TIMEBASE,TIMEBASE*1000)
            self.ui.grafomaxi.plotItem.clear()
            if max(dat) > 0:
                self.ui.grafomaxi.plotItem.plot(xxx,100.0*dat/max(dat),symbolPen='g',symbol='o',symbolSize=4)

    def plotTime(self):
        self.ui.grafo.plotItem.curves[0].setData(self.speed)

    def statusLED(self,state):
        if state:
            self.ui.sLED.setStyleSheet('background-color: green;')
            self.ui.sLED.setText('ON')
        else:
            self.ui.sLED.setStyleSheet('background-color: gray;')
            self.ui.sLED.setText('OFF')

    def intLED(self,state):
        if state:
            self.ui.sINT.setStyleSheet('background-color: red;')
            self.ui.sINT.setText('KO')
        else:
            self.ui.sINT.setStyleSheet('background-color: green;')
            self.ui.sINT.setText('OK')

    def packetreceived(self,v):

        tt = np.array(v[0])
        dt = tt[1:]-tt[0:-1]

        ttransfer = TIMEBASE*(tt[-1]-tt[0])/(float(len(tt)))
        mini = min(dt)
        maxi = max(dt)
        ma = 0

        self.tmp = np.concatenate([self.tmp,dt])
        sp = 1000.0 * float(len(tt)) / ( (tt[-1]-tt[0]) * TIMEBASE)
        self.speed.append(sp)
        self.ui.lcd1.display(sp)
        self.ui.lcd4.display(maxi/TIMETIME)
        self.ui.lcd5.display(maxi*TIMEBASE)
        self.ui.lcd2.display(mini/TIMETIME)
        self.ui.lcd3.display(mini*TIMEBASE)

        dat,xx = np.histogram(dt*TIMEBASE,100,(0,20000))
        xxx = (xx[0:-1]+xx[1:])/2.0
        xxx = xx[0:-1]
        ma = xxx[np.argmax(dat)]

        self.ui.lcd6.display(ma)

        self.plotmini()
        self.plotmaxi()
        self.plotTime()

    def setConnections(self):
        self.data.chunkReceived.connect(self.packetreceived)
        self.ui.butDo.clicked.connect(self.sendCMD)
        self.data.stateChanged.connect(self.statusLED)
        self.data.overloadChanged.connect(self.intLED)

    def sendCMD(self):
        letter = str(self.ui.cmd.currentText() )
        parameters = self.ui.cpar.toPlainText()
        print('Sending {0} with parameters {1}'.format(letter,parameters))

        if letter == 'K':
            self.data.goahead=False
        elif letter=='8':
            TIMETIME = int(parameters)/TIMEBASE
            self.tmp = np.array([])
        elif letter=='R':
            self.tmp = np.array([])

        self.cmd.send(letter,parameters)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName( 'Qt4EP' )
    smfs = curveWindow()
    smfs.show()
    sys.exit(app.exec_())