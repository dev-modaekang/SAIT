#!/usr/bin/python 

from pyutmp import UtmpFile
import time

for utmp in UtmpFile():
    if utmp.ut_user_process:
		local_time = time.localtime(utmp.ut_time) 
		print '%d-%02d-%02d %02d:%02d:%02d %s %s' % (local_time.tm_year, local_time.tm_mon, local_time.tm_mday, local_time.tm_hour, local_time.tm_min, local_time.tm_sec, utmp.ut_user, utmp.ut_line)
		# 2016-11-07 14:57:39 fred /dev/pts/24	
		# use this function time.strftime -> time.strptime
