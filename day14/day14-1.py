f = open('day14-input.txt', 'r')

reindeer = []
speeds = {}
stamina = {}
resttime = {}
distance = {}

for i in f.readlines():
	i = i.split(" ")
	reindeer.append(i[0])
	speeds[i[0]] = int(i[3])
	stamina[i[0]] = int(i[6])
	resttime[i[0]] = int(i[6]) + int(i[13])
	distance[i[0]] = 0

i = 0
while i < 2503:
	for j in reindeer:
		if i % resttime[j] < stamina[j]:
			distance[j] += speeds[j]
	i += 1

best = 0
for i in reindeer:
	if distance[i] > best:
		best = distance[i]
print "The winning reindeer travelled " + str(best) + "km."
