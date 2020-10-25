#!/usr/bin/env python3

import matplotlib
matplotlib.use('Agg')
from pylab import rcParams
rcParams['figure.figsize'] = 30, 12

import mysql.connector
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import MinuteLocator, DayLocator, HourLocator, DateFormatter, drange
import argparse
import socket

parser 			= argparse.ArgumentParser()
parser.add_argument("-f",  "--outfile",  default="test.png", help="the output filename")
args = parser.parse_args()

sql_host 	 	= "speedtester.c6gl0ojvhvge.ap-southeast-2.rds.amazonaws.com"
sql_user 	 	= "dz"
sql_password 	= "precopius"
sql_database 	= "speedtester"
outfn			= args.outfile

download_speed 	= []
time_index 		= []

mydb = mysql.connector.connect(host=sql_host, user=sql_user, password=sql_password, database=sql_database)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM speed_data where date(datetime) = '2020-10-23';")

myresult = mycursor.fetchall()
max_speed = 0
for x in myresult:
	speed = float(x[4])
	download_speed.append(speed)

	if speed > max_speed:
		max_speed = speed
		
	time_index.append(x[5])

fig, ax = plt.subplots()
lines = ax.plot(time_index, download_speed,'b-')
ax.xaxis.set_major_locator(MinuteLocator(interval=2))

ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))

for label in ax.xaxis.get_ticklabels():
	label.set_rotation(45)

plt.ylim(0, max_speed *1.3)
plt.xlabel("Time")
plt.ylabel("Megabytes per second")
plt.grid(b=True, which='both', color='0.65',linestyle='-')
ax.set_facecolor('xkcd:eggshell')
plt.title("Download Speeds From North Virginia (Megabyte Per Second) On 10/23/2020", fontweight='bold')

if socket.gethostname() == "cortona":
	save_dir = '/var/www/html/speedtest/images/'
else:
	save_dir = '/var/www/html/speedtest/images/'

sp_task = save_dir+outfn

plt.savefig(sp_task)
