
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

#Bisection search by Geyang
def bisearch(nums, key):
	if (key > nums[-1]) or (key < nums[0]):
		print "Not Found"
	else:
		if nums[len(nums)/2] == key:
			print "Found"
		else:
			if nums[len(nums)/2] < key:
				bisearch(nums[len(nums)/2:],key)
			else:
				bisearch(nums[0:len(nums)/2],key)

bisearch([1, 5, 7, 9, 10, 13, 17, 19, 27],27) 

