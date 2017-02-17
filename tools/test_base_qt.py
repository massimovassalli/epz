import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QApplication, QLabel)

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from core import qtCmdRec,cmd

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')

        self.p1 = QLabel('P1',self)
        self.p1.setFixedWidth(200)
        self.p1.move(30,50)
        self.epz = qtCmdRec.QtCMDREC()
        self.epz.respReceived.connect(self.p1.setText)
        self.epz.start()
        self.p1.setText('waiting ...')

        self.p2 = QLineEdit(self)
        self.p2.move(30,10)
        self.p3 = QPushButton('SEND',self)
        self.p3.move(150,10)
        self.p3.clicked.connect(self.send)
        self.cmd = cmd.CMD()

        self.show()

    def send(self):
        self.cmd.send(self.p2.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())