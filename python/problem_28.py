def get_sum_of_spiral_diagonals(width):
	top_right_diagonal = []
	x = 3
	while len(top_right_diagonal) < width/2:
		top_right_diagonal.append(x**2)
		x += 2
	top_left_diagonal = [x-(i+1)*2 for i,x in enumerate(top_right_diagonal)]
	bottom_left_diagonal = [x-(i+1)*2 for i,x in enumerate(top_left_diagonal)]
	bottom_right_diagonal = [x-(i+1)*2 for i,x in enumerate(bottom_left_diagonal)]
	return sum([1] + top_right_diagonal + top_left_diagonal
	 + bottom_right_diagonal + bottom_left_diagonal)

print get_sum_of_spiral_diagonals(1001)