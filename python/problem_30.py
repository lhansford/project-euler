def digit_nth_powers(n):
	# limit = int('9'*n)
	results = []
	for x in xrange(2,354294):
		result = 0
		for digit in str(x):
			result += int(digit)**n
		if result == x:
			results.append(x)
	return results

print sum(digit_nth_powers(5))