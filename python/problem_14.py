def collatz_sequence(number):
	"""
	The following iterative sequence is defined for the set of positive integers:

	n ->n/2 (n is even)
	n-> 3n + 1 (n is odd)

	Using the rule above and starting with 13, we generate the following sequence:

	13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
	It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
	Although it has not been proved yet (Collatz Problem), 
	it is thought that all starting numbers finish at 1.
	"""
	length = 1
	while number != 1:
		if number % 2 == 0:
			number /= 2
		else:
			number = (3 * number) + 1
		length += 1
	return length

def find_longest_collatz_sequence(limit):
	length = 0
	number = 0
	for x in xrange(1, limit):
		print x
		l = collatz_sequence(x)
		if l > length:
			length = l
			number = x
	return number


print find_longest_collatz_sequence(1000000)
