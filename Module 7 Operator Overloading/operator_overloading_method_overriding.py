class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def eat(self):
        print('Pizza')
    
    def exercise(self):
        raise NotImplementedError
class Cricketer(Person):
    def __init__(self, name, age, height, weight,team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)
    # override
    def eat(self):
        print('Vegetables')
    
    # override
    def exercise(self):
        print('Stretching ')

    # Operator Overloading
    def __add__(self, other):
        return self.age + other.age
    
    def __mul__(self, other):
        return self.height * other.height
    
    def __len__(self):
        return sakib.weight
    
    def __gt__(self, other):
        return sakib.age > mushi.age
sakib = Cricketer('sakib', 38, 68, 75, 'Bangladesh')
mushi = Cricketer('mushi', 77, 68, 60, 'Bangladesh')
# sakib.eat()
# sakib.exercise()

print(44 + 88)
print('sakib ' + 'mushi')
print(sakib + mushi)
print(sakib * mushi)
print(len(sakib))
print(sakib > mushi)