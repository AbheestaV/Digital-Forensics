#!/usr/bin/python

import csv
import sys
import datetime
import re
import operator
integ = 0
k = 0

numarg = len(sys.argv)
if numarg != 2:
    print("Error! - No Log File Specified!")
    exit()
try:
    with open(sys.argv[1]) as csv_file0:
        flag=0
except:
    print("Error! - File Not Found!")
    
with open(sys.argv[1]) as csv_file:
    csvfile = csv.reader(csv_file, delimiter=',')
    iparr = []
    dicts = []

    print("Source File:", sys.argv[1])
    for row in csvfile:
        if(row[4] in ['1337', '1338', '1339', '1340']):
            if (row[1] not in iparr):
                iparr.append(row[1])
            if (row[2] not in dicts and row[1] in iparr):
                dicts.append(row[2])
            if(k == 0):
                k = row[0]

    parr = []

    for i in iparr:
        parr.append(i.split("."))

    parr.sort(key=lambda parr: int(parr[3]))

    dictf = []

    for i in parr:
        s = "."
        s = s.join(i)
        dictf.append(s)

    print("Systems Infected:", len(dictf))

    print("Infected System IPs: ", dictf)

    print("C2 Servers:", len(dicts))

    dictf.clear()

    parr.clear()

    for w in dicts:
        parr.append(w.split("."))

    parr.sort(key=operator.itemgetter(1, 2, 3))

    for p in parr:
        x = "."
        x = x.join(p)
        dictf.append(x)

    print("C2 Server IPs: ", dictf)

    conntime = datetime.datetime.utcfromtimestamp(
        float(k)).strftime('%Y-%m-%d %H:%M:%S')
    #print(conntime)
    # print(conntime[0])
    # print(conntime[5]+conntime[6])
    c2connf = re.split("[ ]", conntime)
    #print("c2connf[0] is",c2connf[0])
    calend = {
        '01': "Jan",
        '02': "Feb",
        '03': "Mar",
        '04': "Apr",
        '05': "May",
        '06': "Jun",
        '07': "Jul",
        '08': "Aug",
        '09': "Sep",
        '10': "Oct",
        '11': "Nov",
        '12': "Dec"
    }
    c2connf0 = c2connf[0]
    #print("c2connf0 ", c2connf0)
    c2connf1 = c2connf[1]
    #print("c2connf1 ", c2connf1)
    a = c2connf0[5]+c2connf0[6]
    #print("Month is ", a)
    if (a in calend):
        month = calend[a]
    #print(c2connf)
    #print("Month is: ", month)
    print("First C2 Connection: ", c2connf0[0], c2connf0[1], c2connf0[2],
          c2connf0[3], "-", month, "-",c2connf0[8],c2connf0[9]," ", c2connf1, " ", "UTC", sep='')

    csv_file.seek(0)

    ipdict = {}

    for row in csvfile:
        if((row[2] in dictf) and (row[2] not in ipdict.keys())):
            ipdict[row[2]] = int(row[5])
        elif(row[2] in ipdict.keys() and (row[2] in dictf)):
            ipdict[row[2]] = ipdict[row[2]] + int(row[5])

    fdict = sorted(ipdict.items(), key=operator.itemgetter(1), reverse=True)

    print("C2 Data Totals:", fdict)
