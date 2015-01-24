
#Float point accuracy
def floatPointAccuracy():
	a = 1.22222222
	b = 1.22223423
	c = 3
	def equal(int1, int2):
		return ((int1-int2)*(int1-int2)) < 0.00001
	print a == b
	print equal(b,a)
#floatPointAccuracy()


