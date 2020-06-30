from collections import OrderedDict

d = OrderedDict()
d['python'] = 10
d['java'] = 5
d['php'] = 6
d['C'] = 10

for key in d:
    print(key, d[key])

d2 = { }
d2['C'] = 10
d2['php'] = 5
d2['java'] = 6
d2['python'] = 10

for key in d2:
    print(key, d[key])

d
d2