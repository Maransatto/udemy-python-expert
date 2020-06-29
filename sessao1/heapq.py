# este módulo implementa o algoritmo de fila de prioridades #heap = pilha, pensa em um montante
import heapq

# digamos que você queira por exemplo ter uma prioridade de tamplante de orgaos, e um dos critérios seja
# o critério de quanto tempo ela está esperando aquele transplante:
# o critério é o tempo de espera

idades = [15, 10, 20, 18, 25, 8, 19]
print(idades)
# quem são os 3 menores números dessa lisat?
heapq.nsmallest(3, idades)
heapq.nlargest(4, idades)

heapq.heapify(idades) # transforma uma lista em uma heap em tempo linear
heapq.heappop(idades) # remove o menor

# inserir em uma posição específica
heapq.heappush(idades, 25)

