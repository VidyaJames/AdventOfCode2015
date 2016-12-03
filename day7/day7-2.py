f = open('day7-input.txt', 'r')
lines = f.readlines()
signals = {}


def parseLine(line, index):
	instructions = line.split(" ")
	if instructions[0].isdigit() and len(instructions) == 3:
		signals[instructions[2].rstrip()] = int(instructions[0])
	else:
		logic = instructions[0:instructions.index("->")]
		signals[instructions[-1].rstrip()] = logic
	return index + 1

def setCommand(command):
	if command.isdigit():
		return int(command)
	return runInstructions(signals[command], command)

def runInstructions(instructions, key):
	if not isinstance(instructions, list):
		return instructions
	elif len(instructions) == 1:
		signals[key] = runInstructions(signals[instructions[0]], instructions[0])
	elif instructions[0] == "NOT":
		signals[key] = ~runInstructions(signals[instructions[1]], instructions[1]) & 0xffff
	elif instructions[1] == "LSHIFT":
		signals[key] = setCommand(instructions[0]) << int(instructions[2])
	elif instructions[1] == "RSHIFT":
		signals[key] = setCommand(instructions[0]) >> int(instructions[2])
	elif instructions[1] == "AND":
		signals[key] = setCommand(instructions[0]) & setCommand(instructions[2])
	elif instructions[1] == "OR":
		signals[key] = setCommand(instructions[0]) | setCommand(instructions[2])
	return signals[key]
	
i = 0
while i < len(lines):
	i = parseLine(lines[i], i)
signals['b'] = 956

for i in signals:
	signals[i] = runInstructions(signals[i],i)
print "The signal provided to 'a' is " + str(signals['a']) + "."
