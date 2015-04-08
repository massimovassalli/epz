# epz
EpsilonPI ZMQ communication layer

This is an implementation of a very lightweight and custom-oriented distributed framework for managing distributed
control systems. In other words, it implements the communication layer of a network of Producers (mainly hardware-linked
processes) and Consumers (mainly gui-oriented programs) orchestrated together to monitor and manage a physical process.
The hardware layer is intended to be implemented inside Raspberry-PI connected to the real world through Rasp-dsPIC
boards. The whole code is implemented in Python 3, while an older and unsupported Python 2.7 implementation exists.