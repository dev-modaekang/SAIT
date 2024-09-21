#!/usr/bash/python

import stat
import os, time
import sys

sys.argv

if len(sys.argv)<2:
  print "want some arguments"
  sys.exit(-1)

file_name = sys.argv[1]
file_size = os.stat(file_name).st_size
file_inode = os.stat(file_name).st_ino
file_modified = time.ctime(os.path.getmtime(file_name))

print "filename : " + file_name
print "size     :",
print file_size
print "Inode    :",
print file_inode
print "Last Mod :",
print file_modified

#fd = os.open(file_name, os.O_RDWR|os.O_CREAT)
#fd = os.open( val, os.O_RDWR|os.O_CREAT )
#fd = os.open(val, 'r')
#fd = os.open("test.txt")
#fd=os.open("/proc/meminfo",'r')
#info = os.fstat(fd)

#print "size     :",
#print (os.path.getsize('/home/user/git/modae-k/python/m03/test.txt'))
#print "Inode    :",
#print (os.stat('/home/user/git/modae-k/python/m03/test.txt').st_ino)
#print ("Last Mod : %s" % time.ctime(fd))