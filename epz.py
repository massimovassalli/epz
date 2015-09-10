import zmq
import threading
import queue


class Conf(object):

    def __init__(self, fname=None):
        self.fname = fname
        self.defname = '/opt/epz.conf'
        self.data={}
        if self.fname is not None:
            self.parse()

    def parse(self):
        if self.fname is None:
            f = open(self.defname,'r')
        else:
            f = open(self.fname, 'r')
        for line in f:
            pre, post = line.split(':')
            self.data[pre] = post.rstrip('\r\n')
        f.close()

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= len(self.data)-1:
            result = self.data[list(self.data.keys())[self.n]]
            self.n += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, item):
        if item in self.data.keys():
            return self.data[item]
        else:
            try:
                w = int(item)
                return self.data[list(self.data.keys())[w]]
            except:
                raise(KeyError)


class Environment(object):

    def __init__(self, fname=None):
        self.context = zmq.Context.instance()
        self.pubport = None
        self.subport = None
        self.device = None
        self.epserver = None
        self.configure(fname)

    def configure(self, fname=None):
        if fname is not None:
            c = Conf(fname)
            self.epserver = c['EPSERVER']
            self.pubport = c['PUBPORT']
            self.subport = c['SUBPORT']
            self.device = c['THISDEVICE']


class CMD(object):
    def __init__(self, environment, device = None):
        self.context = environment.context
        self.pubport = environment.pubport
        self.epserver = environment.epserver
        if device is None:
            self.device = environment.device
        else:
            self.device = device

        self.command = 'CMD'
        self.socket = self.context.socket(zmq.PUB)
        self.socket.connect("tcp://{0}:{1}".format(environment.epserver, self.pubport))

    def send(self, cmd, values=[]):
        msg = '{0}:{2}:{1}'.format(self.device, cmd, self.command)
        if type(values) != list :
            values = [values]
        for v in values:
            msg = msg + ':' + str(v)
        self.socket.send_string(msg)


class SkelCMDREC(object):
    def __init__(self, environment):
        self.context = environment.context
        self.subport = environment.subport
        self.epserver = environment.epserver
        self.tag = 'RES'
        self.listen = True
        self.device = environment.device
        

    def setZmq(self):
        
        self.socket = self.context.socket(zmq.SUB)
        self.head = "{0}:{1}:".format(self.device,self.tag)
        self.socket.setsockopt_string(zmq.SUBSCRIBE,self.head)
        self.socket.connect("tcp://{0}:{1}".format(self.epserver, self.subport))
        
        
    def react(self,resp):
        pass
        
        
    def run(self):
        self.setZmq()
        
        while self.listen:
            body = self.socket.recv_string()
            resp = body.strip(self.head)
            self.react(resp)


class Skeldata(object):

    def __init__(self, environment, device=None):
        self.context = environment.context
        self.subport = environment.subport
        self.epserver = environment.epserver
        if device is None:
            self.device = environment.device
        else:
            self.device = device
        self.socket = None
        self.goahead = True
        self.decimate = 1
        self.chunk = 10000
        self.notifyLength = 1000
        self.tick = self.notifyLength
        self.x = []
        self.y = []
        self.z = []
        self.queue = []
        self.queue.append(queue.Queue())
        self._save = False
        self._overload = False
        self.notify = False
        self.head = ''

    @property
    def save(self):
        return self._save

    @save.setter
    def save(self, value):
        if self._save is not value:
            if not value:
                self.queue.append(queue.Queue())
            self.switchState(value)
        self._save = value

    @property
    def overload(self):
        return self._overload

    @overload.setter
    def overload(self, value):
        if self._overload is not value:
            self.switchLoad(value)
        self._overload = value

    def setzmq(self):
        self.socket = self.context.socket(zmq.SUB)
        self.head = "{0}:DATA:".format(self.device)
        self.socket.setsockopt_string(zmq.SUBSCRIBE,self.head)
        self.socket.connect("tcp://{0}:{1}".format(self.epserver, self.subport))

    def actondata(self,v):
        pass

    def actOnValue(self):
        pass

    def switchState(self,state):
        pass

    def switchLoad(self,state):
        pass

    def run(self):
        self.setzmq()
        print('DATA channel on {0} starting to receive'.format(self.device))
        while self.goahead:
            body = self.socket.recv_string()
            data = [float(x) for x in body.strip(self.head).split(':')]
            if data[3] == 1.0:
                self.save = True
            else:
                self.save = False

            if data[4] == 1.0:
                self.overload = True
            else:
                self.overload = False

            if self.save:
                self.queue[-1].put(data)

            self.tick -= 1
            if self.tick == 0:
                self.actOnValue(data)
                self.tick = self.notifyLength

            if self.notify:
                self.x.append(data[0])
                self.y.append(data[1])
                self.z.append(data[2])
                if len(self.x) >= self.chunk:
                    self.actondata([self.x[::self.decimate], self.y[::self.decimate], self.z[::self.decimate]])
                    self.x=[]
                    self.y=[]
                    self.z=[]
        print('Finishing data thread')


class DATA(Skeldata, threading.Thread):
    def __init__(self,environment):
        threading.Thread.__init__(self)
        Skeldata.__init__(self, environment)
        

class CMDREC(SkelCMDREC,threading.Thread):
    
    def __init__(self,environment):
        
        threading.Thread.__init__(self)
        SkelCMDREC.__init__(self, environment)        


try:
    from PyQt4.QtCore import pyqtSignal, QThread


    class QtDATA(Skeldata, QThread):
        chunkReceived = pyqtSignal(list, name='chunkReceived')
        xDataReceived = pyqtSignal(float, name='xDataReceived')
        yDataReceived = pyqtSignal(float, name='yDataReceived')
        zDataReceived = pyqtSignal(float, name='zDataReceived')
        stateChanged = pyqtSignal(bool, name='stateChanged')
        overloadChanged = pyqtSignal(bool, name='overloadChanged')

        def actOnValue(self,data):
            self.xDataReceived.emit(data[0])
            self.yDataReceived.emit(data[1])
            self.zDataReceived.emit(data[2])

        def switchState(self,state):
            self.stateChanged.emit(state)

        def switchLoad(self,state):
            self.overloadChanged.emit(state)

        def __init__(self, environment):
            QThread.__init__(self)
            Skeldata.__init__(self, environment)

        def actondata(self,v):
            self.chunkReceived.emit(v)
            
            
    class QtCMDREC(SkelCMDREC,QThread):
        
        respReceived = pyqtSignal(str,name='respReceived')
        
        def __init__(self,environment):
            
            QThread.__init__(self)
            CMDREC.__init__(self, environment)
            
        
        def react(self,resp):
            
            self.respReceived.emit(resp)


except ImportError:
    pass

