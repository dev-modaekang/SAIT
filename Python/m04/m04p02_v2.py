#!/usr/bin/python 

import os
import sys

class LinuxProcList: 
	def proclist(self): 
		proclist = os.listdir('/proc') 
		validpids = []
		for val in proclist:
			if val.isdigit(): 
				validpids.append(int(val)) 
		return validpids

	def cmdline(self,parameter_pid):
		file_name = "/proc/"+str(parameter_pid)+"/cmdline" 
		fd = open(file_name, "r")  
		val_cmdline = fd.read() 
		if val_cmdline =="": 
			return None  
		else: 
			return val_cmdline

	def children(self,parameter_pid):
		file_name = "/proc/"+str(parameter_pid)+"/task/"+str(parameter_pid)+"/children" 
		fd = open(file_name, "r")  
		val_children = fd.read() 
		return val_children

if len(sys.argv)<2:
  print "want some arguments"
  sys.exit(-1)   

pid = sys.argv[1]
func = LinuxProcList()

print "\n### [list of pids] ###"
print func.proclist()
print "\n### [cmdline of the pid : %s ] ###" % pid
print func.cmdline(pid)
print "\n### [children of the pid : %s ] ###" % pid
print func.children(pid)
print "\n"