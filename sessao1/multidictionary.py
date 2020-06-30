from collections import defaultdict

d = defaultdict(list)
d['marcos'].append(10)
d['marcos'].append(20)
d['marcos'].append(30)

d['marcos'] # [10, 20, 30]

d['joão'].append(1)
d['joão'].append(2)

d['joão'] # [1, 2]

d = defaultdict(set)
d['marcos'].add(20)
d['marcos'].add(20)
d['marcos'].add(30)
d['marcos'].add(1)
d['marcos'] # {1, 20, 30}