		

def get_permutations(sequence):
	sequence.sort()
	if len(sequence) == 1:
		return [sequence]
	elif len(sequence) == 2:
		return [sequence, sequence[::-1]]
	else:
		permutations = []
		for i,x in enumerate(sequence):
			subset = sequence[:]
			subset.pop(i)
			for p in get_permutations(subset):
				permutations.append([x]+p)
		return permutations

sequence = [str(x) for x in xrange(0,10)]
permutations = get_permutations(sequence)
print permutations[999999]