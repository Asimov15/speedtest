#!/usr/bin/env python3

import ftplib 
import os
import string
import time
import shutil
import random

file_orig = 'testfile.txt'
file_copy = '/tmp/testfile.txt'
location  = 'Ireland'

with ftplib.FTP('34.245.75.246') as ftp:

	ftp.set_pasv(False)

	try:
		ftp.login('awsftpuser', 'precopius')  
		
		with open(file_copy, 'wb') as fp:
			start = time.time()
			result = ftp.retrbinary('RETR ' + file_orig, fp.write)
			end = time.time()
			if not result.startswith('226 Transfer complete'):
				print('Download failed')
				if os.path.isfile(file_copy):
					os.remove(file_copy)

	except ftplib.all_errors as e:
		print('FTP error:', e)
		if os.path.isfile(file_copy):
			os.remove(file_copy)

	mbs = 10100000 / (1e6 * (end-start))
	print("Download Speed From {1} AWS: {0:0.4} Megabytes per second".format(mbs, location))

	newfn = ""
	for j in range(10):
		newfn = newfn + random.choice(string.ascii_letters)

	newfn = "./" + newfn + ".st"
	shutil.move(file_copy, newfn)
	upfile = open(newfn,'rb')
	start = time.time()
	result = ftp.storbinary('STOR ' + newfn, upfile)
	end = time.time()

	mbs = 10100000 / (1e6 * (end-start))
	print("Upload Speed To {1} AWS: {0:0.4} Megabytes per second".format(mbs, location))

