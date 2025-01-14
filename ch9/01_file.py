f = open("demo.txt", "r")
data = f.read()                 # to read the file
print(data)
f.close()

add = "Gogo is a bad boy"

f = open("demo1.txt", "w")
data = f.write(add)             # to write smthg in the file
print(data)
f.close()


add = "\nGogi is a bad boy"

f = open("demo.txt", "a")
data = f.write(add)             # to add smthg at the end of the file
print(data)
f.close()