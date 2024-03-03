class GreenPhone:
    def __init__(self, model, androidVersion, camera):
        self.model = model
        self.version = androidVersion
        self.cameraCount = camera
        self.updateCount = 0

    def showSpecification(self):
        print(f"Phone Company: GreenPhone")
        print(f"Model Name: {self.model}")
        print(f"Android Version: {self.version}")
        print(f"Number of Cameras: {self.cameraCount}")

    def updatePhone(self):
        if self.model[0] == 'A':
            if self.updateCount == 2:
                print(
                    f"Your phone Greenphone {self.model} is already up to date.")
            else:
                self.version += 1
                print(
                    f"Your phone Greenphone {self.model} is upgraded to Android Version: {self.version}.")
                self.updateCount += 1
        elif self.model[0] == 'M':
            if self.updateCount == 3:
                print(
                    f"Your phone Greenphone {self.model} is already up to date.")

            else:
                self.version += 1
                print(
                    f"Your phone Greenphone {self.model} is upgraded to Android Version: {self.version}.")
                self.updateCount += 1
        else:
            if self.updateCount == 4:
                print(
                    f"Your phone Greenphone {self.model} is already up to date.")
            else:
                self.version += 1
                print(
                    f"Your phone Greenphone {self.model} is upgraded to Android Version: {self.version}.")
                self.updateCount += 1


print('1=======================')
p1 = GreenPhone('A1', 12, 3)
p2 = GreenPhone('M11', 12, 4)
p3 = GreenPhone('U20', 12, 5)
p1.showSpecification()
print('2=======================')
p2.showSpecification()
print('3=======================')
p1.updatePhone()
print('4=======================')
p1.updatePhone()
p2.updatePhone()
p3.updatePhone()
print('5=======================')
p1.updatePhone()
p2.updatePhone()
p3.updatePhone()
print('6=======================')
p2.updatePhone()
p3.updatePhone()
print('7=======================')
p1.showSpecification()
p3.showSpecification()
