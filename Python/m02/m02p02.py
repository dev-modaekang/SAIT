#!/usr/bin/python

import socket
import re

hostname = socket.gethostname()

fd=open("/proc/meminfo",'r')
oneline = fd.readline()
value = int(re.search(r'\d+', oneline).group())
mb = value / 1024

print "Hostname :", hostname+',', "Memory :", mb, "MB"
