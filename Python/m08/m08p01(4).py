from immlib import *

class fire (LogBpHook) :
    def __init__(self):
        self.imm=Debugger()
        self.logfile = "B:\\fire_log.txt"
        #directory where the log file has to be saved
        LogBpHook.__init__(self)
                  
    def run(self,regs):
        addr=self.imm.readLong(regs['ESP']+8)
        str1=self.imm.readString(addr)
        self.imm.log("PR_Write ( 0x%x) <- %s" % (addr,str1) 
        fd = open( self.logfile, "a" )
        fd.write( str1 )
        fd.close()

    # this function run automatically when hook is hit and function code is #executed which logs it in to file and displays on log window of debugger
    def main(args) :
        imm=Debugger()
        wfun=imm.getAddress("nspr4.PR_Write")

    #setup hook point
        fire_hook=fire()
        fire_hook.add( "%08x" % wfun, wfun)
        return "[*] READY for ACTION"

"""
reference
http://c0defreak.blogspot.com/2013/03/

""""