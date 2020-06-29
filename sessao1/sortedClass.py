class Person(object):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return self.name

def by_name(person):
    return person.name

def by_age(person):
    return person.age

p1 = Person('Marcos', 28)
p2 = Person('João', 30)
p3 = Person('Ana', 25)

people = [p1, p2, p3]

print(sorted(people, key = by_name))
print(sorted(people, key = by_age))
print(sorted(people, key = by_age, reverse=True))