def find_palindrome(product_length):
	""" Finds the longest palindromic nubmer that is the product of two numbers
	n-digits long.
	"""
	n_digit_palindromes = []
	product_range = range(int((product_length)*"9"), int((product_length-1)*"9"), -1)
	for x in product_range:
		for y in product_range:
			product = x * y
			if is_palindrome(str(product)):
				n_digit_palindromes.append(product)
		product_range.pop(0)
	# n_digit_palindromes.sort()
	# return n_digit_palindromes.pop()
	return max(n_digit_palindromes)

def is_palindrome(digit):
	if len(digit) < 2:
		return True
	if digit[0] == digit [-1]:
		return is_palindrome(digit[1:-1])
	else:
		return False

print find_palindrome(3)
# print max([x*y for x in range(900,1000) for y in range(900,1000) if str(x*y) == str(x*y)[::-1]]) # http://projecteuler.net/thread=4;page=2