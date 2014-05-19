counter = 0
for base in xrange(1,10):
    for exp in xrange(1,30):
        if len(str(base**exp)) == exp:
            counter += 1
print counter