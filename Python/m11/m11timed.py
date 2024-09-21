import socket
import threading
import datetime

bind_ip   = "0.0.0.0"
bind_port = 2013

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
server.bind((bind_ip,bind_port))

print "[*] UDP Listening on %s:%d" % (bind_ip,bind_port)

while True:
	udp, csocket = server.recvfrom(1024)  
	sent = server.sendto('%s' % datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), csocket)															

