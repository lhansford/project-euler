from __future__ import division
from fractions import Fraction

def create_fraction(level):
	fraction = 2 + Fraction(1,2)
	for x in xrange(level, 1, -1):
		fraction = 1/fraction
		fraction += 2
	return fraction-1

def count_longer_numerators(limit):
	count = 0
	for x in xrange(1,limit+1):
		f = create_fraction(x)
		if len(str(f.numerator)) > len(str(f.denominator)):
			count += 1
	return count

print count_longer_numerators(1000)