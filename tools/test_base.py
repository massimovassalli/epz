# EPZ 1.0
# Perform tests of the base components
# minimally, launch the script from three different terminals with 3 different roles

import argparse,sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

parser = argparse.ArgumentParser()
parser.add_argument("role", help="Specify the role",choices=['forwarder','reader','writer'])
parser.add_argument("-d","--data", help="Set the R/W actor to be a DATA actor",action="store_true")
args = parser.parse_args()

if args.role == 'forwarder':
    print('Ready to orchestrate')
    import forwarder
    f = forwarder.Forwarder()
    f.start()

else:
    if args.data:
        actor = 'DATA'
        print("selected a DATA actor")
    else:
        actor = 'CMD'
        print("selected a CMD actor")

    if args.role == 'reader':
        print('Waiting for incoming data')
        print('Please remember to create and populate my sister writer')
        if actor == 'CMD':
            from core.cmdRec import CMDREC
            c = CMDREC()
            c.setCallback(print)
            c.daemon = False
            c.start()
        else:
            from core.dataRec import dataRec
            d = dataRec()
            d.setValueCallback(print)
            d.daemon = False
            d.start()
    else:
        print('Ready to send')
        if actor == 'CMD':
            from core.cmd import CMD
            sender = CMD()
            while (True):
                newtxt = input('cmd,val -->')
                sender.send(*newtxt.split(','))
        else:
            from core.data import DATA
            sender = DATA()
            while (True):
                newtxt = input('1,1,1 -->')
                sender.send(*newtxt.split(','))