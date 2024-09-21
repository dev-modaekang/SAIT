import socket
from datetime import datetime
import struct

target_host   = "0.0.0.0"
target_port = 2013

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some data
client.sendto("AAABBBCCC",(target_host,target_port))

#receive some data
data, addr = client.recvfrom(1024)

#print "[*] Received '%s' from: %s:%d" % (data, addr[0], addr[1])

time_object=datetime.strptime(data, '%Y-%m-%d %H:%M:%S')
print time_object.now().strftime('%Y-%m-%d %H:%M:%S')