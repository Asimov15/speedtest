#!/usr/bin/env python2

import os
import string
import time
import shutil
from shutil import copyfile
import random
#from pathlib import Path
import mysql.connector
from mysql.connector import Error
from datetime import datetime
#import pysftp
import speedtest 

client_id = '00007'

def nethealth():
	download = st.download()
	upload = st.upload()
	print("Testing Speed To fast.com")
	config = 	{
					'host' : 'speedtester.c6gl0ojvhvge.ap-southeast-2.rds.amazonaws.com',
					'user' : 'dz',
					'password' : 'precopius',
					'database' :'speedtester'
				}
	mydb = mysql.connector.connect(**config)
	mycursor = mydb.cursor()
	sql = """INSERT INTO speed_data (client_id, destination, upload_speed, download_speed, datetime ) VALUES (%s, %s, %s, %s, %s)"""
	recordtuple = (client_id, 'fast.com', upload , download, datetime.utcnow())
	mycursor.execute(sql, recordtuple)
	mydb.commit()

st = speedtest.Speedtest() 
for i in range(int(1e5)):
	nethealth()


