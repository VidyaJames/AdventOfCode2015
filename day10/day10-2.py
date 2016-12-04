start = "1113222113"
iterations = 50
i = 0
while i < iterations:
	newString = ""
	while start != "":
		first = start[0]
		counter = 0
		for j in start:
			if j == first:
				counter = counter + 1
			else:
				break
		start = start[counter:]
		newString = newString + str(counter)
		newString = newString + first
	start = newString
	i = i + 1
print "The length of the string is " + len(start) + "."
