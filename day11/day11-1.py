password = list("vzbxkghb")

rule1 = 0
rule3 = 0

while rule1 == 0 or rule3 == 0:
	index = len(password) - 1
	while password[index] == 'z' and index >= 0:
		password[index] = 'a'
		index -= 1;
	if index >= 0:
		password[index] = chr(ord(password[index]) + 1)
	i = 0
	while i < len(password):
		if password[i] in "iol":
			password[i] = chr(ord(password[i]) + 1)
			j = i + 1
			while j < len(password):
				password[j] = 'a'
				j += 1
		i += 1
	i = 0
	rule1 = 0
	while i < len(password) - 2:
		if ord(password[i]) + 1 == ord(password[i+1]) and ord(password[i]) + 2 == ord(password[i+2]):
			rule1 = 1
		i += 1
	if rule1 == 0:
		continue
	i = 0
	rule3first = 0
	rule3 = 0
	firstChar = '1'
	while i < len(password) - 1:
		if ord(password[i]) == ord(password[i+1]):
			if rule3first == 1 and ord(firstChar) != ord(password[i]):
				rule3 = 1
			else:
				rule3first = 1
				i += 1
				firstChar = password[i]
		i += 1
print "The password is "+  "".join(password) + "."
