class employee:
    company = "Wipro"
    def info(self):
        print(f"Name of the employee is {self.name} and works in {self.company}")

class programmer(employee):     # inherited 
    company = "Infosys"         # programmer contains all properties of employee and can even have more propoerties than employee
    def other(self):
        print(f"Name of the employee is {self.name} and works in {self.company}")

a = employee()
a.name = "Gogi"
a.info()
b = programmer()
b.name = "Tappu"
b.other()