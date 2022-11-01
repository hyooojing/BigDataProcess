import sys
from datetime import datetime, date

rFile = sys.argv[1]
wFile = sys.argv[2]

list = []
d = []
uberDict = dict()

class uberInfo(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return self.name
	def __repr__(self):
		return "'"+self.name+"'"

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
	key = row[0] + ',' + row[1]
	value = row[2] + ',' + row[3]
	uberDict[uberInfo(key)] = value
for k, v in uberDict.items():
	w.write(str(k) + "\t" + v + "\n")
w.close()
f.close()
