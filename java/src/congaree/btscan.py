# file: btscan.py
# auth: Foster Williams
# desc: writes found devices to txt file
import sys
import bluetooth

target = None

services = bluetooth.find_service(address=target)

if len(services) == 0:
    print("no services found")

for svc in services:
    testString = "" + ("Service Name: %s" % svc["name"])
    if "musicPi" in testString: 
      print("%s" % svc["name"])
      print("%s" % svc["service-id"])
