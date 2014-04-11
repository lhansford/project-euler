
def max_path_sum_brute(pyramid):
	# route = []
	# for row in pyramid:
	# 	route.append(get_highest_position(row))
	# if check_route(route):
	# 	return sum([pyramid[row][x] for row, x in enumerate(route)])
	# else:
	# 	return sum([pyramid[row][x] for row, x in enumerate(find_route(pyramid,route))])
	routes = []
	for i, row in enumerate(pyramid):
		# print routes
		if i == 0:
			routes.append([row[0]])
		else:
			new_list = []
			for route in routes:
				new_list.append(list(route))
				new_list.append(list(route))
			routes = new_list
			for j, route in enumerate(routes):
					if j % 2 == 0:
						route.append(row[j/2])
					else:
						try:
							route.append(row[j/2+1])
						
	print routes



def check_route(route):
	previous = 0
	for pos in route:
		if pos < previous or pos > previous + 1:
			return False
		previous = pos
	return True

def find_route(pyramid, route):
	while check_route(route) != True:
		print route
		previous = 0
		for row, pos in enumerate(route):
			if pos < previous:
				route = get_better_diff(pyramid, route, row, pos, previous)
				break
			elif pos > previous + 1:
				route[row] -= 1
				break
			previous = pos
	return route

def get_highest_position(row):
	highest = 0
	position = 0
	for i,x in enumerate(row):
		if x > highest:
			highest = x
			position = i
	return position


pyramid_1 = [[3], 
[7,4], 
[2, 4, 6], [8, 5, 9, 3]
]

pyramid_2 = [
	[75],
	[95, 64],
	[17, 47, 82],
	[20, 04, 82, 47, 65],
	[19, 01, 23, 75, 03, 34],
	[88, 02, 77, 73, 07, 63, 67],
	[99, 65, 04, 28, 06, 16, 70, 92],
	[41, 41, 26, 56, 83, 40, 80, 70, 33],
	[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
	[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
	[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
	[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
	[63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
	[04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23],
]

print max_path_sum_brute(pyramid_1)