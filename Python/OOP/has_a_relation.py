class engine:
    def __init__(self, capacity):
        self.cc = capacity

    def start(self):
        print("The engine has started")


class car:

    def __init__(self, capacity, hasHood):
        self.hood = hasHood
        self.carEngine = engine(capacity)
        # super().__init__(capacity)

    def run(self):
        self.carEngine.start()
        print(f"The car is running at the capacity {self.carEngine.cc}")


firstEngine = engine(150)
firstEngine.start()
VW = car(5000, True)
VW.run()
