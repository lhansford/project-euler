import math
from collections import Counter

def triangle_number_generator():
	nth = 1
	num = 1
	while True:
		yield num
		nth += 1
		num += nth

def prime_generator(number):
    while True:
        if is_prime(number):
            yield number
        number += 1

def is_prime(number):
	if number > 1:
		if number == 2:
			return True
		if number % 2 == 0:
			return False
		for current in range(3, int(math.sqrt(number) + 1), 2):
			if number % current == 0: 
				return False
		return True
	return False

def get_number_of_factors(num):
	num_divisors = 0
	for divisor in xrange(1, num+1):
		if num % divisor == 0:
			num_divisors += 1
	return num_divisors

def get_number_of_factors_with_pf(num):
	num_divisors = 1
	prime_factorisation = Counter(get_prime_factorisation(num))
	for x in prime_factorisation:
		num_divisors *= (prime_factorisation[x] + 1)
	return num_divisors

def get_prime_factorisation(num):
	prime_factorisation = []
	p_gen = prime_generator(0)
	prime = p_gen.next()
	if num < prime:
		return []
	while num % prime != 0:
		prime = p_gen.next()
	prime_factorisation.append(prime)
	if prime == num:
		return prime_factorisation
	elif is_prime(num/prime):
		prime_factorisation.append(num/prime)
		return prime_factorisation
	else:
		return prime_factorisation + get_prime_factorisation(num/prime)
	return prime_factorisation

def first_triangle_number_with_over_n_divisors(n):
	generator = triangle_number_generator()
	num_divisors = 0
	while num_divisors < n:
		tri_num = generator.next()
		print tri_num
		num_divisors = get_number_of_factors_with_pf(tri_num)
	return str(tri_num) + " is the first triangle number with over " + str(n) + " divisors."

print first_triangle_number_with_over_n_divisors(500)