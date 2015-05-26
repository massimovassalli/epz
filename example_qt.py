import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

import sys,os,time
import epz_view as view
import numpy as np

import consumer as epz

epz.EPSERVER = '192.168.0.108'
#epz.EPSERVER = '127.0.0.1'


class curveWindow ( QMainWindow ):

    def __init__ ( self, parent = None ):
        super().__init__( parent )
        self.setWindowTitle( 'Qt4EP' )
        self.ui = view.Ui_MainWindow()
        self.ui.setupUi( self )
        self.data = epz.QtMON('EPIZMQ')

        self.setConnections()
        self.data.start()

        #self.ora = QtCore.QTimer()
        #QtCore.QObject.connect(self.ora, QtCore.SIGNAL(_fromUtf8("timeout()")), self.refresh)
        #self.ora.start(100)
        #self.n = 0

    def setConnections(self):
        #self.ui.okButton.clicked.connect(self.accept)
        #self.ui.cancelButton.clicked.connect(self.reject)

        self.data.x_received.connect(self.ui.pro1.setValue)
        self.data.y_received.connect(self.ui.pro2.setValue)

#        clickable=[self.ui.g_time,self.ui.g_hist,self.ui.g_freq]
#        editable =[]
#        for o in clickable:
#                QtCore.QObject.connect(o, QtCore.SIGNAL(_fromUtf8("clicked()")), self.manageView)
#        for o in editable:
#            QtCore.QObject.connect(o, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.updateCurve)#
#
#        QtCore.QObject.connect(self.ui.bRun, QtCore.SIGNAL(_fromUtf8("clicked()")), self.startCurve)#
#
#        QtCore.QMetaObject.connectSlotsByName(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName( 'Qt4EP' )
    smfs = curveWindow()
    smfs.show()
    sys.exit(app.exec_())