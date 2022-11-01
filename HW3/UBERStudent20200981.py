import sys
from datetime import datetime, date

rFile = sys.argv[1]
wFile = sys.argv[2]

list = []
d = []
uberDict = dict()

def what_day(date):
	days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
	day = date.weekday()
	return days[day]

f = open(rFile, "rt")
w = open(wFile, "wt")

for line in f:
	uber = line.split(',')
	ubers = uber[3].split('\n')
	uber[3] = ubers[0]	
	list.append(uber)
for row in list:
	d = row[1].split('/')
	row[1] = what_day(date(int(d[2]), int(d[0]), int(d[1])))
	key = (row[0], row[1])
	d[1] = int(row[2])
	d[2] = int(row[3])
	value = [d[1], d[2]]
	if uberDict.get(key):
		uberDict[key][0] += d[1]
		uberDict[key][1] += d[2]
	else:
		uberDict[key] = value
for k, v in uberDict.items():
	w.write("%s,%s" %(k[0], k[1]))
	w.write(" %d,%d\n" %(v[0], v[1]))

w.close()
f.close()
