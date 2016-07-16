import serial
import numpy as np
import time

urg = serial.Serial('/dev/tty.usbmodem1461',192000, timeout = 1.5)
urg.write("SCIP2.0\n")
mes1 = urg.readline()
mes2 = urg.readline()
print mes1
print mes2
def get_dist():
   urg.write("MD0384038400001\n")
   time.sleep(0.2)
   hoge = urg.readline()
   hoge2 = urg.readline()
   global dist
   dist = urg.readline()
   global dist2
   dist2 = urg.readline()
   global dist3
   dist3 = urg.readline()
   global dist4
   dist4 = urg.readline()
   time.sleep(0.2)
   print dist4
while 1:
    get_dist()
    if dist2 == "99b\n":
        get_dist()
        dist_data_list = list(dist4)
        dist_data_list_ascii = map(ord,dist_data_list)
        dist_data_list_dec = map(lambda x:x-0x30,dist_data_list_ascii)
        dist_data_list_bin = map(lambda y:format(y,'b'),dist_data_list_dec)

        dist_bin = "".join(dist_data_list_bin[:3])
#dist_bin = "0b" + dist_bin
        distance = int(dist_bin,2)


        print distance 
        time.sleep(0.2)
urg.write("QT\n")
urg.close()
