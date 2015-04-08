"""
EpsilonPi main communication library
"""
import time
import zmq
import threading
import queue

# IP address of the FW engine
EPSERVER = '127.0.0.1'
# SUBPORT = the port to which clients will subscribe
SUBPORT = 5000
# PUBPORT = the port to which clients will publish
PUBPORT = 5010
CONTEXT = zmq.Context.instance()


def killdevice(devicename):
    n = Parameter(devicename, 'KILL')
    n.start()
    time.sleep(2)
    n.query()


class Consumer(threading.Thread):
    def __init__(self, devicename, parname):
        super(Consumer, self).__init__()
        self.parname = parname
        self.devicename = devicename
        self.pubsocket = CONTEXT.socket(zmq.PUB)
        self.subsocket = CONTEXT.socket(zmq.SUB)
        self.fwserver = EPSERVER
        self.subport = SUBPORT
        self.pubport = PUBPORT
        self._val = None
        self.daemon = True
        self.queue = queue.Queue()

    def start(self):
        self.pubsocket.connect("tcp://{0}:{1}".format(self.fwserver, self.pubport))
        self.subsocket.connect("tcp://{0}:{1}".format(self.fwserver, self.subport))
        self.subsocket.setsockopt_string(zmq.SUBSCRIBE, "{0}:{1}".format(self.devicename, self.parname))
        return super(Consumer, self).start()

    def get_val(self):
        return self._val

    def set_val(self, val):
        message = "{0}:{1}:{2}".format(self.devicename, self.parname, val)
        self.pubsocket.send_string(message)

    def query(self):
        message = "{0}:{1}:{2}".format(self.devicename, self.parname, '*')
        self.pubsocket.send_string(message)
    value = property(get_val, set_val)


class Parameter(Consumer):
    def run(self):
        while True:
            body = self.subsocket.recv_string()
            dev, par, val = body.split(':')
            if val != '*':
                self._val = val


class EnQueuer(Consumer):
    def run(self):
        while True:
            body = self.subsocket.recv_string()
            dev, par, val = body.split(':')
            if val != '*':
                val = float(val)
                self.queue.put(val)


class Signal(Parameter):
    def start(self):
        self.data = EnQueuer(self.devicename, self.parname + '_data')
        self.queue = self.data.queue
        self.data.start()
        return super(Signal, self).start()


class Forwarder(threading.Thread):
    def __init__(self):
        super(Forwarder, self).__init__()
        self.frontend = CONTEXT.socket(zmq.SUB)
        self.backend = CONTEXT.socket(zmq.PUB)
        self.subport = SUBPORT
        self.pubport = PUBPORT
        self.daemon = False
        
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


class Producer(threading.Thread):
    def __init__(self,hwname,value=None):
        self.hwname = hwname
        self.device = None
        self.goahead = True
        self.signal = False
        self.qlen = 0
        if value is not None:
            self.value = value
            if type(value)==type(12):
                self.type = lambda x: int(float(x))
            else:
                self.type = type(value)

    def update(self,v):
        if self.signal:
            return True
        if v > 100.0: #wrong range
            return False
        return True

    def getmessage(self,val=None):
        if val is None:
            return "{0}:{1}:{2}".format(self.device.devname, self.hwname, self.value)
        else:
            return "{0}:{1}:{2}".format(self.device.devname, self.hwname, val)

    def subscribe(self,socket):
        socket.setsockopt_string(zmq.SUBSCRIBE,"{0}:{1}".format(self.device.devname,self.hwname))

    def start(self):
        self.queue = queue.Queue(self.qlen)
        self.pubsocket = CONTEXT.socket(zmq.PUB)
        self.pubsocket.connect("tcp://{0}:{1}".format(self.device.fwserver, self.device.pubport))
        acq = threading.Thread(target=self.acquire)
        acq.start()
        return super(Hardware, self).start()

    def run(self):
        while self.goahead:
            val = self.queue.get()
            message = self.getMessage(val)
            self.pubsocket.send_string( message )


class HWparameter(Producer):
    def start(self,socket):
        self.subscribe(socket)

    def update(self,v):
        if v > 100.0: #wrong range
            return False
        return True


class HWsignal(Producer):
    def start(self,socket):
        self.subscribe(socket)

        self.queue = queue.Queue(self.qlen)
        self.pubsocket = CONTEXT.socket(zmq.PUB)
        self.pubsocket.connect("tcp://{0}:{1}".format(self.device.fwserver, self.device.pubport))
        acq = threading.Thread(target=self.acquire)
        acq.start()
        return super(HWsignal, self).start()

    def update(self,v):
        if v == 1:
            self.on = True
        else:
            self.on = False
        return True

    def acquire(self):
        import numpy.random as npr
        while self.goahead:
            if self.on:
                n = npr.random()
                self.queue.put(n)
                time.sleep(1.0)

    def run(self):
        while self.goahead:
            if self.on:
                val = self.queue.get()
                message = "{0}:{1}:{2}".format(self.device.devname, self.hwname + "_data", val)
                self.pubsocket.send_string (message)


class Device(threading.Thread):
    def __init__(self,devname):
        super(Device, self).__init__()
        self.pubsocket = CONTEXT.socket(zmq.PUB)
        self.subsocket = CONTEXT.socket(zmq.SUB)
        self.fwserver = EPSERVER
        self.subport = SUBPORT
        self.pubport = PUBPORT
        self.devname = devname
        self.hw = {}
        self.debug = True
        self.daemon = True        
        self.tsleep=0.1
        self.goahead = True
        self.pubsocket.connect("tcp://{0}:{1}".format(self.fwserver,self.pubport))
        self.subsocket.connect("tcp://{0}:{1}".format(self.fwserver,self.subport))

        self.subsocket.setsockopt_string(zmq.SUBSCRIBE,"{0}:{1}".format(self.devname,'KILL'))

    def shutdown(self):
        for p in self.hw:
            self.hw[p].goahead = False
        self.goahead = False

    def append(self,p):
        p.device = self
        p.start(self.subsocket)
        self.hw[p.hwname]=p

    def run(self):
        while self.goahead:
            body = self.subsocket.recv_string()
            dev, par, val = body.split(':')
            if par in self.hw.keys():
                p = self.hw[par]
                if val != '*':
                    valtogive = p.type(val)
                    if valtogive != p.value:
                        execupdate = p.update(valtogive) 
                        if execupdate:
                            p.value=valtogive
                            if valtogive != val:
                                message = p.getmessage()
                                self.pubsocket.send_string( message )
                        else:
                            message = p.getmessage()
                            self.pubsocket.send_string( message )
                else:
                    message = p.getmessage()
                    self.pubsocket.send_string( message )
            elif par == 'KILL':
                print('{0}: KILL signal received ...'.format(self.name))
                self.shutdown()
