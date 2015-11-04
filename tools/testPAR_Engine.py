try:
    from PyQt5.QtWidgets import QApplication, QMainWindow
    from PyQt5 import QtCore
except:
    from PyQt4.QtGui import QApplication, QMainWindow
    from PyQt4 import QtCore


TIMEBASE = 20.0
TIMETIME = 50

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

import sys
import os

import numpy as np

from tools import testPAR_MainGUI as view
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

import epz.epz as epz
from tools.epzInterpreter import QtQuerist

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
        self.par = epz.CMD(ENV,tag = 'REQPAR')
        #self.parrec = epz.QtCMDREC(ENV,device=None,tag='SNDPAR')
        self.data = epz.QtDATA(ENV,device=None)
        self.data.chunk = 1000
        self.data.notifyLength = 100
        self.data.save = False
        self.data.notify = True

        self.querist = QtQuerist(ENV)
        self.setConnections()
        #self.parrec.start()
        self.data.start()

        self.xrange = [-10.0, 10.0]
        self.yrange = [-10.0, 10.0]
        self.zrange = [-10.0, 10.0]

        self.times = datetime.now()

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

        valbig = int((val-mn)/(mx-mn))
        try:
            mon.setValue(int(valbig))
            dial.setValue(valbig)
        except:
            pass
        led.display(val)

        self.show()

    def received(self,v):
        times = datetime.now()
        sets = ['x','y','z']
        self.times = times
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

    def parWasReceived(self,f):
        self.ui.parDisplay.display(float(f))

    def setConnections(self):
        self.data.chunkReceived.connect(self.received)
        self.data.xDataReceived.connect(self.xUpdate)
        self.data.yDataReceived.connect(self.yUpdate)
        self.data.zDataReceived.connect(self.zUpdate)
        self.ui.butDo.clicked.connect(self.sendCMD)
        self.ui.sendPAR.clicked.connect(self.sendPAR)
        self.querist.heardSomething.connect(self.parWasReceived)
        #self.parrec.respReceived.connect(self.parWasReceived)

        buttons = [self.ui.xmin,self.ui.xmax,self.ui.ymin,self.ui.ymax,self.ui.zmin,self.ui.zmax]
        for b in buttons:
            b.valueChanged.connect(self.setMinMax)

    def sendCMD(self):
        panelstrng = str(self.ui.cmd.currentText() )
        strng = panelstrng.partition(' ')[0]
        parameters = self.ui.cpar.toPlainText()

        print('Sending {0} with parameters {1}'.format(strng,parameters))

        if strng == 'KILL':
            self.data.goahead=False
        elif strng == 'SET_TIM8PER':
            TIMETIME = int(parameters)/TIMEBASE
            self.tmp=np.array([])
        self.cmd.send(strng,parameters)

    def sendPAR(self):
        panelstrng = str(self.ui.par.currentText())
        strng = panelstrng.partition(' ')[0]
        parameters = ' '
        queries = [self.querist.askDevice,self.querist.askAdcRange,self.querist.askAdcMin,
                   self.querist.askAdcMax,self.querist.askAdcResolution,self.querist.askAdcBufPresence,
                   self.querist.askAdcBufInMin,self.querist.askAdcBufInMax,self.querist.askAdcBufOutMin,
                   self.querist.askAdcBufOutMax,self.querist.askDacRef,self.querist.askDacPolarity]
        resp = queries[self.ui.par.currentIndex()]()
        print('Sending param command {0}'.format(strng))

        self.par.send(strng, parameters)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName( 'EPZ Monitor' )
    smfs = curveWindow()
    smfs.show()
    sys.exit(app.exec_())