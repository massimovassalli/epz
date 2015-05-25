"""
EpsilonPi Forwarder
"""

import zmq
import threading

import configparser
config = configparser.ConfigParser()
config.read('epz.ini')

EPSERVER = config['ZMQ']['EPSERVER']
SUBPORT = config['ZMQ']['SUBPORT']
PUBPORT = config['ZMQ']['PUBPORT']
ISFW = config.getboolean('ZMQ','FORWARDING')

CONTEXT = zmq.Context.instance()

class Forwarder(threading.Thread):
    def __init__(self):
        super(Forwarder, self).__init__()
        self.frontend = CONTEXT.socket(zmq.SUB)
        self.backend = CONTEXT.socket(zmq.PUB)
        self.subport = SUBPORT
        self.pubport = PUBPORT
        self.daemon = False #Keeps the forwarder alive

    def start(self):
        print ('Starting FW activity')
        print ('PORT for PUB {0} - PORT for SUB {1}'.format(PUBPORT, SUBPORT))
        print ('-- ready --')
        self.frontend.bind("tcp://*:{0}".format(PUBPORT))
        self.frontend.setsockopt_string(zmq.SUBSCRIBE, '')
        self.backend.bind("tcp://*:{0}".format(SUBPORT))
        return super(Forwarder, self).start()

    def run(self):
        zmq.device(zmq.FORWARDER, self.frontend, self.backend)

if __name__ == "__main__":
    f = Forwarder()
    f.start()