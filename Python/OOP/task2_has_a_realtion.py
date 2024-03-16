class Student:
    def __init__(self, name, id, cgpa):
        self.name = name
        self.id = id
        self.cgpa = cgpa

    def setId(self, newID):
        self.id = newID


class Department:
    def __init__(self, name):
        self.name = name
        self.studentList = []

    def findStudent(self, id):
        found = False
        for student in self.studentList:
            if id == student.id:
                print(
                    f"Student info:\nStudent Name: {student.name}\nID: {student.id}\nCGPA:  {student.cgpa}")
                found = True
                break
        if found == False:
            print("Student with this ID doesn't exist, Please give a valid ID")

    def addStudent(self, *args):
        for stdnt in args:
            exist = False
            for liststdnt in self.studentList:
                if liststdnt.id == stdnt.id:
                    print(
                        "Student with the same ID already exists, Please try with another ID")
                    exist = True
                    break
            if exist == False:
                self.studentList.append(stdnt)
                print(f"Welcome to CSE department, {stdnt.name}")

    def details(self):
        print(
            f"Department Name: {self.name}\nNumber of student:{len(self.studentList)}\nDetails of the students:")
        for stdnt in self.studentList:
            print(
                f"Student name: {stdnt.name}, ID: {stdnt.id}, cgpa: {stdnt.cgpa}")


s1 = Student("Akib", 22301010, 3.29)
s2 = Student("Reza", 22101010, 3.45)
s3 = Student("Ruhan", 23101934, 4.00)
print("1==================================")
cse = Department("CSE")
cse.findStudent(22112233)
print("2==================================")
cse.addStudent(s1, s2, s3)
print("3==================================")
cse.details()
print("4==================================")
cse.findStudent(22301010)
print("5==================================")
s4 = Student("Nakib", 22301010, 3.22)
cse.addStudent(s4)
print("6==================================")
s4.setId(21201220)
cse.addStudent(s4)
print("7==================================")
cse.details()
print("8==================================")
s5 = Student("Sakib", 22201010, 2.29)
cse.addStudent(s5)
print("9==================================")
cse.details()
