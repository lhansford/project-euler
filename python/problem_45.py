from __future__ import division
from math import sqrt

def is_triangle_number(n):
	if (sqrt(8*n+1) - 1)/2 % 1 == 0:
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

def is_all(x):
	if is_triangle_number(x) and is_hexagon_number(x) and is_pentagon_number(x):
		return True
	return False

def get_next_tri_pent_hex(n):
	x = n*(n+1)/2
	while not is_all(x):
		n+=1
		x += n
	return x

print get_next_tri_pent_hex(286)