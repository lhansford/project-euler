from itertools import permutations

def cube_gen(start = 1):
	x = start
	while True:
		yield x**3
		x+=1

def get_unique_permutations(n):
	return set([int(''.join(p)) for p in permutations(str(n))])

def find_n_cubed_permutations(n):
	cubes = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[],13:[],14:[]}
	c_gen = cube_gen(343)
	total_permutations = []
	while len(total_permutations) < n-1:
		total_permutations = []
		c = c_gen.next()
		# print c
		for p in get_unique_permutations(c):
			if p in cubes[len(str(c))]:
				print p
				total_permutations.append(p)
		cubes[len(str(c))].append(c)
		# print cubes
	return total_permutations

print find_n_cubed_permutations(5)