#!/usr/bin/python

import m06attach
debugger = m06attach.debugger()
pid = int(raw_input("Enter the pid of the process to attach to: "))
debugger.attach(int(pid))
debugger.detach()