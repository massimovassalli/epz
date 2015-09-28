# epz
EpsilonPI ZMQ communication layer

Authors: Massimo Vassalli, Ettore Landini

This is an implementation of a very lightweight and custom-oriented distributed framework for managing distributed
control systems. In other words, it implements the communication layer of a network of Producers (mainly hardware-linked
processes) and Consumers (mainly gui-oriented programs) orchestrated together to monitor and manage a physical process.
The hardware layer is intended to be implemented inside Raspberry-PI connected to the real world through Rasp-dsPIC
boards. The whole code is implemented in Python 3, while an older and unsupported Python 2.7 implementation exists.

NB: There is currently no way of knowing when the zmq.socket created by the epz.CMD class will be ready after it's creation.
Thus the first command you'll send to the epz server could not be send correctly.

Required libraries:
PyZmq (https://github.com/zeromq/pyzmq/) version 2.2 or above
ZeroMQ (http://zeromq.org/intro:get-the-software) version 3.25, 4.13 or above