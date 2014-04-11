import math

def get_combinations(n,r):
	return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

def find_combinations_greater_than_x(limit,x):
	count=0
	for n in xrange(1,limit):
		for r in xrange(1,n+1):
			if get_combinations(n,r) > x:
				count+=1
	return count

print find_combinations_greater_than_x(101,1000000)
