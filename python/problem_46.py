from math import sqrt

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

def get_lower_squares(n):
	return [x**2 for x in xrange(1,int(sqrt(n))+1)]

def is_goldbach(x, lower_primes):
	for p in lower_primes:
		for s in get_lower_squares(x):
			if x == p + (2*s):
				return True
	return False

def find_non_goldbach_odd_num():
	x = 9 #i.e. 1st odd composite num
	lower_primes = [2,3,5,7]
	while is_goldbach(x,lower_primes):
		x += 2
		while is_prime(x):
			lower_primes.append(x)
			x += 2
	return x

print find_non_goldbach_odd_num()



