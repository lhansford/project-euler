def find_divisible_1_to_n(divisible_max):
	digit = 0
	is_divisible = False
	while not is_divisible:
		digit += divisible_max
		for x in xrange(3,divisible_max): #We know that they always be divisible by 1,2 and 20, so check 3-19
			if digit % x != 0:
				is_divisible = False
				break
			is_divisible = True
		
	return digit

print find_divisible_1_to_n(20)