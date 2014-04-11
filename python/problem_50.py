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

def get_longest_prime(limit):
	sums = []
	p_gen = prime_gen()
	first = p_gen.next()
	while first < limit:
		primes = [first]
		p_gen2 = prime_gen(first+1)
		next = p_gen2.next()
		while sum(primes) + next < limit:
			primes.append(next)
			if len(sums) < len(primes) and sum(sums) < sum(primes) and is_prime(sum(primes)):
				sums = primes[:]
			next = p_gen2.next()
		first = p_gen.next()
	return sum(sums), sums

print get_longest_prime(1000000)
