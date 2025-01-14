s = {1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, "japjot"} 
s1 = {2, 4, 6, 8, 10}

print(s)

print(len(s))                   #prints length of set

s.add(11)
print(s)

print(s.pop())                  # not a good practice to use pop bcz it removes an element randomly
print(s)

print(s.union(s1))              # print every value of both sets without repetetion

print(s.intersection(s1))       # prints only duplicate values


# prints whether it is true or false
print({3,2}.issubset(s))    
print({1,2}.issubset(s1))