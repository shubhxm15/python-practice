f = open("demo.txt", "r")
data = f.read()           
print(data)
f.close()

# the same can be done with 'with' statement

with open("demo.txt") as f:
    print(f.read())

# using with statement we dont need to close the file