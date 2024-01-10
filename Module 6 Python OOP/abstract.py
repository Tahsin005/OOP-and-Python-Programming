from abc import ABC, abstractmethod
# abstract base class
class Animal(ABC):
    @abstractmethod # enforcing all derived class to have a eat method
    def eat(self):
        print('I need food')
    @abstractmethod
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self, name) -> None:
        self.catagory = 'Monkey'
        self.name = name
        super().__init__()
    def eat(self):
        print('Hey nana, i am eating banana')
    def move(self):
        print('Hanging on the branches')
jongbahadur = Monkey('Jongbahadur')
jongbahadur.eat()
jongbahadur.move()