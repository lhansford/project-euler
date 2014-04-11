number_words = {
	0 : "",
	1 : "one",
	2 : "two",
	3 : "three",
	4 : "four",
	5 : "five",
	6 : "six",
	7 : "seven",
	8 : "eight",
	9 : "nine",
	10 : "ten",
	11 : 'eleven',
	12 : 'twelve',
	13 : 'thirteen',
	14 : 'fourteen',
	15 : 'fifteen',
	16 : 'sixteen',
	17 : 'seventeen',
	18 : 'eighteen',
	19 : "nineteen",
	20 : "twenty",
	30 : 'thirty',
	40 : 'forty',
	50 : 'fifty',
	60 : 'sixty',
	70 : 'seventy',
	80 : 'eighty',
	90 : 'ninety',
	100 : 'hundred',
	1000 : 'thousand'
}

def get_letter_count(limit):
	"""Only works upto 1000 at the moment"""
	letter_count = 0
	for x in xrange(1, limit + 1):
		if x < 100:
			for word in get_double_digit_word(x):
				print word
				letter_count += len(word)
		elif x < 1000:
			for word in get_triple_digit_word(x):
				letter_count += len(word)
		elif x == 1000:
			letter_count += len("onethousand")
	return letter_count

def get_double_digit_word(digit):
	if digit < 20:
		return [number_words[digit]]
	first = int(str(digit)[0]) * 10
	second = int(str(digit)[1])
	if second == 0:
		return [number_words[first]]
	return [number_words[first], number_words[second]]

def get_triple_digit_word(digit):
	first = number_words[int(str(digit)[0])]
	second_third = get_double_digit_word(int(str(digit)[1:]))
	words = [first, number_words[100]]
	if digit % 100 != 0:
		words.append('and')
	return words + second_third