class StudentDatabase:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.grades = {}

    def calculateGPA(self, stringList, semester):
        courseList = []
        tempDict = {}
        totalGPA = 0
        for st in stringList:
            values = st.split(':')
            courseList.append(values[0])
            gpa = float(values[1])
            totalGPA += (gpa*3)
        totalGPA /= len(courseList)*3
        courseList = tuple(courseList)
        tempDict[courseList] = totalGPA
        self.grades[semester] = tempDict

    def printDetails(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")

        for semester, courseAndGPA in self.grades.items():
            print(f"Courses taken in {semester}:")
            for course in courseAndGPA:
                for courseName in course:
                    print(courseName)
                print(f"CGPA: {courseAndGPA[course]}")


s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'], 'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('---------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'], 'Summer2022')
print('---------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('---------------------------------')
s2.printDetails()
