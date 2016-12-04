f = open('day8-input.txt', 'r')

codeSum = 0
stringSum = 0

for i in f.readlines():
	codeSum = codeSum + len(i) - 1
	j = 1
	while j < len(i) - 2:
		if i[j] == '\\':
			if i[j+1] == '"' or i[j+1] == '\\':
				j = j + 1
			else:
				j = j + 3
		j = j + 1 
		stringSum = stringSum + 1
print "The total size is " + str(codeSum - stringSum) + "."
