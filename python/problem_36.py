def convert_to_binary(q):
	binary = ""
	while q != 0:
		r = q % 2
		q = q / 2
		binary = str(r) + binary
	return binary

def is_palindrome(digit):
	if len(digit) < 2:
		return True
	if digit[0] == digit [-1]:
		return is_palindrome(digit[1:-1])
	else:
		return False

def get_palindromes(limit):
	palindromes = []
	for x in xrange(0,limit):
		if is_palindrome(str(x)) and is_palindrome(convert_to_binary(x)):
			palindromes.append(x)
	return palindromes


p = get_palindromes(1000000)
print p
print sum(p)

