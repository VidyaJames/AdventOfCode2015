import hashlib
done = 0
counter = 0
base = "yzbqklnj"
while done == 0:
	text = base + str(counter)
	hashed = hashlib.md5(text).hexdigest()
	if hashed[0:5] == "00000":
		print "The code is " + str(counter)
		done = 1
	counter = counter + 1
