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
        time.sleep(0.01)
        val3 = str(getattr(report,'lat',0.0))
        val4 = str(getattr(report,'lon',0.0))
        Data = "Longitude : " + val1 + "\n" \
               "Latitude :  " + val2

        lon.write(Data)
        R = 6371000 # Meters around the earth 
        Latitude1 = math.radians(val1)
        Latitude2 = math.radians(val3)
        Deltalat = math.radians(val3 - val1)
        Deltalong = math.radians(val4 - val2)
        A = math.sin(Deltalat/2) * math.sin(Deltalat/2) + math.cos(Latitude1) * math.cos(Latitude2) * math.sin(Deltalong/2) * math.sin(Deltalong/2)
        C = 2 * math.atan2(math.sqrt(A), math.sqrt(1-a))
        D = R * C
        print(D)

