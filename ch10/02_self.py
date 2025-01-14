class employee:
    language = "python"
    salary = 150

    def info(self):
        print(f"The name of the employee is {self.name}\nThe employee language is {self.language}\nThe salaray of {self.name} is {self.salary}")

       # to use funtion in the class we need to use self or we can use anything rather than self its our choice
    
    @staticmethod        # use to define that this function does not need to use any attribute and no need to use self then
    def nthg():
        print("Hello Employees")


gogi = employee()
gogi.nthg()
gogi.name = "Gogi"
gogi.language = "Java Script"                     
# print(gogi.name, gogi.language, gogi.salary)
gogi.info()

tapu = employee()
tapu.name = "Tappu"
tapu.language = "Hindi"
# print(tapu.name, tapu.language, tapu.salary)
tapu.info()
