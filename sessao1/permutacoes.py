import itertools

for p in itertools.permutations([1,2,3]):
    print(''.join(str(x) for x in p))
# 123
# 132
# 213
# 231
# 312
# 321