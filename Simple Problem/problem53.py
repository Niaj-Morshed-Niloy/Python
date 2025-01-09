#Create a class "programmer" for storage informarion of few programmmers working at Microsoft.

class programmer:
    company="Microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p=programmer("Anon", 120000,4503333)
print(p.name,p.salary,p.pin,p.company)
q=programmer("Niaj", 120000,4503333)
print(q.name,q.salary,q.pin,q.company)
