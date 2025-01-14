def identify(n):
    if (n%5 == 0):
        return True
    return False

n = [123, 5, 56, 675, 6875, 987654345, 45]

x = list(filter(identify, n)) # filter used to filter smthg from a list like in this above fxn
                            
print(x)