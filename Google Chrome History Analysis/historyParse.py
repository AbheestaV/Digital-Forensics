#!/usr/bin/python

import sqlite3 
import sys
import re
import datetime

calend = {
	 	'01': "Jan",
		'02': "Feb",
		'03': "Mar",
		'04': "Apr",
		'05': "May",
		'06': "Jun",
		'07': "Jul",
		'08': "Aug" ,
		'09': "Sep",
		'10': "Oct",
		'11': "Nov",
		'12': "Dec"
		}
numargs = len(sys.argv)
if(numargs!=2):
    print("Error! - No History File Specified!")
    exit()
try:
	foo = sqlite3.connect(sys.argv[1])
except:
    print("Error! - File Not Found!")
    exit()

print("Source File:", sys.argv[1])
#foo = sqlite3.connect(sys.argv[1])
try:
    comms = foo.cursor()
    comms.execute("SELECT COUNT (DISTINCT id) FROM downloads")
    fs = comms.fetchone()

    print("Total Downloads:", fs[0])

    comms.execute("SELECT current_path, received_bytes from downloads ORDER BY (end_time - start_time) DESC LIMIT 1")
    fs = comms.fetchone()
    file = fs[0].split("\\")

    print("File Name:", file[-1])
    print("File Size:", fs[1])

    comms.execute("SELECT COUNT(DISTINCT term) FROM keyword_search_terms")
    fs2 = comms.fetchone()

    print("Unique Search Terms:", fs2[0])

    comms.execute("SELECT urls.title, urls.last_visit_time, keyword_search_terms.term from urls INNER JOIN keyword_search_terms ON keyword_search_terms.url_id=urls.id ORDER BY urls.last_visit_time DESC LIMIT 1")
    fs = comms.fetchone()

    print("Most Recent Search:", fs[2])

    comms.execute("SELECT datetime(urls.last_visit_time/1000000 + (strftime('%s', '1601-01-01')), 'unixepoch') from urls INNER JOIN keyword_search_terms ON keyword_search_terms.url_id=urls.id ORDER BY urls.last_visit_time DESC LIMIT 1")
    fs = comms.fetchone()
    #print(fs)
    fst = re.split("[ ]", fs[0])
    #print(fst)
    date = re.split("[- ]",fst[0])
    #print(date)
    time = re.split("[- ]", fs[0])
    #print(time)
    if (date[1] in calend):
        month = calend[time[1]]
    
    print("Most Recent Search Date/Time: ", date[0], "-", month,"-", date[2], " ", time[3], sep='')
        
except:
    print("Error! - File Not Found!")
    exit()


