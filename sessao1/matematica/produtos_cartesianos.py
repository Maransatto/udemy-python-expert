import itertools

for p in itertools.product([1,2,3], [4,5]):
    print(p)
# (1, 4)
# (1, 5)
# (2, 4)
# (2, 5)
# (3, 4)
# (3, 5)