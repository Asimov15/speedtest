#!/usr/bin/env python3

import random
import string

testfile = "testfile.txt"

f = open(testfile, "w")
for i in range(int(1e4)):
	line = ""
	for j in range(99):
		line = line + random.choice(string.ascii_letters)
	line = line + '\n'
	f.write(line)
f.close()
