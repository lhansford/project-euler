from __future__ import division
from math import sqrt
from itertools import permutations

def get_cyclical_nums():
	tri = get_all_valid_triangle_nums()
	sqr = get_all_valid_square_nums()
	pen = get_all_valid_pentagon_nums()
	hxg = get_all_valid_hexagon_nums()
	hep = get_all_valid_heptagon_nums()
	ocg = get_all_valid_octagon_nums()

	polys = [tri, sqr, pen, hxg, hep, ocg]
	
	perms = permutations(xrange(0,len(polys)))
	for p in perms:
		for a in polys[p[0]]:
			for b in filter_list(a, polys[p[1]]):
				for c in filter_list(b, polys[p[2]]):
					for d in filter_list(c, polys[p[3]]):
						for e in filter_list(d, polys[p[4]]):
							for f in filter_list(e, polys[p[5]]):
								if str(a)[:2] == str(f)[2:]:
									return [a,b,c,d,e,f]
			

def filter_list(last_num, num_list):
	prefix = str(last_num)[2:]
	return [n for n in num_list if str(n)[:2] == prefix]

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

def get_all_valid_triangle_nums():
	#Get all 4 digit tri nums. Any numbers with 0 on end are disposed of.
	nums = []
	for x in xrange(1000,10000):
		if is_triangle_number(x) and str(x)[2] != '0':
			nums.append(x)
	return nums

def get_all_valid_square_nums():
	#Get all 4 digit square nums. Any numbers with 0 on end are disposed of.
	nums = []
	for x in xrange(1000,10000):
		if is_square_number(x) and str(x)[2] != '0':
			nums.append(x)
	return nums

def get_all_valid_pentagon_nums():
	#Get all 4 digit pentagon nums. Any numbers with 0 on end are disposed of.
	nums = []
	for x in xrange(1000,10000):
		if is_pentagon_number(x) and str(x)[2] != '0':
			nums.append(x)
	return nums

def get_all_valid_hexagon_nums():
	#Get all 4 digit hex nums. Any numbers with 0 on end are disposed of.
	nums = []
	for x in xrange(1000,10000):
		if is_hexagon_number(x) and str(x)[2] != '0':
			nums.append(x)
	return nums

def get_all_valid_heptagon_nums():
	#Get all 4 digit hetpagon nums. Any numbers with 0 on end are disposed of.
	nums = []
	for x in xrange(1000,10000):
		if is_heptagon_number(x) and str(x)[2] != '0':
			nums.append(x)
	return nums

def get_all_valid_octagon_nums():
	#Get all 4 digit octo nums. Any numbers with 0 on end are disposed of.
	nums = []
	for x in xrange(1000,10000):
		if is_octagon_number(x) and str(x)[2] != '0':
			nums.append(x)
	return nums

print sum(get_cyclical_nums())
		