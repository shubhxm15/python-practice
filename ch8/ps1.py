def large():
    if(a>b and a>c):
        print("The largest number is: ", a)
    elif(b>a and b>c):
        print("The largest number is: ", b)
    elif(c>a and c>b):
        print("The largest number is: ", c)

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

large()