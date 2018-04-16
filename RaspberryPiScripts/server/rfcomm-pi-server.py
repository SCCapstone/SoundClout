# file: rfcomm-pi-server.py
# auth: Foster Williams
# desc: simple rfcomm server that can operate the attached pi motor

from bluetooth import *
import re
import os

def run_seqence(sequence):
    f = open('sequence.txt', 'w')
    f.write(sequence)
    f.close()
    os.system('cyclerun.py')
server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service( server_sock, "musicPi1",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ],
#                   protocols = [ OBEX_UUID ]
                    )

print("Waiting for connection on RFCOMM channel %d" % port)

client_sock, client_info = server_sock.accept()
print("Accepted connection from ", client_info)
try:
    while True:
        data = client_sock.recv(1024)
        ribs =  ""
        ribs = ribs + data
        pork = ribs.split()
        beef =  pork[0]
        if beef == "turn":
            print "Testing motor"
            execfile("motorTest.py")
        if beef == "seqence":
            runsequence(beef[2])
        if len(data) == 0: break
        print("received [%s]" % data)
except IOError:
    pass

print("disconnected")

client_sock.close()
server_sock.close()
print("all done")
execfile('rfcomm-pi-server.py')
