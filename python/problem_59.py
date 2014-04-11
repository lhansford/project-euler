from itertools import permutations
from string import lowercase, letters, digits, whitespace

def encrypt(message, key):
	encrypted_message = []
	for i in xrange(0,len(message)):
		encrypted_message.append(message[i] ^ key[i % len(key)])
	return encrypted_message

def get_permutations(length):
	return [str_to_ascii(p) for p in permutations(lowercase, length)]

def str_to_ascii(string):
	return [ord(c) for c in string]

def get_encrypted_message(file):
	with open(file,'r') as message:
		return [int(c) for c in message.read().split(',')]


def asciicode_to_string(message):
	return "".join([str(chr(x)) for x in message])

def analyse(msg, max_word_len):
	words = msg.split(' ')
	for word in words:
		if len(word) > max_word_len:
			return False
	return True

def sum_chars(msg):
	return sum(str_to_ascii(msg))

em = get_encrypted_message('resources/cipher1.txt')
possibilities = []
for p in get_permutations(3):
	msg = asciicode_to_string(encrypt(em,p))
	if analyse(msg, 15):
		possibilities.append(msg)
print sum_chars(possibilities[0])