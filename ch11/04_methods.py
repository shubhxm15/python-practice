class one():
    a = 10
    def __init__(self):
        print("One constructor")

    @classmethod              # a class method is created for this particular fxn and it always prints the class attribute whenever called
    def only(cls):
        print(f"The value of class attribute a is: {cls.a}")

class two(one):
    b = 20
    def __init__(self):
        print("two constructor")

class three(two):
    c = 30
    
    def __init__(self):
        super().__init__()            # basically it prints the parent constructor also which is two here
        print("three constructor")

d = three()
d.a = 69
print(f"The value of instance attribute a is: {d.a}")
d.only()
print(f"The value of instance attribute b is: {d.b}")
print(f"The value of instance attribute c is: {d.c}")

