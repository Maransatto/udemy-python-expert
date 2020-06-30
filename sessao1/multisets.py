from collections import Counter # semelhante ao multiset em outras linguagens

c = Counter(a=4, b=2, c=3)
c.elements()
list(c.elements())
set(c.elements())

c.most_common()
c.most_common(2)