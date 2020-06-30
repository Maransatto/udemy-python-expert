lista = [1,2,3,4]
for i in lista:
    print(i)

# o código acima é simplesmente um "for", um iterator, ok?
# generator é igual, mas os valores são lidos só quando necessário (lazy evaluation)
# prática:

gerador = (letra for letra in 'python')
gerador.next() # coisa do python2
gerador.__next__() # coisa do python3 
# a cada execução, aconteceu o item abaixo
# >>> gerador.__next__()
# 'p'
# >>> gerador.__next__()
# 'y'
# >>> gerador.__next__()
# 't'
# >>> gerador.__next__()
# 'h'
# ou:
next(gerador)
# >>> next(gerador)
# 'o'
# >>> next(gerador)
# 'n'
# >>> next(gerador)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# percorre os valores usando next(), até chegar ao final (StopIteration)