from PyQt4.QtGui import QApplication, QMainWindow
from PyQt4 import QtCore

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

import sys,os,time
import monitor_view as view
import numpy as np
import pyqtgraph as pg
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from epz import epz

fconf = 'test.conf'
if len(sys.argv) == 2:
    fconf = sys.argv[1]
ENV = epz.Environment(fconf)


class curveWindow ( QMainWindow ):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('EPZ Monitor')
        self.ui = view.Ui_MainWindow()
        self.ui.setupUi(self)

        self.cmd = epz.CMD(ENV)
        self.data = epz.QtDATA(ENV)
        self.data.chunk = 1000
        self.data.notifyLength = 100
        self.data.save = False
        self.data.notify = True

        self.setConnections()
        self.data.start()

        self.xrange = [-10.0, 10.0]
        self.yrange = [-10.0, 10.0]
        self.zrange = [-10.0, 10.0]

        for grafo in [self.ui.xgrafo, self.ui.ygrafo, self.ui.zgrafo]:
            grafo.plotItem.clear()

    def plot(self,signal,v):
        grafos = {'x':self.ui.xgrafo, 'y':self.ui.ygrafo, 'z':self.ui.zgrafo}
        grafo = grafos[signal]
        grafo.plotItem.clear()
        x = range(len(v))
        grafo.plotItem.plot(x,v)

    def look(self,signal,val):
        mons = {'x':self.ui.xmon, 'y':self.ui.ymon,'z':self.ui.zmon}
        dials = {'x':self.ui.xdial, 'y':self.ui.ydial,'z':self.ui.zdial}
        rngs = {'x':self.xrange, 'y':self.yrange,'z':self.zrange}
        leds = {'x':self.ui.xled,'y':self.ui.yled,'z':self.ui.zled}

        mon = mons[signal]
        dial = dials[signal]
        mn,mx = rngs[signal]
        led = leds[signal]

        valbig = 10000 * (val-mn)/(mx-mn)

        mon.setValue(valbig)
        dial.setValue(valbig)
        led.display(val)

        self.show()

    def received(self,v):
        sets = ['x','y','z']

        for i in range(3):
            self.plot(sets[i],v[i])

    def xUpdate(self,val):
        self.look('x',val)

    def yUpdate(self,val):
        self.look('y',val)

    def zUpdate(self,val):
        self.look('z',val)

    def setMinMax(self):
        self.xrange[0] = float(self.ui.xmin.value())
        self.xrange[1] = float(self.ui.xmax.value())
        self.yrange[0] = float(self.ui.ymin.value())
        self.yrange[1] = float(self.ui.ymax.value())
        self.zrange[0] = float(self.ui.zmin.value())
        self.zrange[1] = float(self.ui.zmax.value())

    def setConnections(self):
        self.data.chunkReceived.connect(self.received)
        self.data.xDataReceived.connect(self.xUpdate)
        self.data.yDataReceived.connect(self.yUpdate)
        self.data.zDataReceived.connect(self.zUpdate)
        self.ui.butDo.clicked.connect(self.sendCMD)

        buttons = [self.ui.xmin,self.ui.xmax,self.ui.ymin,self.ui.ymax,self.ui.zmin,self.ui.zmax]
        for b in buttons:
            b.valueChanged.connect(self.setMinMax)

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
    app.setApplicationName( 'EPZ Monitor' )
    smfs = curveWindow()
    smfs.show()
    sys.exit(app.exec_())