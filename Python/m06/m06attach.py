from ctypes import *
from my_debugger_defines import *

kernel32 = windll.kernel32
#PROCESS_ALL_ACCESS = (0x000F0000L | 0x00100000L | 0xFFF)

class debugger():
    def __init__(self):
        self.h_process = None
        self.pid = None
        self.debugger_active = False

    def load(self,path_to_exe):

        print "[*] We have successfully launched the process!"
        print "[*] PID: %d" % process_information.dwProcessId
        # Obtain a valid handle to the newly created process
        # and store it for future access
        self.h_process = self.open_process(process_information.dwProcessId)

    def open_process(self,pid):
        h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS,False,pid)
        return h_process

    def attach(self,pid):
        self.h_process = self.open_process(pid)
        # We attempt to attach to the process
        # if this fails we exit the call
        if kernel32.DebugActiveProcess(pid):
            self.debugger_active = True
            self.pid = int(pid)
        else:
            print "[*] Unable to attach to the process."

    def run(self):
        # Now we have to poll the debuggee for
        # debugging events
        while self.debugger_active == True:
            self.get_debug_event()

    def get_debug_event(self):
        debug_event = DEBUG_EVENT()
        continue_status = DBG_CONTINUE
        if kernel32.WaitForDebugEvent(byref(debug_event),INFINITE):
            # We aren't going to build any event handlers
            # just yet. Let's just resume the process for now.
            raw_input("Press a key to continue...")
            self.debugger_active = False
            kernel32.ContinueDebugEvent( \
                debug_event.dwProcessId, \
                debug_event.dwThreadId, \
                continue_status )
    def detach(self):
        if kernel32.DebugActiveProcessStop(self.pid):
            print "[*] Finished debugging. Exiting..."
            return True
        else:
            print "There was an error"
            return False