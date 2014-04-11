def has_same_digits(int1, int2):
	return sorted([d for d in str(int1)]) == sorted([d for d in str(int2)])

def find_permuted_multiples(highest_multiplier):
	x = 1
	while True:
		if len(str(x)) == len(str(x*highest_multiplier)):
			matches = True
			for m in xrange(highest_multiplier,1,-1):
				if not has_same_digits(x,x*m):
					matches = False
					break
			if matches:
				return x
			x+=1
		else:
			x=int('1' + ('0'*len(str(x))))

print find_permuted_multiples(6)