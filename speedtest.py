#!/usr/bin/env python3
import random
import os
import string
from ftplib import FTP
import time

ftp = FTP('34.245.75.246')
ftp.login(user='awsftpuser', passwd='precopius')
filename = '/tmp/testfile.txt'
localfile = open(filename, 'w')
start = time.time()
ftp.retrlines('RETR ' + filename, localfile.write)
end = time.time()
print(end - start)
ftp.quit()
localfile.close()
