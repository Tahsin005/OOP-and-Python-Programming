class Student:
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name

student1 = Student()
student1.set_name("Tahsin")
print(student1.get_name())

student2 = Student()
student2.set_name("Messi")
print(student2.name)