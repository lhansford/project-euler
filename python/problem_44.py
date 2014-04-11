from __future__ import division
from math import sqrt


def get_pentagon_number(n):
	return n * (3*n - 1) / 2

def is_pentagon_number(n):
	if (1/6) * (sqrt(24*n+1) + 1) % 1 == 0:
		return True
	return False
	


def get_pentagon_numbers(limit):
	pentagon_numbers = []
	for x in xrange(1,limit):
		pentagon_numbers.append(get_pentagon_number(x))
	return pentagon_numbers

def get_pentagon_pairs(limit):
	p_nums = get_pentagon_numbers(limit)
	for p1 in p_nums:
		for p2 in p_nums:
			if is_pentagon_number(p1+p2) and is_pentagon_number(abs(p1-p2)):
				return abs(p1-p2)
	return None

print get_pentagon_pairs(100000)




