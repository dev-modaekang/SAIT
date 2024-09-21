#!/usr/bash/python

import os, sys, re
import time

# /proc/[pid]/stat

proclist=os.listdir('/proc')


print proclist

validpids=[]
for oneproc in proclist:
    m=re.match('^[0-9]*$', oneproc)
    if m:
        print oneproc
    else:
        print "NOTAPID", oneproc

for oneproc in proclist:
    try:
        pid=int(oneproc)
        if oneproc==str(pid):
          print oneproc
    except:
        pass

for pid in validpids:
    #fname='/proc/'+pid+'/stat'
    fname = os.path.join('/proc',pid,'stat')
    print fname

