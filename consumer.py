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

class CMD(object):
    def __init__(self, name):
        self.device = name
        self.socket = CONTEXT.socket(zmq.PUB)
        self.socket.connect("tcp://{0}:{1}".format(EPSERVER, PUBPORT))

    def send(self, cmd, values=[]):
        msg = '{0}:CMD:{1}'.format(self.device, cmd)
        if type(values) != list :
            values=[values]
        for v in values:
            msg = msg + ':' + str(v)
        self.socket.send_string(msg)

class MON(threading.Thread):
    def __init__(self, device):
        super().__init__()
        self.device = device
        self.socket = None
        self.goahead = True
        self.log = False

    def start(self):
        self.socket = CONTEXT.socket(zmq.SUB)
        self.head = "{0}:MON:".format(self.device)
        self.socket.setsockopt_string(zmq.SUBSCRIBE,self.head)
        self.socket.connect("tcp://{0}:{1}".format(EPSERVER, SUBPORT))
        return super().start()

    def actOnData(self,v):
        pass

    def run(self):
        while self.goahead:
            body = self.socket.recv_string()
            data = [float(x) for x in body.strip(self.head).split(':')]
            if self.log:
                print ('Data {0} received and converted'.format(data))
            self.actOnData(data)
        print('Finishing monitor thread')

class DATA(threading.Thread):
    def __init__(self, device):
        super().__init__()
        self.device = device
        self.socket = None
        self.goahead = True
        self.queue = queue.Queue

    def start(self):
        self.socket = CONTEXT.socket(zmq.SUB)
        self.head = "{0}:DATA:".format(self.device)
        self.socket.setsockopt_string(zmq.SUBSCRIBE,self.head)
        self.socket.connect("tcp://{0}:{1}".format(EPSERVER, SUBPORT))
        return super().start()

    def actOnData(self,v):
        pass

    def run(self):
        while self.goahead:
            body = self.socket.recv_string()
            data = [float(x) for x in body.strip(self.head).split(':')]
            self.queue.put(data)
        print('Finishing monitor thread')