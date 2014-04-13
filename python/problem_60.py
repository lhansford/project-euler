from itertools import combinations

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

def prime_gen(num=2):
	while True:
		if is_prime(num):
			yield num
		num += 1

def get_all_primes(start,limit):
	primes = []
	p_gen = prime_gen(start)
	p = p_gen.next()
	while p < limit:
		primes.append(p)
		p = p_gen.next()
	return primes

def concatenates(combo):
	for a in combo:
		for b in combo:
			if a != b and not is_prime(int(str(a) + str(b))):
				return False
	return True

def find_concatenating_primes(n, test_range):
	combos = []
	primes = get_all_primes(2,test_range)
	for c in combinations(primes, n):
		if concatenates(c):
			combos.append(c)
	return combos

print find_concatenating_primes(5, 10000)