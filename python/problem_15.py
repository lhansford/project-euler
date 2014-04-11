import math

def get_number_routes(grid_size):
	a = math.factorial(grid_size * 2)
	b = math.factorial(grid_size) * math.factorial(grid_size)
	return a/b

print get_number_routes(20)