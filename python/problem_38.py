def is_pandigital(number):
	if len(number) != 9:
		return False
	counter = {key: 0 for key in "123456789"}
	for d in number:
		if d == '0':
			return False
		counter[d] +=1
	for key in counter.keys():
		if counter[key] != 1:
			return False
	return True

def get_pandigital_multiples(limit):
	largest = 0
	for x in xrange(1,limit):
		number = str(x)
		multiplier = 2
		while len(number) < 9:
			number += str(x * multiplier)
			multiplier += 1
		if is_pandigital(number) and int(number) > largest:
			largest = int(number)
	return largest

print get_pandigital_multiples(9877)