#! /usr/bin/python
 
from gps import *
import time
    
gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE) 

lon = open("/home/pi/Drone/static/long.txt", "r+")
while True:
    report = gpsd.next() #
    if report['class'] == 'TPV':
        lon.seek(0)
        val1 = str(getattr(report,'lat',0.0))
        val2 = str(getattr(report,'lon',0.0))
        print  "longitude : ", val1
        print  "Latitude  : ", val2
        time.sleep(0.1)
        Data = "Longitude : " + val1 + "\n" \
               "Latitude :  " + val2

        lon.write(Data)
