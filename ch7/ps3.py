n = int(input("Enter a number: "))

for i in range(2, n):
    if(n%i) == 0:                              # divides the number with every digit between 1 to n-1 to check its reminder
        print("Number is not a prime")         # if reminder comes 0 then the number is not prime
        break

else:
    print("Number is prime")