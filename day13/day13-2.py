import itertools
f = open('day13-input.txt', 'r')

happiness = {}
guestlist = []
guestlist.append("Jamie")

for i in f.readlines():
	gain = -1
	i = i.split(" ")
	if i[0] not in guestlist:
		guestlist.append(i[0])
	if i[2] == "gain":
		gain = 1
	happiness[(i[0], i[10][0:-2])] = int(i[3]) * gain

for i in guestlist:
	happiness[("Jamie", i)] = 0
	happiness[(i, "Jamie")] = 0

perms = itertools.permutations(guestlist)

best = 0
for i in list(perms):
	j = 0
	total = 0
	while j < len(i) - 1:
		total += happiness[(i[j],i[j+1])] + happiness[(i[j + 1],i[j])]
		j += 1
	total += happiness[(i[j],i[0])] + happiness[(i[0],i[j])]
	if total > best:
		best = total
print "The total change in happiness for the optimal seating arrangement is " + str(best) + "."
