# class Student:
#     def __init__(self, student_id):
#         self.student_id = student_id
#         print('I am a Student')

#     def display(self):
#         print('I am in Student Class')


# class Tutor:
#     def __init__(self, tutor_id):
#         self.tutor_id = tutor_id
#         print('I am a Tutor')

#     def display(self):
#         print('I am in Tutor Class')


# class StudentTutor(Student, Tutor):
#     def __init__(self, name, s_id, t_id, cgpa):
#         self.name = name
#         super().__init__(s_id)
#         Tutor.__init__(self, t_id)
#         self.cgpa = cgpa

#     def display(self):
#         print("I am in StudentTutor Class")


# st1 = StudentTutor('John', '1234', 'T100', 3.8)
# st1.display()
# print(f'Method Resolution Order: \n{StudentTutor.mro()}')


# print("-----2nd part---")


# class Student:
#     def __init__(self, student_id):
#         self.student_id = student_id
#         print('I am a Student')

#     def display(self):
#         print('I am in Student Class')


# class Tutor:
#     def __init__(self, tutor_id):
#         self.tutor_id = tutor_id
#         print('I am a Tutor')

#     def display(self):
#         print('I am in Tutor Class')


# class StudentTutor(Student, Tutor):
#     def __init__(self, name, s_id, t_id, cgpa):
#         self.name = name
#         super().__init__(s_id)
#         Tutor.__init__(self, t_id)
#         self.cgpa = cgpa

#     def display(self):
#         super().display()
#         Tutor.display(self)


# st1 = StudentTutor('John', '1234', 'T100', 3.8)
# print('-------------')
# st1.display()
# print(f'Method Resolution Order: \n{StudentTutor.mro()}')


# MultiLevel Inheritance

class Person:
    def __init__(self, name):
        self.name = name
        print('I am a Person')

    def display(self):
        print(f'Display method of Person class. My name is {self.name}.')


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
        print('I am a Student')

    def display(self):
        print('I am in Student Class')


class StudentTutor(Student):
    def __init__(self, name, s_id, t_id, cgpa):
        super().__init__(name, s_id)
        self.t_id = t_id
        self.cgpa = cgpa

    def display(self):
        super().display()
        print(f'Name: {self.name}')


st1 = StudentTutor('John', '1234', 'T100', 3.8)
print('-------------')
st1.display()
print(f'Method Resolution Order: \n{StudentTutor.mro()}')
