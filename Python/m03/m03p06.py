#!/usr/bash/python

import struct 
import sys

if len(sys.argv)<2:
  print "want some arguments"
  sys.exit(-1)

file_name = sys.argv[1]
fd=open(file_name,'r')

temp1 = fd.read(64) # file header

# Program Header
print("[Program Header]")
p_type = fd.read(4)
np_type = struct.unpack('I',p_type)[0]
if np_type == 0x00000000:
	print "Type    : PT_NULL" 

elif np_type == 0x00000001:
	print "Type    : PT_LOAD"

elif np_type == 0x00000002:
	print "Type    : PT_DYNAMIC"

elif np_type == 0x00000003:
	print "Type    : PT_INTERP"

elif np_type == 0x00000004:
	print "Type    : PT_NOTE"

elif np_type == 0x00000005:
	print "Type    : PT_SHLIB"

elif np_type == 0x00000006:
	print "Type    : PT_PHDR"

elif np_type == 0x60000000:
	print "Type    : PT_LOOS"

elif np_type == 0x6FFFFFFF:
	print "Type    : PT_HIOS"

elif np_type == 0x70000000:
	print "Type    : PT_LOPROC"

elif np_type == 0x7FFFFFFF:
	print "Type    : HIPROC" 
else: 
	print "Type    : Unknown"

temp1 = fd.read(4)

p_offset = fd.read(8)
np_offset = struct.unpack('q', p_offset)[0]
print "Offset  : %s" % np_offset

p_vaddr = fd.read(8)
np_vaddr = struct.unpack('q', p_vaddr)[0]
print "Vaddr   : %s" % np_vaddr

temp2 = fd.read(8)

p_filesz = fd.read(8)
np_filesz = struct.unpack('q', p_filesz)
print "Filesz  : %d" % np_filesz

p_memsz = fd.read(8)
np_memsz = struct.unpack('q', p_memsz)
print "Memsz   : %d" % np_memsz

temp3 = fd.read(4)

# Section Header
print("[Section Header]")
sh_name = fd.read(4)
nsh_name = struct.unpack('I',sh_name)[0]
print "Name    : %s" % nsh_name

sh_type = fd.read(4)
nsh_type = struct.unpack('I',sh_type)[0]
if sh_type == 0x0:
	print "Type    : SHT_NULL"
elif sh_type == 0x1:
	print "Type    : SHT_PROGBITS" 

elif sh_type == 0x2:
	print "Type    : SHT_SYMTAB"

elif sh_type == 0x3:
	print "Type    : SHT_STRTAB"

elif sh_type == 0x4:
	print "Type    : SHT_RELA"

elif sh_type == 0x5:
	print "Type    : SHT_HASH"

elif sh_type == 0x6:
	print "Type    : SHT_DYNAMIC"

elif sh_type == 0x7:
	print "Type    : SHT_NOTE"

elif sh_type == 0x8:
	print "Type    : SHT_NOBITS"

elif sh_type == 0x9:
	print "Type    : SHT_REL"

elif sh_type == 0x0A:
	print "Type    : SHT_SHLIB"

elif sh_type == 0x0B:
	print "Type    : SHT_DYNSYM" 
elif sh_type == 0x0E:
	print "Type    : SHT_INIT_ARRAY" 
elif sh_type == 0x0F:
	print "Type    : SHT_FINI_ARRAY" 
elif sh_type == 0x10:
	print "Type    : SHT_PREINIT_ARRAY" 
elif sh_type == 0x11:
	print "Type    : SHT_GROUP" 
elif sh_type == 0x12:
	print "Type    : SHT_SYMTAB_SHNDX" 
elif sh_type == 0x13:
	print "Type    : SHT_NUM" 
elif sh_type == 0x60000000:
	print "Type    : SHT_LOOS" 
else: 
	print "Type    : Unknown"

temp4 = fd.read(8)

sh_address = fd.read(8)
nsh_address = struct.unpack('q', sh_address)
print "Address : %s" % nsh_address

sh_offset = fd.read(8)
nsh_offset = struct.unpack('q', sh_offset)
print "Offset  : %s" % nsh_offset

sh_size = fd.read(8)
nsh_size = struct.unpack('q', sh_size)
print "Size    : %d" % nsh_size

# Program Header
"""
 * p_type : (0x00 / 4byte) Identifies the type of the segment.
 * p_offset : (0x04 / 4bytes or 0x08 / 8bytes) Offset of the segment in the file image.
 * p_vaddr : (0x08 / 4bytes or 0x10 / 8bytes Virtual address of the segment in memory.
 * p_filesz : (0x10 / 4bytes or 0x20 / 8bytes) Size in bytes of the segment in the file image. May be 0.
 * p_memsz (0x14 / 4bytes or 0x28 / 8bytes) Size in bytes of the segment in memory. May be 0.
"""

# Section Header
"""
 name : (0x00 / 4bytes) An offset to a string in the .shstrtab section that represents the name of this section
 Type : (0x04 / 4bytes) Identifies the type of this header.
 Address : (0x0C / 4bytes or 0x10 / 8bytes) Virtual address of the section in memory, for sections that are loaded.
 Offset : (0x10 / 4bytes or 0x18 / 8bytes) Offset of the section in the file image.
 Size : (0x14 / 4bytes or 0x20 / 8bytes) Size in bytes of the section in the file image. May be 0.
 """