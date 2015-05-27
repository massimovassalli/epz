"""
EpsilonPi Fake Hardware for tests
"""

import zmq
import threading
import time
import numpy as np

import configparser
config = configparser.ConfigParser()
config.read('epz.ini')

EPSERVER = config['ZMQ']['EPSERVER']
SUBPORT = config['ZMQ']['SUBPORT']
PUBPORT = config['ZMQ']['PUBPORT']

CONTEXT = zmq.Context.instance()
DEVICE = 'EPIZMQ'

loop = True
def receive():
    global loop
    socket = CONTEXT.socket(zmq.SUB)
    socket.setsockopt_string(zmq.SUBSCRIBE,"{0}:CMD:".format(DEVICE))
    socket.connect("tcp://{0}:{1}".format(EPSERVER,SUBPORT))
    while loop:
        #  Wait for next request from client
        message = socket.recv()
        if message==b'KILL':
            print('FakeSerial: KILL signal received ...')
            time.sleep (1)
            socket.send_string("KO")
            loop = False
        else:
            print ("Received request: {0}".format(message))
        time.sleep (1)
def send():
    global loop
    global whe
    ssock = CONTEXT.socket(zmq.PUB)
    ssock.connect("tcp://{0}:{1}".format(EPSERVER,PUBPORT))

    i = 0
    j = 0
    while loop:
        i += 1
        j += 1
        n = np.random.random() / 10.0

        st = np.sin(2*np.pi*float(i)/10000.0)+n
        ct = np.cos(2*np.pi*float(i)/10000.0)-n
        if j >= 7000:
            msg = '{0}:MON:{1}:{2}'.format(DEVICE,st,ct)
            ssock.send_string(msg)
            j=0
        msg = '{0}:DATA:{1}:{2}'.format(DEVICE,st,ct)
        ssock.send_string(msg)

import forwarder as fw
f = fw.Forwarder()
f.start()

acpol = threading.Thread(target=receive)
acpol.daemon = False
acpol.start()

ac2 = threading.Thread(target=send)
ac2.daemon = False
ac2.start()

print('I\'m now producing ...')