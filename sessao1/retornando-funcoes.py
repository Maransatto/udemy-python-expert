def pai(num):
    
    def filho1():
        print('Oi, eu sou o filho1')

    def filho2():
        print('Oi, eu sou o filho2')

    try:
        assert num == 20
        return filho1
    except AssertionError:
        return filho2

f1 = pai(20)
f2 = pai(10)

f1()
f2()