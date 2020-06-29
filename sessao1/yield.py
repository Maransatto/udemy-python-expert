# é preciso conhecer os generators antes de entender o yield
# é igual o return, mas retorna um generator

def gerador():
    for i in range(5):
        yield i

g = gerador()

next(g)

# >>> next(g)
# 0
# >>> next(g)
# 1
# >>> next(g)
# 2
# >>> next(g)
# 3
# >>> next(g)
# 4

# outro exemplo:
def gerador():
    yield 1
    for i in range(2,5):
        yield i

g = gerador()
next(g)