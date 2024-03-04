# is a realtion is basically nothing but inheritance

class person:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def walk(self):
        print(f"the {self} started walking")


class employee(person):
    def __init__(self, height, weight, salary):
        self.salary = salary
        super().__init__(height, weight)

    def work(self):
        print("The employee started working")


nahiyan = person(55, 60)
nahiyan.walk()

sihab = employee(57, 66, 100)
sihab.walk()
sihab.work()
print(sihab.salary, sihab.height)
