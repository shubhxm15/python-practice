# function definition
def average():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))

    d = (a + b + c)/3
    print("The average is: ", d)

print("Hello Everyone..!!")

# function call
average()

# function with arguments
def call(name):
    print(f"Hello my name is {name}")
    return "Nice to meet you..!!"          # return value of the function which is stored in a 

a = call("Gogi Puttar")
print(a)