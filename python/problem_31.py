from itertools import combinations_with_replacement

def get_combos(total):
	#This was adapted from 
	#http://www.mathblog.dk/project-euler-31-combinations-english-currency-denominations/
	coins = [1, 2, 5, 10, 20, 50, 100, 200]
	ways = [0 for i in xrange(0, total+1)]
	ways[0] = 1
	for x in xrange(0,len(coins)):
		for y in xrange(coins[x], total+1):
			ways[y] += ways[y - coins[x]]
	return ways[-1]

print get_combos(200)