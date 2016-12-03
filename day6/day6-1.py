f = open('day6-input.txt', 'r')
i = 0
grid = []
while i < 1000:
	row = []
	j = 0
	while j < 1000:
		row.append(0)
		j = j + 1
	grid.append(row)
	i = i + 1

for i in f.readlines():
	instructions = i.split(" ")
	if instructions[0] == "turn":
		if instructions[1] == "on":
			rule = 0
		elif instructions[1] == "off":
			rule = 1
	elif instructions[0] == "toggle":
		rule = 2
	if rule < 2:
		startCoord = instructions[2].split(",")
		endCoord = instructions[4].split(",")
	elif rule == 2:
		startCoord = instructions[1].split(",")
		endCoord = instructions[3].split(",")
	j = int(startCoord[1]) 
	while j <= int(endCoord[1]):
		k = int(startCoord[0])
		while k <= int(endCoord[0]):
			if rule == 0:
				grid[j][k] = 1
			elif rule == 1:
				grid[j][k] = 0
			elif rule == 2:
				if grid[j][k] == 0:
					grid[j][k] = 1
				elif grid[j][k] == 1:
					grid[j][k] = 0
			k = k + 1
		j = j + 1

counter = 0
for i in grid:
	counter = counter + i.count(1)
print "There are " + str(counter) + " lights on."
