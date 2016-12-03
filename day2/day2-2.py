f = open('day2-input.txt','r')
sum = 0
for i in f.readlines():
	l, w, h = i.split("x")
	l = int(l)
	w = int(w)
	h = int(h)
	smallest = min(l, w, h)
	middle = sorted([l,w,h])[1]
	length = 2 * smallest + 2 * middle
	bow = l * w * h
	sum = sum + length + bow
print "total ribbon needed is " + str(sum)
		
