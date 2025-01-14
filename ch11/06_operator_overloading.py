class overloading:
    def __init__(self, n):
        self.n = n

    def __add__(self, m):
        return self.n + m.n
    
    def __sub__(self, m):
        return self.n - m.n
    
    def __mul__(self, m):
        return self.n * m.n

a = overloading(2)
b = overloading(10)

print(a + b)
print(a - b)
print(a * b)
