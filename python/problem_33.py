from __future__ import division

def is_digit_cancelling_fraction(num, den):
	num_str, den_str = str(num), str(den)
	for d in num_str:
		if d in den_str:
			num_str = num_str.replace(d,"")
			den_str = den_str.replace(d,"")
			if den_str == "" or den_str == "0" or num_str == "" or num_str == "0":
				return False
			if num/den == int(num_str)/int(den_str):
				return True
	return False

def get_fractions():
	fractions = []
	for x in xrange(10,100):
		for y in xrange(10,100):
			if x/y >= 1 or (x % 10 == 0 and y % 10 == 0):
				continue
			elif is_digit_cancelling_fraction(x,y):
				fractions.append((x,y))
	return fractions

def product_of_fractions(fractions):
	product = 1
	for fraction in fractions:
		product *= (fraction[0]/fraction[1])
	return product

print product_of_fractions(get_fractions())