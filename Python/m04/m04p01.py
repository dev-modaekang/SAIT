#!/usr/bin/python 

import os
import sys

class LinuxProcess:
	def __init__(self, pid): 	
		self.file_name = "/proc/" + pid + "/stat"
		file = open(self.file_name, "r")
		fd = file.read()
		lists =fd.split()
        # http://man7.org/linux/man-pages/man5/proc.5.html
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
	
	def print_info(self):
		print "\n"
		print "%15s" % "name : ", "%20s" % self.name[1:len(self.name)-1] # it start from 1 to len-1
		print "%15s" % "rss_lim : ","%20s" % hex(int((self.rss_lim)))  
		print "%15s" % "start_code : ","%20s" % hex(int((self.start_code)))  
		print "%15s" % "end_code : ", "%20s" % hex(int((self.end_code)))  
		print "%15s" % "start_stack : ","%20s" % hex(int((self.start_stack)))
		print "%15s" % "esp : ","%20s" % hex(int((self.esp))) 
		print "%15s" % "eip : ","%20s" % hex(int((self.eip))) 
		print "%15s" % "start_data : ","%20s" % hex(int((self.start_data))) 
		print "%15s" % "end_data : ","%20s" % hex(int((self.end_data)))  
		print "%15s" % "start_brk : ","%20s" % hex(int((self.start_brk))) 
		print "%15s" % "arg_start : ","%20s" % hex(int((self.arg_start))) 
		print "%15s" % "arg_end : ","%20s" % hex(int((self.arg_end))) 
		print "%15s" % "env_start : ","%20s" % hex(int((self.env_start))) 
		print "%15s" % "env_end : ","%20s" % hex(int((self.env_end))) 
		print "\n"

if len(sys.argv)<2:
  print "want some arguments"
  sys.exit(-1)   

pid = sys.argv[1]

func = LinuxProcess(pid)
func.print_info()












##############################
"""
proclist=os.listdir('/proc')
validpids=[])

for oneproc in proclist:
    try:
        pid= oneproc)
        if oneproc==str(pid):
          validpids.append(oneproc)
    except:
        pass

# we can get the pid
for pid in validpids:
    print pid
"""

"""
pid
comm
state
ppid 
pgrp
session
tty_nr 
tpgid
flags
minflt  
cminflt 
majflt  
cmajflt  
utime  
stime 
cutime  
cstime  
priority  
nice  
num_threads  
itrealvalue  
starttime  
vsize  
rss  
rsslim  
startcode  
endcode 
startstack  
kstkesp  
kstkeip  
signal  
blocked 
sigignore  
sigcatch  
wchan 
nswap  
cnswap  
exit_signal
processor
rt_priority
policy 
delayacct_blkio_ticks 
guest_time
cguest_time 
start_data  
end_data  
start_brk 
arg_start 
arg_end 
env_start
env_end
exit_code
"""