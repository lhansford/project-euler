def get_solutions(p):
	solutions = []
	for a in xrange(1,p):
		for b in xrange(1,a):
			c = p - a - b
			if a**2 + b**2 == c**2:
				solutions.append([a,b,c])
	return solutions

def get_max_solutions(limit):
	max_solutions = 0
	p = 0
	for x in xrange(1,limit):
		solutions = get_solutions(x)
		if len(solutions) > max_solutions:
			max_solutions = len(solutions)
			p = x
	return p

print get_max_solutions(1001)