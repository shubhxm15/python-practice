def pattern():
    for i in range(1, n+1):
        print("*" * ((n+1) - i), end="")
        print("")                                 # using functions

n = int(input("Enter a number: "))
pattern()


def patt(n):
    if(n==0):
        return
    print("*" * n)
    patt(n-1)

n = int(input("Enter a number: "))               # using recursive functions
patt(n)


'''

*****
****    n = 5
***
**
*

'''