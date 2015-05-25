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
SERPORT = config['PIC']['SERPORT']
SPIPORT = config['PIC']['SPIPORT']

ACT = config['ACTIONS']

CONTEXT = zmq.Context.instance()

loop = True
def receive():
    global loop
    socket = CONTEXT.socket(zmq.REP)
    socket.bind("tcp://127.0.0.1:{0}".format(SERPORT))
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
        socket.send_string("OK")
def send():
    global loop
    ssock = CONTEXT.socket(zmq.PAIR)
    ssock.bind("tcp://127.0.0.1:{0}".format(SPIPORT))
    while loop:
        n = np.random.random()
        t = time.clock()
        msg = '{0}:{1}:{2}'.format(t,np.sin(2*np.pi*t/1.0)+n,np.cos(2*np.pi*t/1.0)+n)
        ssock.send_string(msg)

acpol = threading.Thread(target=receive)
acpol.daemon = False
acpol.start()
ac2 = threading.Thread(target=send)
ac2.daemon = False
ac2.start()

print('I\'m now producing ...')