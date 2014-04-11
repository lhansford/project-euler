from itertools import permutations

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

def get_arithemtic_sequence(perms):
	first = perms.pop(0)
	for p1 in perms:
		for p2 in perms:
			if p1 != p2 and p1 - first == p2 - p1 and is_prime(p1) and is_prime(p2):
				return (first,p1,p2)
	return None

def get_permutations(x):
	return [int(''.join(p)) for p in permutations(str(x)) if p[0] != '0']

def find_prime_permutations():
	results = []
	for x in xrange(1001,10000,2):
		if not is_prime(x):
			continue
		sequence = get_arithemtic_sequence(get_permutations(x))
		if sequence is not None:
			results.append(sequence)
	return results



print find_prime_permutations()