# create a class "employee" and add salary and increment properties to it

class employee:
    salary=234
    increment=20
    @property
    def salaryafterincrement(self):
        return(self.salary + self.salary *(self.increment/100))
    

    @salaryafterincrement.setter
    def salaryafterincrement(self,salary):
        self.increment=((salary/self.salary)-1)*100

e=employee()
# print(e.salaryafterincrement)
e.salaryafterincrement=280.8
print(e.increment)