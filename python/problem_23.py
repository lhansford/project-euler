def find_abundant_numbers(limit):
	return [x for x in xrange(1,limit) if is_abundant_number(x)]

def is_abundant_number(n):
	if sum(get_divisors(n)) > n:
		return True
	return False

def get_divisors(n):
	"""Get nums less than n which divide evenly into n (i.e. proper divisors)"""
	divisors = []
	for x in xrange(1, int(n**0.5)+1):
		if n % x == 0:
			divisors.append(x)
			if n/x != x and x != 1:
				divisors.append(n/x)
	return divisors

def find_sum_of_abundant_numbers(limit):
	abundant_sums = {x:False for x in xrange(1,limit)}
	abundant_numbers = find_abundant_numbers(limit)
	for x in abundant_numbers:
		for y in abundant_numbers:
			if (x+y) < limit:
				abundant_sums[x+y] = True
	return abundant_sums

limit = 28123
abundant_sums = find_sum_of_abundant_numbers(limit)
print sum([x for x in xrange(1, limit) if not abundant_sums[x]])