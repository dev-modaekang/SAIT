#!/usr/bash/python#!/usr/bin/python 

import struct 
import sys

# tips
#fd = ~~~~
#data = read(fd)
#otf = 12 #e_machine
#size = 2 #e_machine
#res = struct.unpack("H", data[12:14])[0] #e_machine
#etype = struct.unpack("HH", data[10:14])[0] #e_type + e_,machine

sys.argv

if len(sys.argv)<2:
  print "want some arguments"
  sys.exit(-1)

file_name = sys.argv[1]
fd=open(file_name,'r')
header = fd.read(4)
magic = struct.unpack('I',header)[0]
print "File   :", file_name
print "Magic  :", hex(magic)

format = fd.read(1)
format_res = struct.unpack('b', format)[0]
#print format_res
if format_res == 1:
    print "Format : 32-bit"
elif format_res == 2:
    print "Format : 64-bit"

endian  = fd.read(1)
endian_res = struct.unpack('b',endian)[0] 
#print endian_res
if endian_res == 1:
	print "Endian : little"
elif endian_res == 2:
	print "Endian : big"
else:
	print "Endian : unknown"

temp = fd.read(12)
machine = fd.read(2)

machine_res = struct.unpack('h', machine)[0]
#print machine_res

if machine_res == 0x00:
	print "No specific instruction set" 

elif machine_res == 0x02:
	print "Machine: SPARC"

elif machine_res == 0x03:
	print "Machine: x86"

elif machine_res == 0x08:
	print "Machine: MIPS"

elif machine_res == 0x14:
	print "Machine: PowerPC"

elif machine_res == 0x16:
	print "Machine: S390"

elif machine_res == 0x28:
	print "Machine: ARM"

elif machine_res == 0x2A:
	print "Machine: SuperH"

elif machine_res == 0x32:
	print "Machine: IA-64"

elif machine_res == 0x3E:
	print "Machine: x86-64"

elif machine_res == 0xB7:
	print "Machine: AArch64" 

elif machine_res == 0xF3:
	print "Machine: RISC-V"

else: 
	print "Machine: Unknown"