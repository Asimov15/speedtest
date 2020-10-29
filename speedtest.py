#!/usr/bin/env python3

import os
import string
import time
import shutil
from shutil import copyfile
import random
from pathlib import Path
import mysql.connector
from mysql.connector import Error
from datetime import datetime
import pysftp
import fast_com

client_id = '00001'
send_dir = 'send/'
receive_dir = 'receive/'
sql_host = 'speedtester.c6gl0ojvhvge.ap-southeast-2.rds.amazonaws.com'

def testspeed(ip, location):
	print("Testing Speed To {0}".format(location))
	
	#create name of file to upload
	dateTimeObj = datetime.utcnow()
	timestampstr = dateTimeObj.strftime("%H%M%S%f")
	suffix = "tf" + timestampstr + ".txt"
	newfn = send_dir + suffix
	copyfile(testfile, newfn)
	with pysftp.Connection(ip, username='awsftpuser', password='precopius') as sftp:
		start = time.time()
		sftp.put(newfn) 
		end = time.time()
		os.remove(newfn)
		mbs_up = 1000000 / (1e6 * (end-start))
		print("Up Speed To {1} AWS: {0:0.4} Megabytes per second".format(mbs_up, location))
		newfn = suffix
		start = time.time()
		localpath = receive_dir + newfn
		sftp.get(newfn, localpath)
		end = time.time()
		mbs_down = 1000000 / (1e6 * (end - start))
		print("Download Speed To {1} AWS: {0:0.4} Megabytes per second".format(mbs_down, location))
		mydb = mysql.connector.connect(host="speedtester.c6gl0ojvhvge.ap-southeast-2.rds.amazonaws.com", user="dz", password="precopius", database="speedtester")
		mycursor = mydb.cursor()
		sql = """INSERT INTO speed_data (client_id, destination, upload_speed, download_speed, datetime ) VALUES (%s, %s, %s, %s, %s)"""
		recordtuple = (client_id, location, mbs_up, mbs_down, datetime.utcnow())
		mycursor.execute(sql, recordtuple)
		mydb.commit()
		os.remove(localpath)

if not os.path.exists(send_dir):
	os.mkdir(send_dir)

if not os.path.exists(receive_dir):
	os.mkdir(receive_dir)

testfile = send_dir + "testfile.txt"

if not os.path.exists(testfile):
	f = open(testfile, "w")

	for i in range(int(1e4)):
		line = ""
		for j in range(99):
			line = line + random.choice(string.ascii_letters)
		line = line + '\n'
		f.write(line)
	f.close()

def fast(ip, location):
	result = fast_com.fast_com()
	print(result)

for i in range(int(1e5)):
	#testspeed('34.245.75.246', 'Ireland')
	#testspeed('54.157.129.155', 'North Virginia')
	#time.sleep(10 * 60)
	fast('54.157.129.155', 'North Virginia')
	
