f = open('day18-input.txt', 'r')

def toggle(lights, x, y):
	neighboursOn = 0
	neighbours = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
	i = 0
	if x == 0:
		 while i < len(neighbours):
			if neighbours[i][0] == x - 1:
				neighbours.remove(neighbours[i])
			else:
				i += 1
	elif x == len(lights) - 1:
		while i < len(neighbours):	
			if neighbours[i][0] == x + 1:
				neighbours.remove(neighbours[i])
			else:
				i += 1
	i = 0
	if y == 0:
		while i < len(neighbours):
			if neighbours[i][1] == y - 1:
				neighbours.remove(neighbours[i])
			else:
				i += 1
	elif y == len(lights) - 1:
		while i < len(neighbours):
			if neighbours[i][1] == y + 1:
				neighbours.remove(neighbours[i])
			else:
				i += 1
	for i in neighbours:
		if lights[i[1]][i[0]] == '#':
			neighboursOn += 1
	if lights[y][x] == '#' and neighboursOn > 1 and neighboursOn < 4 or lights[y][x] == '.' and neighboursOn == 3:
		return '#'
	else:
		return '.'

lights = []
for i in f.readlines():
	lights.append(i[:-1])
lights.reverse()

i = 0
while i < 100:
	newlights = []
	j = 0
	while j < len(lights):
		newline = ""
		k = 0
		while k < len(lights):
			newline += toggle(lights, k, j)
			k += 1
		newlights.append(newline)
		j += 1
	lights = newlights
	i += 1

lightsOn = 0
for i in lights:
	lightsOn += i.count('#')
print "There are " + str(lightsOn) + " lights on."
