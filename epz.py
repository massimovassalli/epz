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
        self.chunk = 10000
        self.x = []
        self.y = []
        self.t = []
        self.queue = queue.Queue()
        self. save = True
        self.notify = False
        self.setzmq()
        self.head = ''

    def setzmq(self):
        self.socket = self.context.socket(zmq.SUB)
        self.head = "{0}:DATA:".format(self.device)
        self.socket.setsockopt_string(zmq.SUBSCRIBE,self.head)
        self.socket.connect("tcp://{0}:{1}".format(self.epserver, self.subport))

    def actondata(self,v):
        pass

    def run(self):
        print('DATA channel on {0} starting to receive'.format(self.device))
        while self.goahead:
            body = self.socket.recv_string()
            data = [float(x) for x in body.strip(self.head).split(':')]
            if self.save:
                self.queue.put(data)
            if self.notify:
                self.t.append(data[0])
                self.x.append(data[1])
                self.y.append(data[2])
                if len(self.x) >= self.chunk:
                    self.actondata([self.t, self.x, self.y])
                    self.x=[]
                    self.y=[]
                    self.t=[]
        print('Finishing data thread')


class DATA(Skeldata, threading.Thread):
    def __init__(self,environment):
        threading.Thread.__init__(self)
        Skeldata.__init__(self, environment)

try:
    from PyQt4.QtCore import pyqtSignal, QThread


    class QtDATA(Skeldata, QThread):
        chunkReceived = pyqtSignal(list, name='chunkReceived')

        def __init__(self, environment):
            QThread.__init__(self)
            Skeldata.__init__(self, environment)

        def actondata(self,v):
            self.chunkReceived.emit(v)

except ImportError:
    pass

