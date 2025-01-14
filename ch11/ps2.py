class complex:

    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, b):
        return complex(self.r + b.r, self.i + b.i)
    
    def __str__(self):
        return f"{self.r} + i{self.i}"

a = complex(1, 2)
b = complex(2, 3)
print(a + b)