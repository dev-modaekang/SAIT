#! /usr/bin/env python
# -*- coding: utf-8 -*- 

import threading
import sys
import subprocess
import time
import getopt 
import socket

execute = ""
port = 0
listen = False
target = ""
upload_dest = ""
command = False

def usage():
	print "BHP Net Tool"
	print
	print "Usage: bhpnet.py -t target_host -p port"
	print "-l --listen - listen on [host]:[port] for incoming connections"
	print "-e --execute=file_to_run - execute the given file upon receiving a connection"
	print "-c --command- initialize a command shell"
	print "-u --upload=destination - upon receiving connection upload a file and write to [destination]"
	print
	print
	print "Examples: "
	print "bhpnet.py -t 192.168.0.1 -p 5555 -l -c"
	print "bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe"
	print "bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\""
	print "echo 'ABCDEFGHI' | ./bhpnet.py -t 192.168.11.12 -p 135"
	sys.exit(0)

def client_sender(bfr):
	#create a TCP socket
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		#connect to the target host
		client.connect((target, port))
		if len(bfr):
			client.send(bfr)

		#now wait the respnse 
		while True:

			recv_len = 1
			response = ""

			while recv_len:
				data = client.recv(4096)
				recv_len = len(data)
				response += data

				if recv_len < 4096:
					break
			print response

			#wait for another input
			bfr = raw_input("")
			bfr += '\n'
			client.send(bfr)

	except:
		print "Exiting! sth went wrong. (tho, seriously, has anything gone right in your whole pathetic existence?)"
		client.close()

def client_handler(client_sock):
	global execute
	global upload
	global command

	if len(upload_dest):
		file_buffer = ""
		while True:
			data = client_sock.recv(1024)

			if not data:
				break
			else:
				file_buffer += data
				try:
					file_desc = open(upload_dest, 'wb')
					file_desc.write(file_buffer) 
					file_desc.close()
					client_sock.send('Successfully saved into %s \r\n' % upload_dest)

				except:
					client_sock.send("Failed to save data to file %s \r\n" % upload_dest)


	if len(execute):
		output = run_command(execute)
		client_sock.send(output)

	if command:
		while True:
			client_sock.send("<BHP:#> ")
			cmd_bfr = ""
			while "\n" not in cmd_bfr:
				cmd_bfr += client_sock.recv(1024)

			response = run_command(cmd_bfr)
			client_sock.send(response)


def server_loop():
	global target

	if not len(target):
		target = "0.0.0.0"

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((target, port))
	server.listen(5)

	while True:
		client_sock, addr = server.accept()
		client_thread = threading.Thread(target=client_handler, args=(client_sock,))
		client_thread.start()



def run_command(command):
	#strip the new line
	command = command.rstrip()

	try:
		output = subprocess.check_output(command, stderr=subprocess.STDOUT,shell=True)
	except Exception, e:
		output = "Failed to execute the fuckin' command"

	return output



def main():
	global listen
	global port
	global upload_dest
	global execute
	global target
	global command

	if not len(sys.argv[1:]):
		usage()

	try:
		opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu", ['help', 'listen', 'execute', 'target','port','command', 'upload'])
	except getopt.GetoptError as err:
		print err
		usage()

	for o, a in opts:
		if o in ('-l', '--listen'):
			listen = True
		elif o in ('-h', '--help'):
			usage()
		elif o in ('-e', '--execute'):
			execute = a
		elif o in ('-p', '--port'):
			port = int(a)
		elif o in ('-u', '--upload'):
			upload_dest = a
		elif o in ('-c', '--command'):
			command = True
		elif o in ('-t', '--target'):
			target = a
		else:
			print "What exactly are you tryna do motherfucker?"
			assert False, "Unhandled option"

	if not listen and len(target) and port > 0:
		bfr = sys.stdin.read()
		client_sender(bfr)

	if listen:
		server_loop()


if __name__ == '__main__':
	main()