from threading import Thread

import zmq
from epz.core.epz import ENV

CHUNK_SIZE = 250000
ADDR = '172.16.1.202'
LOCADDR = '127.0.0.1'


class FileRec(object):

    def __init__(self,destFile,addr,ctx=ENV['context']):

        self.ctx = ctx
        self.destFile = destFile
        self.server = addr
        self.tempThread = None


    def update(self,destFile,addr):

        self.destFile = destFile
        self.server = addr


    def receive(self):

        if self.tempThread is not None:
            if self.tempThread.isAlive():
                return
        self.tempThread = Thread(target=client_thread, args=[self.ctx, self.destFile,self.server])
        self.tempThread.start()



def client_thread(ctx,destfile, addr=LOCADDR):
    dealer = ctx.socket(zmq.DEALER)
    dealer.connect('tcp://{0}:6000'.format(addr))
    dealer.send(b"fetch")

    total = 0       # Total bytes received
    chunks = 0      # Total chunks received

    theChunk = open(destfile,'wb')

    while True:
        try:
            chunk = dealer.recv()
        except zmq.ZMQError as e:
            if e.errno == zmq.ETERM:
                return   # shutting down, quit
            else:
                raise

        chunks += 1
        size = len(chunk)
        print('Sloth love Chunk: {0}'.format(chunk))
        total += size
        theChunk.write(chunk)
        if size == 0:
            break   # whole file received

    theChunk.close()