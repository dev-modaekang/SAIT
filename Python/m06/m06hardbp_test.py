import m06hardbp 
from my_debugger_defines import *

debugger = m06hardbp.debugger()

pid = raw_input("Enter the PID of the process to attach to: ")

debugger.attach(int(pid))

printf = debugger.func_resolve("msvcrt.dll","printf")
print "Address of printf: 0x%08x" % printf

debugger.bp_set_hw(printf,1,HW_EXECUTE) 

debugger.run()

debugger.detach()
