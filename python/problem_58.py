from __future__ import division

def get_diagonals(previous, level):
	return [x+(((i+1)*2)+(8*(level-1))) for i,x in enumerate(previous)]

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

def determine_prime_ratio(primes):
	num_primes = sum([1 for x in primes if x == True])
	return (num_primes/len(primes)) * 100

def get_ratio_lower_than(limit):
	last_diagonals = [3,5,7,9]
	level = 2
	diagonals = [is_prime(1)] + [is_prime(x) for x in last_diagonals]
	while determine_prime_ratio(diagonals) >= limit:
		last_diagonals = get_diagonals(last_diagonals, level)
		level+=1
		diagonals += [is_prime(x) for x in last_diagonals]
	return last_diagonals[1] - last_diagonals[0] + 1

print get_ratio_lower_than(10)