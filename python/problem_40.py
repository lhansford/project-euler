s = ""
for x in xrange(1,200000): #200000 gives us at least 1m decimal places
	s += str(x)
print int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999])