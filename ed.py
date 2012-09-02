#!/usr/bin/env python
import signal
import random
def handler(o, b):
	# do NOTHING
	True

signal.signal(signal.SIGQUIT, handler)
while random.randint(0,1000) != 6:
	try:
		raw_input()
		print "?"
	except:
		print "\n?"
		continue
