class Parent:
    def __init__(self):
        self.super_attribute = True
        print("This is parent class")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("This is child class")
        print(self.super_attribute)

child1 = Child()

'''Types of inheritance
1. Single inheritance
2. Multiple inheritance
3. Multilevel inheritance
4. Hierarchical inheritance
5. Hybrid inheritance - combined with multiple and multileve inheritance
'''