import itertools

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

comb = itertools.chain(lista1, lista2)

list(comb) # [1, 2, 3, 4, 5, 6]

lista3 = ['python', 'php', 'go']

comb = itertools.chain(lista1, lista2, lista3)

list(comb) # [1, 2, 3, 4, 5, 6, 'python', 'php', 'go']