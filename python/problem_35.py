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

def get_iterations(n):
	n = str(n)
	iterations = []
	while n not in iterations:
		iterations.append(n)
		n = n[1:] + n[:1]
	return [int(x) for x in iterations]

def get_circular_primes(limit):
	count = 1 # Count 2
	for x in xrange(3,limit+1, 2):
		if is_prime(x):
			if False not in [is_prime(i) for i in get_iterations(x)]:
				count += 1
	return count

print get_circular_primes(1000000)
