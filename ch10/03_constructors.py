class employee:
    language = "python"
    salary = 150

    def __init__(self):         # this is called a dunder method
        print("Object is being created")     # init dunder method automatically executes before an object is created


    def info(self):
        print(f"The name of the employee is {self.name}\nThe employee language is {self.language}\nThe salaray of {self.name} is {self.salary}")


gogi = employee()

gogi.name = "Gogi"
gogi.language = "Java Script"                     
# print(gogi.name, gogi.language, gogi.salary)
gogi.info()
