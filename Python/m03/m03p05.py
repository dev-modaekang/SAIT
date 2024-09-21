#!/usr/bash/python

import struct, sys

def hex_dump(lists):
	print "\n[%08x]: " % length,
	for i in lists:
	  print "%02x" % i,

	line = ""
	for j in lists:
		if j == ord('\n'):  # ord('a') returns the integer 97
			print " ",
		else: 
			line += chr(j)  # chr(97) returns the string 'a'
	print line,

sys.argv

if len(sys.argv)<2:
  print "want some arguments"
  sys.exit(-1)

file_name = sys.argv[1]
fd = open(file_name, "r")
lists = [] 
length = 0
while (1):
    value = fd.read(1)
    if value=="": 
      break
    length += 1
    n_value = struct.unpack('b',value)[0]
    lists.append(n_value)
    if len(lists)==16:
        hex_dump(lists)
        lists = []

hex_dump(lists)
print "\nTotal Length %d " % (length),