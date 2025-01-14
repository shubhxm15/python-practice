class one():
    a = 10
class two(one):
    b = 20
class three(two):
    c = 30

d = three()
print(d.a)
print(d.b)
print(d.c)

