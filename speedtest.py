#!/usr/bin/env python3

import ftplib 
import os

with ftplib.FTP('34.245.75.246', 'awsftpuser', 'precopius') as ftp:

	file_orig = '/testfile.txt'
	file_copy = '/tmp/testfile.txt'

	try:
		ftp.login()  
		
		with open(file_copy, 'w') as fp:
			
			res = ftp.retrlines('RETR ' + file_orig, fp.write)
			
			if not res.startswith('226 Transfer complete'):
				
				print('Download failed')
				if os.path.isfile(file_copy):
					os.remove(file_copy)

	except ftplib.all_errors as e:
		print('FTP error:', e) 
		
		if os.path.isfile(file_copy):
			os.remove(file_copy)
