# epz
EpsilonPI ZMQ communication layer

Authors: Massimo Vassalli, Ettore Landini

This is an implementation of a very lightweight and custom framework for managing distributed control systems.

It implements the communication layer of a network of Producers (internally called epz_dev or simply DEVICES) which are
expected to be linked to a specific hardware (acquisition board, external switches, LED display, ...). The state of the
device is defined by a set of PARAMETERS (internally also epz_par) and one or more streams of DATA (epz_data) can also
be generated. A network of devices is allowed to exist, orchestrated to monitor and control a physical process. All
devices register as publishers (PUB) to a "messaging network" based on ZeroMQ [1], through which all parameters and data
streams will be routed to registered subscribers (SUB). Subscribers are digital representations of the state of the
device(s), which are instantiated at client-side to monitor the physical process, interact with it (change parameters)
and eventually visualize or save to disk the corresponding stream.

Although the concept of EPZ is quite general, it was designed to fit the needs of a specific hardware implementation,
for which devices are running on a "real-world" connected Raspberry-PI and remote clients are PyQt user interfaces. The
RPI is expected to speak with the hardware through dedicated procedures, not part of this package (see the fakeHW script
to have an idea of this component).

So far, EPZ was used to implement a single molecule force spectroscopy device in which one RPI was interfaced with a
Rasp-dsPIC board [1], providing 16bit 10kHz AD/DA and real-time feedback to control a piezo
actuator while stretching single molecules in a liquid cell [3].

LINKS
[1] http://zeromq.org
[2] http://www.epsilonpi.eu
[3] http://ww1.microchip.com/downloads/en/DeviceDoc/MicroSolutions-JanFeb-2016.pdf#25