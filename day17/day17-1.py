f = open('day17-input.txt', 'r')

sizes = []
used = []
for i in f.readlines():
	sizes.append(i[:-1])
	used.append(0)

numCombs = 0
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
		numCombs += 1
	index = len(used) - 1
	while used[index] == 1:
		used[index] = 0
		index -= 1
	used[index] = 1
	
print "There are " + str(numCombs) + " different combinations."
