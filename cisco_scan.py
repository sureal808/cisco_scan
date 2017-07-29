#!/usr/bin/env python
#
# Python Cisco Scanner
#

from socket import *
import threading

print "Cisco Router Scanner."
target,output = (raw_input("Class C IP: "), raw_input("Logfile: "))
f = open(output, 'w')

for i in range(1, 255):
	t = target + '.' + str(i)
	setdefaulttimeout(0.5)
	s = socket(AF_INET,SOCK_STREAM)
	try: 
		print "Trying %s\r" % (t,)
		s.connect((t, 22))
		data = s.recv(3)
		s.close()
		print t
		print data
		if data == "":		
			f.write("Cisco router found at: %s\n" % (t,))
	except Exception,e:
		s.close()
f.close()
