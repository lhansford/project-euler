def find_pythagorean_triplet(triplet_sum):
	"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

		a^2 + b^2 = c^2
		For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

		There exists exactly one Pythagorean triplet for which a + b + c = 1000.
		Find the product abc.
	"""

	##NOTE: This works for the given problem but I think it will infinite loop
	##with other numbers. The first while loop may never terminate.
	a = 0
	b = 1
	c = 2
	while a < b and not is_pythagorean_triplet(a,b,c):
		a += 1
		b = a+1
		c = triplet_sum - (a + b)
		while b < c and not is_pythagorean_triplet(a,b,c):
			b += 1
			c -= 1

	if is_pythagorean_triplet(a,b,c):
		return (a,b,c)


def is_pythagorean_triplet(a,b,c):
	return a**2 + b**2 == c**2


a = find_pythagorean_triplet(1000)
print a
print a[0] * a[1] *a[2]