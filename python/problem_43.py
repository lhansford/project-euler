def get_pandigitals(start,end):
	all_results = []
	last_results = [str(start)]
	for x in xrange(start+1,end+1):
		new_results = []
		for item in last_results:
			for index in xrange(0,len(item)):
				new_results.append(item[:index]+str(x)+item[index:])
			new_results.append(item + str(x))
		all_results += last_results
		last_results = new_results
	all_results += new_results
	return [int(x) for x in all_results if len(x) == end+1 and x[0] != "0"]

def check_substring_divisibility(num):
	num = str(num)
	divs = [2,3,5,7,11,13,17]
	for i,x in enumerate(xrange(1,len(num)-2)):
		if int(num[x] + num[x+1] + num[x+2]) % divs[i] != 0:
			return False
	return True

def get_subdivisible_pandigitals():
	pandigitals = get_pandigitals(0,9)
	return [x for x in pandigitals if check_substring_divisibility(x)]

print sum(get_subdivisible_pandigitals())