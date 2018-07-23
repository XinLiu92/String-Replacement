#!/usr/bin/python

import os

path = raw_input("File location with path:" )


find = raw_input("Find:")

replace = raw_input("Replace:")


f = open(path,'r+')
contents = f.read()

if find in contents:
	print ("\n********************************************************************************")
	newdata = contents.replace(find, replace)
	f.close()
	f = open(path,'w+')
	f.write(newdata)
	replaced = f.read()
	f.close
else:
	print("STRING NOT FOUND\n")
	f.close()

#regex version
shake = open(path,'r+')
S1_IP = ' 8.8.8.8/21'
s1 = 'ip:'+S1_IP
file = open(path,'a')
file.write(re.sub(r'ip:(.*)',s1,shake.read()))
	#may need to change imsi later
shake.close()
file.close()

