#!/usr/bin/env python3
import random
import os
import string
import subprocess

testfile = "/tmp/testfile.txt" 
pemfile = "/home/dz/speedtest/speedtester.pem"

def do_test(location, ip):
	print("Copying Test File To {0}".format(location))
	host = "stu2@{0}:~".format(ip)
	result = subprocess.run(["scp", "-v", testfile, host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
	list_of_words = result.stderr.split()
	mbs = float(list_of_words[list_of_words.index("Bytes") + 4][:-1]) / 1e6
	print("Upload Speed To {1} AWS: {0:0.4} Megabytes per second".format(mbs, location))

if os.path.isfile(testfile):
	os.remove(testfile)

f = open(testfile, "a")

print("Creating Test File")
for i in range(int(1e4)):
	line = ""
	for j in range(int(1e3)):
		line = line + random.choice(string.ascii_letters)
	f.write(line)
f.close()

do_test("Sydney Australia", "3.26.55.166")
do_test("North Virginia", "54.157.129.155")
do_test("Ireland", "34.245.75.246")
