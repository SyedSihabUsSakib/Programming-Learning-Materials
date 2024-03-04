# Basically no overloading is possible in python OOP but with some techniques we can achieve the goal of overloading

# suppose a class named calculator which has a function called sum(a,b). but unfortunately we wan to add 3 numbers at a time with the help the function called "sum()". So what is the solution?
class calculator:
    # def sum(self, a, b):
    #     return a+b

    # def sum(self, a=None, b=None, c=None): #overloading achieved via fixed number of parameters
    #     if c == None:
    #         return a+b
    #     else:
    #         return a+b+c

    def sum(self, *args):
        val = 0
        for values in args:
            val += values
        return val


user = calculator()
print(user.sum(2, 5))
print(user.sum(4, 9, 11))
print(user.sum(4, 9, 11, 15))
