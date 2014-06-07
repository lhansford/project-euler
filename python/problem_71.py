from fractions import Fraction

### Brute force method for finding the fraction next to 3/7 in the range of 
### 1 to 1000000 for denominator or numerator. Takes about 30 secs to run.

### A faster solution would be to find the greatest multiple of 7 under 1000000,
### which is 999999, and apply that to the fraction (i.e. 3/7 == 428571/999999).
### Take one from the numerator and you have the answer.

limit = Fraction(3, 7)
closest = Fraction(2, 5)
for denominator in range(1,1000000):
	start = int((denominator / closest.denominator) * closest.numerator)
	for numerator in range(start,1000000):
		if Fraction(numerator, denominator) >= limit:
			break
		elif Fraction(numerator, denominator) > closest:
			closest = Fraction(numerator, denominator)
print(closest)
