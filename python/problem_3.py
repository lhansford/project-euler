def get_prime_factors(number):
	factors = []
	div = 2
	while number > 1:
		while number % div == 0:
			factors.append(div)
			number /= div
		div = div + 1
	return factors

print(get_prime_factors(600851475143))