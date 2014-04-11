def get_divisors(n):
	"""Get nums less than n which divide evenly into n (i.e. proper divisors)"""
	return [x for x in xrange(1,n) if n % x == 0]

def is_amicable_number(n):
	n_div_sum = sum(get_divisors(n))
	if n == n_div_sum:
		return False
	if n == sum(get_divisors(n_div_sum)):
		return True
	return False

def get_amicable_numbers(limit):
	return [x for x in xrange(1, limit) if is_amicable_number(x)]

print sum(get_amicable_numbers(10000))