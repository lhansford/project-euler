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

def get_prime_factors(n):
	if is_prime(n):
		return [n]
	else:
		div = 2
		while n % div != 0:
			div += 1
			while not is_prime(div):
				div +=1
		return [div] + get_prime_factors(n/div)

def place_powers(factors):
	pfs = {}
	for f in factors:
		if pfs.get(f) == None:
			pfs[f] = 1
		else:
			pfs[f] += 1
	return [(k,pfs[k]) for k in pfs.keys()]

def has_distinct_prime_factors(x,n):
	all_pfs = []
	for y in xrange(0,n):
		if is_prime(x+y):
			return False
		pfs = get_prime_factors(x + y)
		if len(place_powers(pfs)) != n:
			return False
		for f in place_powers(pfs):
			if f in all_pfs:
				return False
			all_pfs.append(f)
	return True


def find_n_ints_distinct_prime_factors(n):
	x = 2
	while not has_distinct_prime_factors(x,n):
		x+=1
	return x

print find_n_ints_distinct_prime_factors(4)