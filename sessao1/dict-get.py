d = { 'marcos' : 28, 'joão': 19, 'maria': 25 }

d['marcos']

d['blablabla']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'blablabla'

if d['blablabla']:
    print('chave existente')
else:
    print('chave inexistente')

d.get('joão')
d.get('blablabla') # não dá erro

if d.get('blablabla'): # dá pra testar a existência sem precisar usar try/except
    print('chave existente')
else:
    print('chave inexistente')