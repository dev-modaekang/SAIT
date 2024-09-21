#!/usr/bin/python 

import socket

# target_host = "itss.biomea.com" #this one is for problem 02
target_host = "127.0.0.1"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
client.send("GET /cgi-bin/echo.cgi HTTPS/1.1\r\nHost: itss.biomea.com\r\n\r\n")
response = client.recv(4096)

print response
