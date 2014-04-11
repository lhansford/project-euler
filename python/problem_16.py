def power_digit_sum(number, power):
	""" Find the sum of the digits of number**power. """
	return sum([int(d) for d in str(number**power)])