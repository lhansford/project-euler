def get_triangle(filename):
	triangle = []
	with open(filename, 'r') as text:
		for line in text.readlines():
			line = line.strip()
			triangle.append([int(x) for x in line.split(" ")])
	return triangle

def get_max(top, bottom):
	""" Top is an int, bottom is a list containing two ints. Returns the sum 
	of top and the larger int in bottom."""
	return top + max(bottom)

def get_max_path_sum(pyramid):
	if len(pyramid) == 1:
		return pyramid[0][0]
	elif len(pyramid) == 2:
		return get_max(pyramid[0][0], pyramid[1])
	else:
		new_pyramid = pyramid[:-2]
		second_row = pyramid[-2]
		last_row = pyramid[-1]
		new_row = []
		for i in xrange(0,len(last_row)-1):
			m = get_max(second_row[i], [last_row[i], last_row[i+1]])
			new_row.append(m)
		new_pyramid.append(new_row)
		return get_max_path_sum(new_pyramid)

triangle = get_triangle("resources/triangle.txt")
print(get_max_path_sum(triangle))