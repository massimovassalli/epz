"""
EpsilonPi Device
"""

import zmq
import time
import numpy as np

import configparser
config = configparser.ConfigParser()
config.read('epz.ini')

EPSERVER = config['ZMQ']['EPSERVER']
SUBPORT = config['ZMQ']['SUBPORT']
PUBPORT = config['ZMQ']['PUBPORT']

DEVICE = 'EPIZMQ'

CONTEXT = zmq.Context.instance()

#psocket = CONTEXT.socket(zmq.PAIR)
#psocket.connect("tcp://{0}:{1}".format(EPSERVER,SPIPORT))

loop = True
log = False

import consumer

class myDat (consumer.DATA):

    def __init__(self, device):
        super().__init__(device)
        self.mon = False
        self.chunk = 1000

    def actOnData(self):
        t = []

        hm = min(self.chunk,self.queue.qsize())
        while hm < self.chunk:
            hm = min(self.chunk,self.queue.qsize())
            time.sleep(1)


        for i in range(self.chunk):
            t.append(self.queue.get()[0])
        t = np.array(t)
        dt = t[1:]-t[0:-1]

        mini = np.min(dt)
        maxi = np.max(dt)
        freq = 1000.0*len(t)/(t[-1]-t[0])
        tottime = int((t[-1]-t[0])/1000.0)

        print ('Time: {3}ms MIN: {0}us -- MAX: {1}us -- Effective F {2}kHz'.format(mini,maxi,freq,tottime) )

        if self.mon:
            self.actOnData()

dat = myDat(DEVICE)
cmd = consumer.CMD(DEVICE)

dat.start()

while loop:
    message = input("Give me the command:parameter string to be sent to the TEST device:")
    if message == 'K':
        loop = False
        dat.goahead = False
        cmd.send('K')
    elif message == 'LOG':
        if log:
            log=False
        else:
            log=True
    elif message == 'do':
        dat.mon=True
        dat.actOnData()

    msg = '{0}:{1}:{2}'.format('TEST','ACTION',message)

