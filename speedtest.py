#!/usr/bin/env python3

import time
from ftplib import FTP

ftp = FTP('34.245.75.246')

ftp.login('awsftpuser','precopius')

filename = '/tmp/testfile.txt'
downfile = 'testfile.txt'

localfile = open(filename, 'wb')
start = time.time()
ftp.retrbinary('RETR ' + downfile, localfile, 1024) 
ftp.quit()
end = time.time()
print(end - start)
localfile.close()
