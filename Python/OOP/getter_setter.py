# Abstraction
class person:
    def __init__(self, name, height, age):
        self.__name = name
        self.height = height
        self.age = age

    @property  # read only->getter method
    def name(self):
        return self.__name

    @name.setter
    def name(self, newName):
        self.__name = newName


anto = person("anto", 6, 25)
print(anto.name, anto.height, anto.age)

# anto.name = "jontu"
# anto.__name = "Jontu"
anto.name = "hamba"
print(anto.name, anto.height, anto.age)
