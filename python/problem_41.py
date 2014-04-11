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

def get_all_pandigitals(n):
	all_results = []
	last_results = ["1"]
	for x in xrange(2,n+1):
		new_results = []
		for item in last_results:
			for index in xrange(0,len(item)):
				new_results.append(item[:index]+str(x)+item[index:])
			new_results.append(item + str(x))
		all_results += last_results
		last_results = new_results
	all_results += new_results
	return [int(x) for x in all_results]

def get_highest_pandigital():
	pandigitals = get_all_pandigitals(9)
	pandigitals.sort()
	pandigitals.reverse()
	for d in pandigitals:
		if is_prime(d):
			return d

print get_highest_pandigital()
