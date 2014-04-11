import itertools

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

def has_n_prime_values(p, n):
	digits = set([d for d in str(p)])
	for d in digits:
		primes = 0
		for x in xrange(0,10):
			if str(p).replace(d,str(x))[0] != '0' and is_prime(int(str(p).replace(d,str(x)))):
				primes += 1
		if primes == n:
			return True
	return False

def get_n_prime_family(n):
	primes = prime_gen(n)
	p = primes.next()
	while not has_n_prime_values(p,n):
		p = primes.next()
	return p

print get_n_prime_family(8)