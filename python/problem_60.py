from itertools import combinations

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

def get_all_primes(start,limit):
	primes = []
	p_gen = prime_gen(start)
	p = p_gen.next()
	while p < limit:
		primes.append(p)
		p = p_gen.next()
	return primes

def can_split(n):
	str_num = str(n)
	pairs = []
	for x in xrange(1, len(str_num)):
		if is_prime(int(str_num[:x])) and is_prime(int(str_num[x:])):
			pairs.append((int(str_num[:x]),int(str_num[x:])))
	return pairs

def get_matching_pairs(pairs):
	matches = []
	while len(pairs) > 0:
		pair = pairs.pop()
		for p in pairs:
			if concatenates(pair, p):
				matches.append((pair,p))
	return matches

def get_groups_of_5(matching_pairs):
	groups_of_5 = []
	while len(matching_pairs) > 0:
		mp1 = matching_pairs.pop()
		for mp2 in matching_pairs:
			if concatenates(mp1[0], mp2[0]) and concatenates(mp1[1], mp2[0]) and concatenates(mp1[0], mp2[1]) and concatenates(mp1[1], mp2[1]):
				groups_of_5.append((mp1,mp2))
	return groups_of_5

# def concatenates(pair1, pair2):
# 	if not is_prime(int(str(pair1[0])+str(pair2[0]))):
# 		return False
# 	if not is_prime(int(str(pair1[1])+str(pair2[0]))):
# 		return False
# 	if not is_prime(int(str(pair1[0])+str(pair2[1]))):
# 		return False
# 	if not is_prime(int(str(pair1[1])+str(pair2[1]))):
# 		return False
# 	return True

def find_concatenating_primes(n, test_range):
	candidates = [[p] for p in get_all_primes(2, test_range)]
	for x in xrange(0,n):
		next = []
		for c in candidates:
			for p in get_all_primes(2, test_range):
				if concatenates(c, p):
					next.append(c[:]+[p])
		candidates = next[:]
		print candidates
	return candidates


def concatenates(current, new):
	for n in current:
		if not is_prime(int(str(n)+str(new))):
			return False
		if not is_prime(int(str(new)+str(n))):
			return False
	return True

print find_concatenating_primes(5, 10000)

# all_pairs = []
# primes = get_all_primes(2,50000)
# for p in primes:
# 	all_pairs+=can_split(p)
# print get_groups_of_5(get_matching_pairs(all_pairs))