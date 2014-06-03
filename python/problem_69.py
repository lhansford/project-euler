
def get_greatest_common_divisor(a,b):
	""" Euclidean algorithm - find the gcd of a and b"""
	div = a//b
	remainder = a % b
	while remainder != 0:
		a = b
		b = remainder
		div = a//b
		remainder = a % b
	return b

def get_coprimes(n):
	return [ x for x in range(1,n) if get_greatest_common_divisor(n,x) == 1]

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

def get_prime_product(limit):
	""" Get the product of conescutive primes from 2 that stays under limit """
	p_gen = prime_gen(2)
	prime = next(p_gen)
	result = 1
	while result * prime < limit:
		result *= prime
		prime = next(p_gen)
	return result

print(get_prime_product(1000000))
# print(get_coprimes(get_prime_product(1000000)))