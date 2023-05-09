#!/usr/bin/python
import exifread
import sys
import logging
from exifread import process_file, exif_log
import math


llsplargs = len(sys.argv)
if (llsplargs != 2):
    print("Error! - No Image File Specified!")
    exit()

fp = sys.argv[1]
try:
    file = open(fp, 'rb')
except:
    print("Error! - File Not Found!")
    exit()

'''
arr=[
    'Make',
    'Model',
    'DateTime',
    'GPSLatitude',
    'GPSLongitude'
     ]
'''
arr = [
    'Make', 'Model', 'DateTime', 'GPSLatitude', 'GPSLongitude'
]

foo = process_file(file)

datakeys = list(foo.keys())
datakeys.sort()

print("Source File:", sys.argv[1])

for i in datakeys:
    #
	if ('Image' in i):
		if(i[6::] in arr and i[6::] == 'DateTime'):
			t1 = foo[i].printable
		elif(i[6::] in arr):
			print(i[6::], ": ", foo[i].printable, sep='')
    #
    
print("Original Date/Time:", t1)

for i in datakeys:
    
    if('GPS' in i):
        if(i[4::] == 'GPSLatitudeRef'):
            latitude = foo[i].printable
        if(i[4::] == 'GPSLongitudeRef'):
            longitude = foo[i].printable
            
            
for i in datakeys:
    #
	if ('GPS' in i and i[4::] in arr):
		latlong = foo[i].printable.strip('][').split(', ')

		llspl = latlong[1].split('/')

		z = len(llspl)
		y = 0

		if(z > 1):
			y = float(float(llspl[0])/float(llspl[1]))

		latlongspl = latlong[2].split('/')

		w = len(latlongspl)
		x = 0

		if(w > 1):
			x = float(float(latlongspl[0])/float(latlongspl[1]))

		if((i[4::] == 'GPSLatitude' and latitude == 'S') or (i[4::] == 'GPSLongitude' and longitude == 'W')):
			if (x != 0 and y == 0):
				print(i[7::], ": -", latlong[0], " degrees, ",
						float(latlong[1]), " minutes, ", x, " seconds", sep='')
    
			elif(x != 0 and y != 0):
				print(i[7::], ": -", latlong[0], " degrees, ",
						float(y), " minutes, ", x, " seconds", sep='')
    
			elif(x == 0 and y != 0):
				print(i[7::], ": -", latlong[0], " degrees, ", float(y),
						" minutes, ", latlong[2], " seconds", sep='')
    
			else:
				print(i[7::], ": -", latlong[0], " degrees, ", float(latlong[1]),
						" minutes, ", latlong[2], " seconds", sep='')
    
		elif(i[4::] == 'GPSLatitude' and latitude == 'N') or (i[4::] == 'GPSLongitude' and longitude == 'E'):
			if (x != 0 and y == 0):
				print(i[7::], ": ", latlong[0], " degrees, ", float(
					latlong[1]), " minutes, ", x, " seconds", sep='')
    
			elif(x != 0 and y != 0):
				print(i[7::], ": ", latlong[0], " degrees, ", float(
					y), " minutes, ", x, " seconds", sep='')
    
			elif(x == 0 and y != 0):
				print(i[7::], ": ", latlong[0], " degrees, ", float(
					y), " minutes, ", latlong[2], " seconds", sep='')
    
			else:
				print(i[7::], ": ", latlong[0], " degrees, ", float(
					latlong[1]), " minutes, ", latlong[2], " seconds", sep='')
    
    #