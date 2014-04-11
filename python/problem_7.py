# from math import sqrt

def get_nth_prime(nth):
	"""Get the nth number prime using trial division"""
	current_nth = 3
	prime_candidate = 5
	while current_nth < nth:
		prime_candidate += 2
		if prime_candidate % 5 == 0 or prime_candidate % 3 == 0:
			continue
		trial_divider = int(prime_candidate**0.5)
		if trial_divider % 2 == 0:
			trial_divider -= 1
		while trial_divider > 1:
			if prime_candidate % trial_divider == 0:
				break
			trial_divider -= 2
		if trial_divider == 1:
			current_nth += 1
	return prime_candidate