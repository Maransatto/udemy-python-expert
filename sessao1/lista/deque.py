# O módulo deque from collections representa fila de 2 pontas
# é uma estrutura que pode remover tanto do início como no final da fila
# segue a propriedade fifo = first in, first out (o primeiro a entrar, é o primeiro a sair)

from collections import deque
'''
fila = deque(maxlen=4)
fila.append(1)
fila.append(2)
fila.append(3)
fila.append(4) # deque([1, 2, 3, 4], maxlen=4)
fila.append(5) # deque([2, 3, 4, 5], maxlen=4) # removeu o primeiro da fila
print(fila)
'''

f = deque()
f.append(1)
f.append(2)
f.append(3)
f.appendleft(4) 
# f.appendright(5) # vai dar erro, pois não faz sentido se o default do append já é a direita
f.pop() # remove do final
f.popleft() # o deque me permite remover itens de qualquer extremidade
print(f)

# é bem rápido, em termos análise asintótica (complexidade e custo de tempo das aplicações (ozão de 1))
# é bom atentar que é diferente de uma lista, pois inserir ou remover elementos da frente da lista possui complexidade O de N (função linear)
# onde N é a quantidade de elementos de uma lista

# exemplo de conversão de lista pra deque
g = ['fernando', 'silva', 'maransatto']
nome = deque(g)
print(nome)
nome.pop()