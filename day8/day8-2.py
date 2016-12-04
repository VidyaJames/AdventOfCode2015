f = open('day8-input.txt', 'r')

codeSum = 0
encodeSum = 0

for i in f.readlines():
	codeSum = codeSum + len(i) - 1
	j = 0
	while j < len(i) - 1:
		if i[j] == '"' or i[j] == '\\':
			encodeSum = encodeSum + 1
		encodeSum = encodeSum + 1
		j = j + 1
	encodeSum = encodeSum + 2
print "The total size is " + str(encodeSum - codeSum) + "."
