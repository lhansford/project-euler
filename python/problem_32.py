def get_pandigital_products():
	products = []
	for x in xrange(1,100000000):
		print x
		y = 1
		while is_correct_length(x,y):
			if is_pandigital(x,y) and x*y not in products:
				products.append(x*y)
			y+=1
	return sum(products)

def is_correct_length(x,y):
	if (len(str(x)) + len(str(y)) + len(str(x*y))) < 10:
		return True
	return False

def is_pandigital(x,y):
	if (len(str(x)) + len(str(y)) + len(str(x*y))) != 9:
		return False
	counter = {key: 0 for key in "123456789"}
	digits = str(x*y) + str(x) + str(y)
	for d in digits:
		if d == '0':
			return False
		counter[d] +=1
	for key in counter.keys():
		if counter[key] != 1:
			return False
	return True

print get_pandigital_products()