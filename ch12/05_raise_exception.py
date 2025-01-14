a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if(b == 0):
    raise ZeroDivisionError("I cant do that dumb ass")    # we can raise custom errors for mistakes done by the user
else:
    print(f"The divisor is {a/b}")