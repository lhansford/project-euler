def find_quadratic_primes(limit):
	best = 0
	best_a,best_b = 0,0
	for a in xrange(0,limit):
		for b in xrange(0,limit):
			result = test_quadratic(a,b)
			if result > best:
				best = result
				best_a,best_b = a,b
			result = test_quadratic(-a,b)
			if result > best:
				best = result
				best_a,best_b = -a,b
			result = test_quadratic(a,-b)
			if result > best:
				best = result
				best_a,best_b = a,-b
			result = test_quadratic(-a,-b)
			if result > best:
				best = result
				best_a,best_b = -a,-b
	return best, best_a, best_b

def test_quadratic(a,b):	
	n = 0
	while is_prime(quadratic(a,b,n)):
		n += 1
	return n

def quadratic(a,b,n):
	return (n*n) + (a*n) + b

def is_prime(number):
	if number > 1:
		if number == 2:
			return True
		if number % 2 == 0:
			return False
		for current in range(3, int(number**0.5 + 1), 2):
			if number % current == 0: 
				return False
		return True
	return False

seq,a,b = find_quadratic_primes(1000)
print seq,a,b
print a*b