from threading import Thread

import zmq

from epz.core.zhelpers import socket_set_hwm
from epz.core.epz import ENV

CHUNK_SIZE = 250000


class FileSend(object):

    def __init__(self, fileT, ctx=ENV['context']):

        self.ctx = ctx
        self.fileT = fileT
        self.tempThread = None


    def transfer(self):

        if self.tempThread is not None:
            if self.tempThread.isAlive():
                return
        self.tempThread = Thread(target=sender_server,args=[self.ctx,self.fileT])
        self.tempThread.start()


def sender_server(ctx,fileT):
    file = open(fileT, "rb")

    router = ctx.socket(zmq.ROUTER)

    # Default HWM is 1000, which will drop messages here
    # since we send more than 1,000 chunks of test data,
    # so set an infinite HWM as a simple, stupid solution:
    socket_set_hwm(router, 0)
    router.bind("tcp://*:6000")

    while True:
        # First frame in each message is the sender identity
        # Second frame is "fetch" command
        try:
            identity, command = router.recv_multipart()
        except zmq.ZMQError as e:
            if e.errno == zmq.ETERM:
                return   # shutting down, quit
            else:
                raise

        assert command == b"fetch"

        while True:
            data = file.read(CHUNK_SIZE)
            try:
                datas = data.encode('ascii')
            except:
                datas = data
            print('the datas: {0}'.format(datas))
            router.send_multipart([identity, datas])
            if not data:
                break
        break