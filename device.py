"""
EpsilonPi Device
"""

import zmq
import threading
import time

import configparser
config = configparser.ConfigParser()
config.read('epz.ini')

EPSERVER = config['ZMQ']['EPSERVER']
SUBPORT = config['ZMQ']['SUBPORT']
PUBPORT = config['ZMQ']['PUBPORT']
SERPORT = config['PIC']['SERPORT']
SPIPORT = config['PIC']['SPIPORT']
ISFW = config.getboolean('ZMQ','FORWARDING')

ACT = config['ACTIONS']

CONTEXT = zmq.Context.instance()

class state(threading.Thread):
    def __init__(self,name,device=None):
        super(state, self).__init__()
        self.statename = name
        self.goahead = True
        self.device = device
        self.fire = threading.Event()
        self.socket = CONTEXT.socket(zmq.PUB)
        self.socket.connect("tcp://{0}:{1}".format(EPSERVER,PUBPORT))
        self.value = None

    def set(self):
        v = self.value
        if type(v) != list:
            v = [v]
        msg = '{0}:STATE:{1}:{2}'.format(self.device,self.statename,v[0])
        for par in v[1:]:
            msg = msg + ':' + str(par)
        self.socket.send_string(msg)

    def run(self):
        while self.goahead:
            self.fire.wait()
            self.set()
            self.fire.clear()
        print ('Exiting state {0}'.self.statename)

class action(object):
    def __init__(self,command='setValue',letter='M',npars=0):
        self.letter = letter
        self.command = command
        self.npars = npars
        self.changeState = False #set to True to let call stateChanged

    def convert(self,v):
        o=[]
        for vx in v:
            o.append(int(vx))

    def getMessage(self,p):
        m = self.letter
        p = self.convert(p)
        for px in p:
            m = m + ':' + str(p)
        return m

    def stateChanged(self):
        return 'statename',['newvalue1','newvalue2']

class Device(object):
    def __init__(self,name):
        self.daemon = True
        self.name = name
        self.goahead = True
        self.now = 0
        self.stattime = 10000 # in seconds
        self.streaming = False
        self.states = {'t':state('t',self.name),'dac':state('dac',self.name),'adc':state('adc',self.name)}
        self.datastates = ['t','dac','adc']
        self.actions={}
        for ac in ACT:
            letter = ac
            command,npars = ACT[letter].split(',')
            self.actions[command]=action(command,letter,int(npars))

    def poller(self):
        self.spisocket = CONTEXT.socket(zmq.PAIR)
        #self.spisocket.setsockopt_string(zmq.SUBSCRIBE,"")
        self.spisocket.connect("tcp://{0}:{1}".format('127.0.0.1',SPIPORT))
        while self.goahead:
            body = self.spisocket.recv_string()
            istime = ( self.now >= self.stattime )
            self.now += 1
            if istime or self.streaming:
                dat = body.split(':')
                if istime:
                    self.now=0
                    i=0
                    for nm in self.datastates:
                        self.states[nm].value = dat[i]
                        self.states[nm].fire.set()
                        i+=1
                if self.streaming:
                    pass
        print('Data manager from device {0} shutting down ...'.format(self.name))

    def action(self):
        self.subsocket = CONTEXT.socket(zmq.SUB)
        self.subsocket.setsockopt_string(zmq.SUBSCRIBE,"{0}:ACTION:".format(self.name))
        self.subsocket.connect("tcp://{0}:{1}".format(EPSERVER,SUBPORT))
        self.sersocket = CONTEXT.socket(zmq.REQ)
        self.sersocket.connect("tcp://{0}:{1}".format('127.0.0.1',SERPORT))
        while self.goahead:
            body = self.subsocket.recv_string()
            parse = body.split(':')
            command = parse[1]
            params=[]
            if len(parse) > 2:
                params = parse[2:]

            if command == 'KILL':
                self.goahead = False
                for s in self.states:
                    s.goahead = False
                print('{0}: KILL signal received ...'.format(self.name))
                self.sersocket.send_string ('KILL')
                notify = self.sersocket.recv()
            elif command == 'DECIMATE':
                self.stattime = int(float(params[0]))
            elif command in self.actions:
                msg = self.actions[command].getMessage(params)
                self.sersocket.send_sting (msg)
                notify = self.sersocket.recv()
                if notify == 'OK':
                    if self.actions[command].changeState:
                        nm,v = self.actions[command].stateChanged()
                        self.states[nm].set(v)
                else:
                    print('Unmanaged error updating PIC on action {0}'.format(self.command))
            else:
                print('Error accessing device: requested command {0} was not found'.format(command))

        print('Action getter from device {0} shutting down ...'.format(self.name))

    def start(self):
        for s in self.states:
            self.states[s].start()

        acpol = threading.Thread(target=self.poller)
        acpol.daemon = False
        acpol.start()

        acman = threading.Thread(target=self.action)
        acman.daemon = False
        acman.start()

if __name__ == "__main__":
    f = Device('TEST')
    f.start()
    print('Device TEST running')