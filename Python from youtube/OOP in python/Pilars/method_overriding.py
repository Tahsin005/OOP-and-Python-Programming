class Animal:
    def speaks(self):
        pass

class Dog(Animal):
    def speaks(self):
        print("Barks")

class Cat(Animal):
    def speaks(self):
        print("Meow")

class Cow(Animal):
    def speaks(self):
        print("Moo")

dog = Dog()
cat = Cat()
cow = Cow()

dog.speaks()
cat.speaks()
cow.speaks() 