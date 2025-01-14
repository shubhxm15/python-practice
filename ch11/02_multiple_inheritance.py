class employee:
    company = "Wipro"
    def info(self):
        print(f"Name of the employee is {self.name} and works in {self.company}")


class coder:
    company = "IOT company"
    def name(self, name):
        self.name = name
        print(f"The real coder of our class is {self.name} and he works in {self.company}")

class programmer(employee, coder):     # multiple inherited 
    company = "Infosys"         # programmer contains all properties of employee and can even have more propoerties than employee
    def other(self):
        print(f"Name of the employee is {self.name} and works in {self.company}")

a = employee()
b = programmer()
c = coder()
a.name = "Gogi"
a.info()
b.name = "Tappu"
b.other()
c.name("Dev Khatri")