n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} * {11 - i} = {n * (11-i)}")      # sum of odered and reversed number is 11  
                                                 # eg: 10 and 1 is 11
                                                 #      9 and 2 is 11 and goes on till 1 and 10
                                                 # here value of i is 1 to 10 and 11 - i gives the reverse order