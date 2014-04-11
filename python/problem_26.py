def recurring_cycle(limit):
	longest_cycle = 0
	longest_cycle_divisor = 0
	for divisor in xrange(limit,1,-1):
		if divisor < longest_cycle:
			break
		for length in xrange(1, divisor):
			if 1 == 10**length % divisor:
				if length > longest_cycle:
					longest_cycle = length
					longest_cycle_divisor = divisor
					break
	return longest_cycle,longest_cycle_divisor

print recurring_cycle(1000)