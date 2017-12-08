#!/bin/bash
touch devices.txt
sudo /usr/bin/python btscan.py > devices.txt
