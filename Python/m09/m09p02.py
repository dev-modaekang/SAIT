import sys

# Read in the DLL
attached_file = raw_input("Enter the name of the file to attach to: ")
dll_file = raw_input("Enter the name of the DLL file to be hidden: ")

fd = open( attached_file, "rb" )
dll_contents = fd.read()
fd.close()

print "[*] Filesize: %d" % len( dll_contents )

# Now write it out to the ADS
fd = open( "%s:%s" % ( dll_file, attached_file ), "wb" )
fd.write( dll_contents )
fd.close()
