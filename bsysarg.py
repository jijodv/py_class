#!/usr/bin/env python
import sys
print ("Name of the script: ", sys.argv[0])
print ("Number of arguments: ", len(sys.argv))
print ("The arguments are: ", str(sys.argv))

if len(sys.argv) is not 2:
	print ("Usage: {} <arg1> <arg2>" .format(str(sys.argv)))
else:
	print ("{} has {} arguments as expected" .format(str(sys.argv[0], str(len(sys.argv)))))
