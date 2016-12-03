f = open('day5-input.txt', 'r')
banned = ['ab', 'cd', 'pq', 'xy']
vowels = "aeiou"
counter = 0
for i in f.readlines():
	if any(j in i for j in banned):
		continue
	j = 0

	double = 0
	while j < len(i) - 1:
		if i[j] == i[j+1]:
			double = 1
			j = len(i)
		j = j + 1

	vowelCount = 0
	for j in i:
		if j in vowels:
			vowelCount = vowelCount + 1

	if vowelCount > 2 and double == 1:
		counter = counter + 1
print "There are " + str(counter) + " nice strings."
