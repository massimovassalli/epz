"""
EpsilonPi Fake Hardware for tests
"""

import zmq
import threading
import queue
import time
import numpy as np

import configparser
config = configparser.ConfigParser()
config.read('epz.ini')

EPSERVER = config['ZMQ']['EPSERVER']
SUBPORT = config['ZMQ']['SUBPORT']
PUBPORT = config['ZMQ']['PUBPORT']

CONTEXT = zmq.Context.instance()

from PyQt4.QtCore import pyqtSignal, QThread
#from PyQt5.QtCore import pyqtSignal, QThread

class QtMON(QThread):
    x_received = pyqtSignal(int, name='xdataReceived')
    y_received = pyqtSignal(int, name='ydataReceived')
    def __init__(self, device):
        super().__init__()
        self.device = device
        self.socket = None
        self.goahead = True
        self.log = False
        self.memory = False
        self.memlen = 1000
        self.x = []
        self.y = []

    def start(self):
        self.socket = CONTEXT.socket(zmq.SUB)
        self.head = "{0}:MON:".format(self.device)
        self.socket.setsockopt_string(zmq.SUBSCRIBE,self.head)
        self.socket.connect("tcp://{0}:{1}".format(EPSERVER, SUBPORT))
        return super().start()

    def actOnData(self,v):
        self.x_received.emit(int(v[1]*1000.0))
        self.y_received.emit(int(v[2]*1000.0))

        if self.memory:
            if len(self.x) == self.memlen:
                self.x.pop(0)
                self.y.pop(0)
            self.x.append(v[0])
            self.y.append(v[1])

    def run(self):
        while self.goahead:
            body = self.socket.recv_string()
            data = [float(x) for x in body.strip(self.head).split(':')]
            self.actOnData(data)
        print('Finishing monitor thread')

class QtDATA(QThread):
    chunkReceived = pyqtSignal(list, name='chunkReceived')
    def __init__(self, device):
        super().__init__()
        self.device = device
        self.socket = None
        self.goahead = True
        self.chunk = 10000
        self.x = []
        self.y = []
        self.t = []
        self.queue = queue.Queue()
        self. save = True
        self.notify = False

    def start(self):
        self.socket = CONTEXT.socket(zmq.SUB)
        self.head = "{0}:DATA:".format(self.device)
        self.socket.setsockopt_string(zmq.SUBSCRIBE,self.head)
        self.socket.connect("tcp://{0}:{1}".format(EPSERVER, SUBPORT))
        return super().start()

    def actOnData(self,v):
        self.chunkReceived.emit(v)

    def run(self):
        while self.goahead:
            body = self.socket.recv_string()
            data = [float(x) for x in body.strip(self.head).split(':')]
            if self.save:
                self.queue.put(data)
            if self.notify:
                self.t.append(data[0])
                self.x.append(data[1])
                self.y.append(data[2])
                if len(self.x) >= self.chunk:
                    self.actOnData([self.t,self.x,self.y])
                    self.x=[]
                    self.y=[]
                    self.t=[]
        print('Finishing data thread')