import timeit

def get_multiples_3_5(number):
	"""Finds the multiples of 3 and 5 for all natural numbers below the given
	number. Returns as a list
	"""
	multiples = []
	for x in range(0, number):
		if x%3 == 0 or x%5 == 0:
			multiples.append(x)
	return multiples

def sum_list(numbers):
	"""Sum the number is the given list."""
	total = 0
	for x in numbers:
		total += x
	return total

def multiple_3_5_sum(limit):
	return sum([i for i in range(limit) if i%3 == 0 or i%5 == 0])


# print(sum_list(get_multiples_3_5(1000)))
# print(multiple_3_5_sum(1000))

#Test time
def test1():
	# 281.09496298999875
	return sum_list(get_multiples_3_5(1000))
def test2():
	# 236.26332607900258
	return multiple_3_5_sum(1000)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test1()", setup="from __main__ import test1"))
    print(timeit.timeit("test2()", setup="from __main__ import test2"))