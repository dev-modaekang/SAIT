import socket
import os
import struct
import threading
from netaddr import IPNetwork,IPAddress


# host to listen on
host   = "10.187.136.253"

# subnet to target
subnet = "10.187.136.0/24"

# magic we'll check ICMP responses for
magic_message = "PYTHONRULES!"
# map protocol constants to their names
protocol_map = {1:"ICMP", 6:"TCP", 17:"UDP"}
#Length of ICMP packet
sizeof_ICMP=8

def udp_sender(subnet,magic_message):
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    for ip in IPNetwork(subnet):
        try:
            sender.sendto(magic_message,("%s" % ip,65212))
        except:
            pass
              
# create a raw socket and bind it to the public interface
print "My IP: %s" %host
if os.name == "nt":
    socket_protocol = socket.IPPROTO_IP 
else:
    socket_protocol = socket.IPPROTO_ICMP
    
sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

sniffer.bind((host, 0))

# we want the IP headers included in the capture
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# if we're on Windows we need to send some ioctls
# to setup promiscuous mode
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# start sending packets
t = threading.Thread(target=udp_sender,args=(subnet,magic_message))
t.start()        

try:
    while True:
        
        # read in a single packet
        raw_buffer = sniffer.recvfrom(65535)[0]
        
        # decode IP header from the first 20 bytes of the buffer
        ip_buffer=raw_buffer[:20]
        iph = struct.unpack('!BBHHHBBH4s4s',ip_buffer)
        version = iph[0] >> 4 #Version
        ihl = iph[0] * 0xF    #IHL
        iph_length = ihl * 4  #Total Length
        ttl = iph[5]
        protocol_num= iph[6]
        # human readable protocol
        protocol=protocol_map[protocol_num]
        # human readable IP addresses
        src_address = socket.inet_ntoa(iph[8])
        dst_address = socket.inet_ntoa(iph[9])     
        
        if protocol == "IP":
             print "Proto: %s %s -> %s" % (protocol, src_address, dst_address)
        # if it's ICMP we want it
        if protocol == "ICMP":
            
            # calculate where our ICMP packet starts
           # offset = ihl * 4
           
            icmp_buf = raw_buffer[20:20+sizeof_ICMP]
            #icmp_buf = raw_buffer[offset:offset+sizeof_ICMP]
            
            # create our ICMP structure
            icmp_type,icmp_code,checksum,packetID,sequence=struct.unpack("bbHHh",icmp_buf) 
            #icmp_header = ICMP(buf)
            print ("Proto: %s %s -> %s" % (protocol,src_address, dst_address)),
            print ("    ICMP -> Type: %d Code: %d" % (icmp_type, icmp_code))
            
            
            # now check for the TYPE 3 and CODE 3 which indicates
            # a host is up but no port available to talk to           
            if icmp_code == 3 and icmp_type == 3:
                
                # check to make sure we are receiving the response 
                # that lands in our subnet
                if IPAddress(src_address) in IPNetwork(subnet):
                    
                    # test for our magic message
                    if raw_buffer[len(raw_buffer)-len(magic_message):] == magic_message:
                        print "Host Up: %s" % src_address
# handle CTRL-C
except KeyboardInterrupt:
    # if we're on Windows turn off promiscuous mode
    if os.name == "nt":
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)