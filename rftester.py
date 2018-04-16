#This is a sequence tester for the SoudClout Project. The purpose of the soundclout project is to create music installations
#This program simply

from bluetooth import *
import re
import os

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
            print "Successful test connection"
        if beef == "seqence":
            print(beef)
        if len(data) == 0: break
        print("received [%s]" % data)
except IOError:
    pass

print("disconnected")

client_sock.close()
server_sock.close()
print("all done")
