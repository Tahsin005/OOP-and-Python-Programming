class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id
    def __repr__(self) -> str:
        return f'Student with name : {self.name}, class : {self.current_class}, id : {self.id}'

class Teacher:
    def __init__(self, name, subject, id) -> None:
        self.name = name
        self.subject = subject
        self.id = id
    def __repr__(self) -> str:
        return f'Teacher : {self.name}, subject : {self.subject}, id : {self.id}'

class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)
    def enroll(self, name, fee):
        if fee < 6500:
            return 'Not enough fee'
        else:
            id = len(self.students) + 1
            student = Student(name, 12, id)
            self.students.append(student  )
            return f'{name} is enrolled with id : {id}, extra money {fee - 6500}'
    def __repr__(self) -> str:
        print('------------Welcome to Phitron--------------------')
        print('-----------Our Teachers----------------')
        for teacher in self.teachers:
            print(teacher)
        print('----------------Our Students------------')
        for student in self.students:
            print(student)
        return 'All done for now'
    
# alia = Student('MD. Tahsin Ferdous', 12, 1068)
# jafor = Teacher('Jafor Quaderi', 'Di    gital logic design', 101)
# print(alia)
# print(jafor)
phitron = School('Phitron')
phitron.enroll('Tahsin', 6500)
phitron.enroll('Niloy', 6500)
phitron.enroll('Rizu', 6500)

phitron.add_teacher('Rahat Khan Pathan', 'DSA')
phitron.add_teacher('Asif Mohammad Rifat', 'Conceptual Session')

print(phitron)
