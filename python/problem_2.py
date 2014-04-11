def sum_even_fibonacci(limit):
	f1 = 0
	f2 = 1
	total = 0
	while f1 + f2 <= limit:
		f1, f2 = f2, f1 + f2
		if f2%2 == 0:
			total += f2
	return total

print(sum_even_fibonacci(4000000))