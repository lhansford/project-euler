def get_self_powers(limit):
	return sum([x**x for x in xrange(1,limit)])

print str(get_self_powers(1001))[-10:]