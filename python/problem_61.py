from __future__ import division
from math import sqrt
from collections import OrderedDict

def get_cyclical_nums(cycles = OrderedDict()):
	print cycles
	tests = [is_triangle_number,is_square_number,is_pentagon_number,is_heptagon_number,is_hexagon_number,is_octagon_number]
	if len(cycles.keys()) == 6:
		return cycles
	elif len(cycles.keys()) == 0:
		for a in xrange(1000,10000):
			for test in tests:
				cycles[a] = test
				return get_cyclical_nums(cycles)
	else:
		prev = str(cycles.keys()[-1])[2:]
		for a in xrange(1000,10000):
			if str(a)[:2] == prev:
				for test in tests:
					if test not in cycles.values() and test(a):
						cycles[a] = test
						return get_cyclical_nums(cycles)
		return False




	# 	cycles = [a]
	# 	if str(a)[-2] != "0":
	# 		for y in xrange(int(str(x)[:2]+"10"),int(str(x)[:2]+"99")):
	# 			if str(y)[-2] != "0":
	# 				cycles.append((x,y,int(str(y)[-2:]+str(x)[:2])))
	# return cycles

def is_triangle_number(n):
	if (sqrt(8*n+1) - 1)/2 % 1 == 0:
		return True
	return False

def is_square_number(n):
	if (sqrt(n)) % 1 == 0:
		return True
	return False

def is_pentagon_number(n):
	if (sqrt(24*n+1) + 1)/6 % 1 == 0:
		return True
	return False

def is_hexagon_number(n):
	if (sqrt(8*n+1) + 1)/4 % 1 == 0:
		return True
	return False

def is_heptagon_number(n):
	if (sqrt(40*n+9) + 3)/10 % 1 == 0:
		return True
	return False

def is_octagon_number(n):
	if (sqrt(3*n+1) + 1)/3 % 1 == 0:
		return True
	return False

print get_cyclical_nums()
		