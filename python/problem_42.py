def get_words():
	with open("resources/words.txt", "r") as f:
		words = f.read().replace('"', '').split(",")
	return words

def get_triangle_numbers(limit):
	return [int((0.5*x)*(x+1)) for x in xrange(1,limit)]

def get_word_value(word):
	value = 0
	for c in word:
		value += ord(c) - 64
	return value

def get_triangle_words():
	t_words = []
	t_nums = get_triangle_numbers(27)
	for word in get_words():
		if get_word_value(word) in t_nums:
			t_words.append(word)
	return len(t_words)

print get_triangle_words()