import m06events
debugger = m06events.debugger()
pid = raw_input("Enter the PID of the process to attach to: ")
debugger.attach(int(pid))
debugger.run()
debugger.detach()
