class employee:
    language = "python"
    salary = 150
                                        # instance attribute gets preference than class attribute thats why langugage attribute get preference
gogi = employee()
gogi.name = "Gogi"
gogi.language = "Java Script"  # instance attribute  also it does not change the class attribute          
print(gogi.name, gogi.language, gogi.salary, employee.language)   # this last part will print class attribute only instead instance attribute

tapu = employee()
tapu.name = "Tappu"
tapu.language = "Hindi"        # instance attribute
print(tapu.name, tapu.language, tapu.salary)

