from math import sqrt

def is_squared(n):
	return sqrt(n) % 1 == 0

def get_minimal_solution(d):
	""" x**2 - Dy**2 = 1 """
	x = 1
	y = 1
	while diophantine(x,d,y) != 1:
		while diophantine(x,d,y) > 1:
			y *= 2
		if diophantine(x,d,y) == 1:
			return x
		print(d, (x,y))
		if get_y(x,d,range(y/2,y+1)):
			return x
		x += 1
		y = 1
	return x

def get_y(x,d, y_list):
	# print(y_list)
	if len(y_list) == 1 and diophantine(x, d, y_list[0]) == 1:
		return y_list[0]
	elif len(y_list) < 2:
		return None
	mid = int(len(y_list)/2)
	result = diophantine(x, d, y_list[mid])
	if result == 1:
		return y_list[mid]
	elif result > 1:
		return get_y(x, d, y_list[mid:])
	else:
		return get_y(x, d, y_list[:mid])

		
def diophantine(x,d,y):
	return x**2 - (d*y**2)


minimal_solutions = []
for d in range(1000, 2, -1):
	if not is_squared(d):
		minimal_solutions.append((get_minimal_solution(d), d))
		print(minimal_solutions)
print(max(minimal_solutions, key=lambda item:item[0]))
