"""
EpsilonPi Forwarder
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from core import epz

import zmq
import threading

class Forwarder(threading.Thread):
    def __init__(self):
        super(Forwarder, self).__init__()
        self.frontend = epz.ENV['context'].socket(zmq.SUB)
        self.backend = epz.ENV['context'].socket(zmq.PUB)
        self.subport = epz.ENV['subport']
        self.pubport = epz.ENV['pubport']
        self.daemon = False #Keep the forwarder alive

    def start(self):
        print ('Starting FW activity')
        print ('PORT for PUB {0} - PORT for SUB {1}'.format(self.pubport, self.subport))
        print ('-- ready --')
        self.frontend.bind("tcp://*:{0}".format(self.pubport))
        self.frontend.setsockopt_string(zmq.SUBSCRIBE, '')
        self.backend.bind("tcp://*:{0}".format(self.subport))
        return super(Forwarder, self).start()

    def run(self):
        zmq.device(zmq.FORWARDER, self.frontend, self.backend)

def start():
    f = Forwarder()
    f.start()

if __name__ == "__main__":
  start()