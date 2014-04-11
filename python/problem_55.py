def is_lychrel_num(n):
	for x in xrange(1,50):
		if is_palindrome(str(n+reverse_num(n))):
			return False
		n = n+reverse_num(n)
	return True

def reverse_num(n):
	return int(str(n)[::-1])

def is_palindrome(n):
	""" Takes a string """
	if len(n) < 2:
		return True
	if n[0] == n [-1]:
		return is_palindrome(n[1:-1])
	else:
		return False

def get_lychre_nums(limit):
	l_nums = []
	for x in xrange(1,limit):
		if is_lychrel_num(x):
			l_nums.append(x)
	return l_nums


print len(get_lychre_nums(10000))