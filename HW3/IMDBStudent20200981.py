import sys

rFile = sys.argv[1]
wFile = sys.argv[2]
gList = []
dict = {}

f = open(rFile, "rt")
w = open(wFile, "wt")
for line in f:
	movie = line.split('::')
	genres = movie[2].split('\n')
	genre = genres[0].split('|')
	for g in genre:
		gList.append(g)
print(gList)
for i in gList:
	if dict.get(i): 
		dict[i] += 1
	else:
		dict[i] = 1
for key, value in dict.items():
	w.write(key + " " + str(value) + "\n")
w.close()
f.close()
	
