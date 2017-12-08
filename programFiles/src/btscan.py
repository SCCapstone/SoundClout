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

for svc in services:
    testString2 = "" + ("Service Name: %s" % svc["name"])
    testString3 = "" + ("%s" % svc["service-id"])
    if "musicPi" in testString2:
      testString2 = testString2
    elif "None" in testString2:
      testString2 = testString2
    elif "None" in testString3:
      testString2 = testString2
    else: 
      print("%s" % svc["name"])
      print("%s" % svc["service-id"])
