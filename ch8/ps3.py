def sum(n):
    if(n==1):
        return 1
    a = sum(n-1) + n
    return a
                                                    # sum for first n natural numbers
n = int(input("Enter a number: "))
print(f"The sum of the numbers are: {sum(n)}")    