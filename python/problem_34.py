def factorial(n):
	f = 1
	for x in xrange(2,n+1):
		f*=x
	return f

def find_factorial_sums(limit):
	# Max nubmer would be whatever limit for 9! is. Got the answer with 1000000, but dont know what the lower limit would be
	sums = []
	for x in xrange(3,limit):
		if sum([factorial(int(d)) for d in str(x)]) == x:
			sums.append(x)
	return sums

print find_factorial_sums(1000000)