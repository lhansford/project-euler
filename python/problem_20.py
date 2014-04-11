def sum_factorial_digits(n):
	factorial = n
	for x in xrange(1,n):
		factorial *= x
	return sum([int(digit) for digit in str(factorial)])

print sum_factorial_digits(100)