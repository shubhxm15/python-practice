from functools import reduce
l = [1, 2, 4, 6, 8, 90, 56, 91, 99]

def greatest(a, b):
    if(a>b):
        return a
    return b

print(reduce(greatest, l))  # reduce check the condition in fxn one by one with every element in the list