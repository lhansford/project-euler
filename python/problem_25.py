def fibonacci_generator():
	f1, f2 = 1,1
	while True:
		yield f1 + f2
		f1, f2 = f2, f1+f2

f = fibonacci_generator()
x = 3
while len([n for n in str(f.next())]) < 1000:
	x += 1
print x