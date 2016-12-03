f = open('day5-input.txt', 'r')
counter = 0
for i in f.readlines():
	rule1 = 0
	j = 0
	while j < len(i) - 3:
		check = i[j] + i[j+1]
		if check in i[j+2:]:
			rule1 = 1
			j = len(i)
		j = j + 1

	rule2 = 0
	j = 0
	while j < len(i) - 2:
		if i[j] == i[j+2]:
			rule2 = 1
			j = len(i)
		j = j + 1

	if rule1 == 1 and rule2 == 1:
		counter = counter + 1
print "There are " + str(counter) + " nice strings."
