f = open('day2-input.txt','r')
sum = 0
for i in f.readlines():
	l, w, h = i.split("x")
	l = int(l)
	w = int(w)
	h = int(h)
	side1 = l * w
	side2 = w * h
	side3 = h * l
	smallest = min(side1, side2, side3)
	area = 2 * side1 + 2 * side2 + 2 * side3 + smallest
	sum = sum + area
print "total wrapping paper needed is " + str(sum)
		
