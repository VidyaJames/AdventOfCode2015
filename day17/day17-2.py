import operator
f = open('day17-input.txt', 'r')

sizes = []
used = []
for i in f.readlines():
	sizes.append(i[:-1])
	used.append(0)

numCombs = {}
while used[:-1] != used[1:] or used[0] != 1:
	total = 0
	i = 0
	while i < len(sizes):
		if used[i] == 1:
			total += int(sizes[i])
		if total > 150:
			break
		i += 1
	if total == 150:
		bottles = used.count(1)
		if bottles not in numCombs.keys():
			numCombs[bottles] = 1
		else:
			numCombs[bottles] += 1
	index = len(used) - 1
	while used[index] == 1:
		used[index] = 0
		index -= 1
	used[index] = 1

lowest = min(numCombs.items(), key=lambda x: x[0])[1]
print "There are " + str(lowest) + " different combinations using the smallest number of bottles."
