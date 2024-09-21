#!/usr/bin/python 

import os
import sys

class LinuxProcList: 
    def __init__(self, parameter_pid): 	
		self.file_name = "/proc/" + str(parameter_pid) + "/stat"
		file = open(self.file_name, "r") 
		fd = file.read()
		lists =fd.split()
		self.pid = lists[0]
		self.name = lists[1] ##
		self.state = lists[2]
		self.ppid = lists[3]
		self.pgrp =  lists[4]
		self.session =  lists[5]
		self.tty_nr =  lists[6]
		self.tpgid =  lists[7]
		self.flags =  lists[8] 
		self.minflt =  lists[9] 
		self.cminflt =  lists[10] 
		self.majflt =  lists[11] 
		self.cmajflt =  lists[12]
		self.utime =  lists[13]
		self.stime =  lists[14]
		self.cutime =  lists[15]
		self.cstime =  lists[16]
		self.priority =  lists[17]
		self.nice =  lists[18]
		self.num_threads =  lists[19]
		self.itrealvalue =  lists[20]
		self.starttime =  lists[21]
		self.vsize =  lists[22]
		self.rss =  lists[23]
		self.rss_lim =  lists[24] ## 
		self.start_code =  lists[25] ## 
		self.end_code =  lists[26] ##
		self.start_stack =  lists[27] ##
		self.esp =  lists[28] ##
		self.eip =  lists[29]  ##
		self.signal =  lists[30] 
		self.blocked =  lists[31] 
		self.sigignore =  lists[32] 
		self.sigcatch =  lists[33] 
		self.wchan =  lists[34] 
		self.nswap =  lists[35] 
		self.cnswap =  lists[36]
		self.exit_signal =  lists[37] 
		self.processor =  lists[38]
		self.rt_priority =  lists[39]
		self.policy =  lists[40] 
		self.delayacct_blkio_ticks =  lists[41] 
		self.guest_time =  lists[42] 
		self.cguest_time =  lists[43] 
		self.start_data =  lists[44] ## 
		self.end_data =  lists[45] ##
		self.start_brk =  lists[46] 
		self.arg_start =  lists[47] 
		self.arg_end =  lists[48] 
		self.env_start =  lists[49] 
		self.env_end =  lists[50] 
		self.exit_code =  lists[51]
		self.children = LinuxProcess().children(parameter_pid).split(' ')
	
    def print_info(self):
		print "%15s" % "name : ",   "%20s" % self.name[1:len(self.name)-1] # it start from 1 to len-1
		print "%15s" % "rss_lim : ",    "%20s" % hex(int((self.rss_lim)))  
		print "%15s" % "start_code : ", "%20s" % hex(int((self.start_code)))  
		print "%15s" % "end_code : ", "%20s" % hex(int((self.end_code)))  
		print "%15s" % "start_stack : ", "%20s" % hex(int((self.start_stack)))
		print "%15s" % "esp : ", "%20s" % hex(int((self.esp))) 
		print "%15s" % "eip : ", "%20s" % hex(int((self.eip))) 
		print "%15s" % "start_data : ","%20s" % hex(int((self.start_data))) 
		print "%15s" % "end_data : ","%20s" % hex(int((self.end_data)))  
		print "%15s" % "start_brk : ","%20s" % hex(int((self.start_brk))) 
		print "%15s" % "arg_start : ","%20s" % hex(int((self.arg_start))) 
		print "%15s" % "arg_end : ","%20s" % hex(int((self.arg_end))) 
		print "%15s" % "env_start : ","%20s" % hex(int((self.env_start))) 
		print "%15s" % "env_end : ","%20s" % hex(int((self.env_end))) 

class LinuxProcess:
    def proclist(self): 
		proclist = os.listdir('/proc') 
		validpids = []
		for val in proclist:
			if val.isdigit(): 
				validpids.append(int(val)) 
		return validpids

    def cmdline(self, parameter_pid):
		file_name = "/proc/"+str(parameter_pid)+"/cmdline" 
		fd = open(file_name, "r")  
		val_cmdline = fd.read() 
		if val_cmdline =="": 
			return "None"  
		else: 
			return val_cmdline

    def children(self,parameter_pid):
		file_name = "/proc/"+str(parameter_pid)+"/task/"+str(parameter_pid)+"/children" 
		fd = open(file_name, "r")  
		val_children = fd.read() 
		return val_children

def print_val(pid):
	print "|    L... %s " % pid,
	if len(func1.cmdline(pid)) >= 120:
		print func1.cmdline(pid)[0:120]
	else:
		print func1.cmdline(pid)
	list_children3 =func1.children(pid).split()
	if list_children3 == "None":
		print("\n")
	else:
		for k in list_children3:
			print("|   "),
			print_val(k)

func1 = LinuxProcess()
list_pids = func1.proclist()

for i in list_pids:
	if func1.cmdline(i) == "None":
		continue
	else :
		print "%s " % i,
		if len(func1.cmdline(i)) >= 120:
			print func1.cmdline(i)[0:120]
		else:
			print func1.cmdline(i)
    	
		list_children = func1.children(i).split()
    
		for j in list_children:
			if func1.cmdline(i) == "None":
				continue
			else :
				print "L... %s " % j,
				if len(func1.cmdline(j)) > 120:
					print func1.cmdline(j)[0:120]
				else:
					print func1.cmdline(j)
				
				list_children2 = func1.children(j).split()
				if list_children2 == "None":
					print("\n")
				else:
					for i in list_children2:
						if func1.cmdline(i) == "None":
							continue
						else :
							print_val(i)

