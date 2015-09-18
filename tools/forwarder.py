"""
EpsilonPi Forwarder
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from epz import epz
ENV = epz.Environment('epz.conf')

import zmq
import threading

class Forwarder(threading.Thread):
    def __init__(self):
        super(Forwarder, self).__init__()
        self.frontend = ENV.context.socket(zmq.SUB)
        self.backend = ENV.context.socket(zmq.PUB)
        self.subport = ENV.subport
        self.pubport = ENV.pubport
        self.daemon = False #Keeps the forwarder alive

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

if __name__ == "__main__":
    import sys
    fconf = 'test.conf'
    if len(sys.argv) == 2:
        fconf = sys.argv[1]
    ENV = epz.Environment(fconf)
    f = Forwarder()
    f.start()