# fila de prioridades com auxílio do heapq
# um dos algoritmos mais famosos na computação é o de caminhos mínimos
# menor distância entre um caminho e outro

import heapq

class PriorityQueue:
    
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Person(object):
    
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

q = PriorityQueue()
q.push(Person('Marcos'), 28)
q.push(Person('João'), 30)
q.push(Person('Maria'), 15)
q.push(Person('Gabriel'), 40)

print(q.pop())
print(q._queue)