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

def is_reverse_truncatable(number):
	number = str(number)
	if len(number) == 1:
		if is_prime(int(number)):
			return True
		else:
			return False
	else:
		if is_prime(int(number)):
			return is_reverse_truncatable(number[1:])
		else:
			return False

def is_truncatable(number):
	number = str(number)
	if len(number) == 1:
		if is_prime(int(number)):
			return True
		else:
			return False
	else:
		if is_prime(int(number)):
			return is_truncatable(number[:-1])
		else:
			return False

def find_truncatable_primes():
	truncatable_primes = []
	candidate = 11
	while len(truncatable_primes) < 11:
		if is_truncatable(candidate) and is_reverse_truncatable(candidate):
			truncatable_primes.append(candidate)
		candidate += 2
	# new_primes = ['2', '3', '5', '7']
	# while len(new_primes) > 0:
	# 	new_primes = get_new_primes(new_primes)
	# 	truncatable_primes += new_primes
	return truncatable_primes

def get_new_primes(primes):
	new_primes = []
	for p in primes:
		for n in [str(x) for x in xrange(0,10)]:
			if is_prime(int(p+n)) and is_reverse_truncatable(p+n):
				new_primes.append(p+n)
	return new_primes


print sum(find_truncatable_primes())

