import sys
try:
    from pydbg import *
    from pydbg.defines import *
    from utils import hooking
except:
    print "ERROR: you need pydbg and utils.hooking from PAIMEI."
    sys.exit(-1)

hooks = None # needed in handler_load_dll()

def entry_SomeChromeFunction(dbg, args):
    """ This is where you end up when the function got called """
    # Do whatever you like in here
    return DBG_CONTINUE

def handler_load_dll(dbg):
    last_dll = dbg.get_system_dll(-1)
    # Wait for the DLL we're looking for ...
    if "some-chrome.dll".lower() == last_dll.name.lower():
        # Now resolve the address of the function (see note: requires debug symbols)
        funcaddr = dbg.func_resolve(last_dll.name,"SomeChromeFunction")
        # Add the hook
        hooks.add(dbg, funcaddr, 2, entry_SomeChromeFunction, None) # <- last one is for breakpoint on exit of the function
    return DBG_CONTINUE

dbg = pydbg()
hooks = utils.hook_container()
dbg.load("chrome.exe"); # assuming that is the name of the binary
# you can also use a full path above and pass the command line as parameter
dbg.set_callback(LOAD_DLL_DEBUG_EVENT, handler_load_dll)
dbg.run()