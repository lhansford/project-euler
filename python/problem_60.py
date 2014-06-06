from collections import OrderedDict
from itertools import combinations

## THIS IS A LITTLE SLOW, BUT IT WORKS (takes 2-3mins to get answer)

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
	p = next(p_gen)
	while p < limit:
		primes.append(p)
		p = next(p_gen)
	return primes

def get_tuples_with_n_occurences(pairs, n):
	pairs_with_n_occurences = []
	for pair in pairs:
		count = 0
		for pair2 in pairs:
			if pair[0] == pair2[0] or pair[0] == pair2[1]:
				count += 1
			if count == n:
				pairs_with_n_occurences.append(pair)
				break
	return pairs_with_n_occurences

def get_prime_sets(pairs, n):
	pair_dict = {}
	
	for pair in pairs:
		if pair_dict.get(pair[0]):
			pair_dict[pair[0]].append(pair[1])
		else:
			pair_dict[pair[0]] = [pair[1]]
	pair_dict = OrderedDict(sorted(pair_dict.items(), key=lambda t: t[0]))

	prime_sets = []

	for key in pair_dict.keys():
		for item in pair_dict[key]:
			count = 2
			p_set = [key,item]
			for item2 in pair_dict.get(item,[]):
				if item2 in pair_dict[key]:
					count+=1
					p_set.append(item2)
				if count == n:
					prime_sets.append(p_set)
					break
			if count < n:
				for item2 in pair_dict.get(key,[]):
					if item in pair_dict.get(item2,[]):
						count+=1
						p_set.append(item2)
					if count == n:
						prime_sets.append(p_set)
						break
	print(prime_sets)
	return(prime_sets)

def find_concatenating_primes(n, test_range):
	candidates = get_all_primes(2, test_range)
	pairs = set()
	for a in candidates:
		for b in get_all_primes(2, test_range):
			if concatenates(a, b):
				pairs.add(tuple(sorted([a,b])))
	pairs = get_tuples_with_n_occurences(pairs, n)
	return get_prime_sets(pairs, n)


def concatenates(a, b):
	if is_prime(int(str(a)+str(b))) and is_prime(int(str(b)+str(a))):
		return True
	return False

def get_min_sum(list):
	return min([sum(x) for x in list])

def remove_non_concatenating(list):
	valid_sets = []
	for sublist in list:
		valid = True
		for combo in combinations(sublist,2):
			if not concatenates(combo[0], combo[1]):
				valid = False
				break
		if valid:
			valid_sets.append(sublist)
	return valid_sets

c = find_concatenating_primes(5, 10000)
print(get_min_sum(remove_non_concatenating(c)))