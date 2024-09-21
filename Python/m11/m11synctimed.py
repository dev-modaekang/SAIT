import socket
import struct
import sys
import time
from datetime import datetime

bind_ip   = "0.0.0.0"
bind_port = 2013
NTP_SERVER = "time.nist.gov"
TIME1970 = 2208988800L

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
server.bind((bind_ip,bind_port))

print "[*] UDP Listening on %s:%d" % (bind_ip,bind_port)

while 1:
    client, addr = server.recvfrom(1024)
    print "[*] connected : %s:%d" % (addr[0], addr[1])
    print "[*] Received '%s' from %s" % (client, addr[0])

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = '\x1b' + 47 * '\0'
    client.sendto(data, (NTP_SERVER, 37))
    data, address = client.recvfrom( 1024 )
    if data:
        print "[*] connected : %s:%d" % (NTP_SERVER, 37)
        #t = struct.unpack( '!12I', data )[10]
        #t -= TIME1970
        print "[*] Received '%s' from: %s" % (data, address)
    #time_object = datetime.strftime(t, "%Y-%m-%d %H:%M:%S \r\n")
    server.sendto(data, addr)


    #sent = server.sendto('%s' % datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), address)