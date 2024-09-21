#!/usr/bash/python 

import ctypes
import os, sys

pid = sys.argv[1]; 
file_name = "/proc/"+str(pid)+"/stat" 
result = ctypes.CDLL("./libprintproc.so")

fd = open(file_name, 'r') 
values = fd.read() 
word_list = values.split() 

result.printproc(ctypes.c_char(word_list[2]),int(word_list[3]),int(word_list[7]),int(word_list[25]),int(word_list[27]),int(word_list[28]),int(word_list[29]))