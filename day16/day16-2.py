goodSue = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}
f = open('day16-input.txt', 'r')

greaterThan = ['cats', 'trees']
lessThan = ['pomeranians', 'goldfish']
for i in f.readlines():
	sue, data = i.split(": ", 1)
	data = data.split(", ")
	bad = 0
	for j in data:
		j = j.split(": ")
		if j[1][-1] == '\n':
			j[1] = j[1][:-1]
		if j[0] in greaterThan:
			if goodSue[j[0]] >= int(j[1]):
				bad = 1
		elif j[0] in lessThan:
			if goodSue[j[0]] <= int(j[1]):
				bad = 1
		elif goodSue[j[0]] != int(j[1]):
			bad = 1
	if bad == 0:
		print sue + " is the Sue who sent the letter."
