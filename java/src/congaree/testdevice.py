# file: connect.py
# auth: Foster Williams
# desc: Sends basic data to a Raspberry pi to run a motor breifly 
from bluetooth import *
import sys

if sys.version < '3':
    input = raw_input

addr = None
filedata = open("connectedDevices.txt", "r")


deviceinfo = filedata.readlines()

uuid = (deviceinfo[1].lower()).strip('\n')
service_matches = find_service( uuid = uuid, address = addr )


first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print (name)
print (uuid)
sock=BluetoothSocket( RFCOMM )
sock.connect((host, port))

data = "turn on"

sock.send(data)
sock.close()
