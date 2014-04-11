def get_max_digit_sum(limit):
	max_sum = 0
	for a in xrange(1,100):
		for b in xrange(1,100):
			digit_sum = sum([int(d) for d in str(a**b)])
			if digit_sum > max_sum:
				max_sum = digit_sum
	return max_sum

print get_max_digit_sum(100)