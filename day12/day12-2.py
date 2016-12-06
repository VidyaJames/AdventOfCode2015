import json
def parse(data):
	total = 0
	if isinstance(data, dict):
		if "red" in data.values():
			return 0
		for i in data:
			total += parse(data[i])
	elif isinstance(data, list):
		for i in data:
			total += parse(i)
	elif isinstance(data, int):
		return total + data
	return total

with open('day12-input.txt') as dataFile:
	data = json.load(dataFile)
total = 0
total = parse(data)
print "The total of all numbers in the JSON is " + str(total) + "."
