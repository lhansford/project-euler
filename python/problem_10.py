def is_prime(number):
		if number < 6 and number in [2,3,5]:
			return True
		if number % 5 == 0 or number % 3 == 0:
			return False
		trial_divider = int(number**0.5)
		if trial_divider % 2 == 0:
			trial_divider -= 1
		while trial_divider > 1:
			if number % trial_divider == 0:
				return False
			trial_divider -= 2
		if trial_divider == 1:
			return True
		print '?'
		return False

def get_primes(limit):
	"""Get all primes below the limit."""
	primes = [2]
	for i in xrange(3, limit, 2):
		if is_prime(i):
			primes.append(i)
	return primes

print sum(get_primes(2000000))