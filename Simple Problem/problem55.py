#Add static method in prb 54
#write a class "calculator" capable of finding square, cube and square root of a number.

class calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The square is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"The square is {self.n**1/2}")

    @staticmethod
    def hello():
        print("Hello Anon")

a=calculator(4)
a.hello()
a.square()
a.cube()
a.squareroot()