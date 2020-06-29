# aulas 1 e 2

x,y,z = [1,2,3] # arrays
n1, n2 = ("marcos", "joão") # tuplas
a,b,c,d,e = "hello" # string

# x,y = [1,2,3] # vai dar erro
x,y,_ = [1,2,3] # vai descartar o terceiro
_,x,y = [1,2,3] # vai descartar o primeiro

# Observação: funciona com todo tipo de objeto que seja iterável

lista = [9,4,5,15,20]
*n1, n2 = lista # evita de dar o erro pela diferença de quantidade

print(n1)
# >>> n1
# [9, 4, 5, 15]
# >>> n2
# 20

n1, *n2 = lista
# >>> n1
# 9
# >>> n2
# [4, 5, 15, 20]

# o asterístico sempre será uma lista independente da quantidade de elementos.
# é importanta quando se quer desempacotar variáveis de quantidade desconhecida de elementos
# exemplo:

notas = [9,7,8,5,10]
# quero descartar a primeira e a última nota, como eu faço?
n1, *n2, n3 = notas
# >>> n1
# 9
# >>> n2
# [7, 8, 5]
# >>> n3
# 10

# outro exemplo
# e se eu quero pegar a primeira e a última nota, jogar fora as outras.
first, *_, last = lista
# >>> first
# 9
# >>> last
# 20