a = int(input("Enter a digit: "))

b = int(input("Enter a digit: "))

c = int(input("Enter a digit: "))

d = int(input("Enter a digit: "))

if(a>b and a>c and a>d):
    print("The greatest number is: ", a)
if(b>a and b>c and b>d):
    print("The greatest number is: ", b)  
if(c>a and c>b and c>d):
    print("The greatest number is: ", c)     # we can also use elif in last 3 conditions
if(d>a and d>b and d>c):
    print("The greatest number is: ", d)