class name:

    @property                  # makes a method act like an attribute
    def name(self):
        return f"{self.fname}, {self.lname}"
    
    @name.setter               # lets you define a method to set the value of a property
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

a = name()

a.name = "Gogi Puttar"
print(a.fname, a.lname, a.name)
