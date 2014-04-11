def sum_of_squares(limit):
	return sum(x**2 for x in xrange(limit+1)) 

def square_of_sum(limit):
	return sum(x for x in xrange(limit+1))**2

print square_of_sum(100) - sum_of_squares(100)