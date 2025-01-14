a = 90      # global variable which can be accessed anywhere

def fun():
    global a   # using this we can change the value of a global variable
    a = 20
    print(a)

fun()
print(a)