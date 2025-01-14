''' So recursions are basically those funtions who call itself repeatedly'''

def fact(n):
    if(n==1 or n==0):
        return 1
    a = n * fact(n-1)
    return a

n = int(input("Enter a number: "))
print(f"The factorial of this number is: {fact(n)}")           # factorial of a number using recursions
