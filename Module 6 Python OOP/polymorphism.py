# poly --> many (multiple)
# morph --> shape

class  Animal:
    def __init__(self, name) -> None:
        self.name = name
    
    def make_sound(self):
        print('animal making some sound')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('meow meow')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('gheu gheu')

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('beh beh beh')

    

don = Cat('Real Don')
don.make_sound()

shepard = Dog('Local Shephard')
shepard.make_sound()

messi = Goat('L M')
messi.make_sound()

less = Goat('gora gori')

animals = [don, shepard, messi, less]
for animal in animals:
    print(animal.name)
    animal.make_sound()