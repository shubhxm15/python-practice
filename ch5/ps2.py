s = set()

s.add(20)
s.add(20.0)           # in python 20 == 20.0 and the data type doesnt matter if its equal
s.add("20")

print(s)              # so thats why the length is 2 and obviously sets does not repeat the value