from collections import Counter

def cube_gen(start = 1):
    x = start
    while True:
        yield x**3
        x+=1

def find_n_cubed_permutations(n):
    permutations = {}
    c_gen = cube_gen()
    while True:
        cube = c_gen.next()
        cube_key = frozenset(Counter([digit for digit in str(cube)]).iteritems())
        if cube_key in permutations:
            permutations[cube_key] += [cube]
        else:
            permutations[cube_key] = [cube]
        if len(permutations[cube_key]) == n:
            return permutations[cube_key]

print min(find_n_cubed_permutations(5))