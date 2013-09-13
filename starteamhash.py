#!/usr/bin/python

#Starteamhash.py is a small python application that reverses the hash of a user as found in the database of Borland StarTeam
#
#    Copyright (C) 2013  Bart Leppens (@bmantra)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import re


def printUsage():
	print("\nThis program is free software: you can redistribute it and/or modify \nit under the terms of the GNU General Public License as published by\nthe Free Software Foundation, either version 3 of the License, or\n(at your option) any later version.\n\nThis program is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\nGNU General Public License for more details.\n\nYou should have received a copy of the GNU General Public License\nalong with this program.  If not, see <http://www.gnu.org/licenses/>.\n\n")
	print("Usage: %s 0x6461686C6BFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFAFA" % str(sys.argv[0]))

		
args = len(sys.argv)

if args > 1:
	hashedvalue = str(sys.argv[1])
	#check if argument is valid 
	matchObj = re.match( r'^(0x)?[0-9A-F][0-9A-F][0-9A-F]*$', hashedvalue, re.I)
	if matchObj:	
		#get 2 last characters
		padding = hashedvalue[-2:]
		#convert to int
		padding = int(padding, 16)
		
		#from the padding we can deduct the length of the password
		#length = FF - padding
		passwordlength = 255 - padding
		
		#strip leading 0x
		if hashedvalue[:2] == "0x":
			hashedvalue = hashedvalue[2:]
		#remove padding (2 characters are used per byte in the DB)
		hashedvalue = hashedvalue[:passwordlength * 2]
		
		while(len(hashedvalue) > 1):
			#take byte (represented as 2 characters in the DB)
			currentbyte = hashedvalue[0:2]
			currentbyte = int(currentbyte, 16)
			#xor of the current byte with the password length
			currentbyte = currentbyte ^ passwordlength
			print ("%s" % chr(currentbyte), end='')
			
			#proceed to next byte (=next 2 characters)
			hashedvalue = hashedvalue[2:]
	else:
		printUsage()
else:		
	printUsage()
