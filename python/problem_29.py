def get_distinct_terms(a,b):
	distinct_terms = []
	for x in xrange(2,a+1):
		for y in xrange(2,b+1):
			distinct_terms.append(x**y)
	return set(distinct_terms)

print len(get_distinct_terms(100,100))